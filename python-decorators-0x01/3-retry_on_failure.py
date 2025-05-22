import time
import sqlite3 
import functools

def with_db_connection(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect('users.db')
        try:
            return func(*args, **{**kwargs, 'conn': conn})
        finally:
            conn.close()
    return wrapper

def retry_on_failure(retries, delay):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempts in range(1, retries + 1):
                try:
                    results = func(*args, **kwargs)
                except Exception as e:
                    print('failed', e)
                    if attempts < retries:
                        time.sleep(delay)
                    else:
                        print("All retries failed.")
                        raise
            return results
        return wrapper
    return decorator


@with_db_connection
@retry_on_failure(retries=3, delay=1)
def fetch_users_with_retry(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()


users = fetch_users_with_retry()
print(users)