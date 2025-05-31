#!/usr/bin/env python3

import unittest
from parameterized import parameterized
from unittest.mock import patch, PropertyMock
from client import GithubOrgClient

class TestGithubOrgClient(unittest.TestCase):

    @parameterized.expand(['google', 'abc'])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        expected = {"login": org_name}
        mock_get_json.return_value = expected

        client = GithubOrgClient(org_name)
        self.assertEqual(client.org, expected)
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
        )

    def test_public_repos_url(self):
        """
        Test that _public_repos_url returns the correct repos_url.
        """
        with patch(
            'client.GithubOrgClient.org',
            new_callable=PropertyMock
        ) as mock_org:
            mock_org.return_value = {
                "repos_url": "https://api.github.com/orgs/check/"
            }
            client = GithubOrgClient("test")
            self.assertEqual(
                client._public_repos_url,
                "https://api.github.com/orgs/check/"
            )        

    def test_public_repos(self):
        with patch('client.get_json') as mock_get_json:
            mock_get_json.return_value = {
                "repos_url": "https://api.github.com/orgs/test/repos"
            }

            with patch('client.GithubOrgClient.org', new_callable=PropertyMock) as mock_org:
                mock_org.return_value = {
                    "repos_url": "https://api.github.com/orgs/test/repos"
                }

                client = GithubOrgClient("test")
                result = client._public_repos_url

                self.assertEqual(result, "https://api.github.com/orgs/test/repos")
                mock_org.assert_called_once()
                mock_get_json.assert_called_once()
