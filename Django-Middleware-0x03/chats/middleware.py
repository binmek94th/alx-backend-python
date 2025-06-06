from datetime import datetime


class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user = request.user.username if request.user.is_authenticated else 'Anonymous'

        open(f"requests.log", 'a').write(
            f"{datetime.now().isoformat()} - User: {user}, Path: {request.path}\n"
        )

        response = self.get_response(request)

        return response
