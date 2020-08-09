import multiprocessing
import os


def env(key, default=None):
    return os.environ.get(key, default)


bind = f"0:{env('PORT', '8000')}"

preload_app = True

max_requests = env("GUNICORN_MAX_REQUESTS", 1000)
max_requests_jitter = env("GUNICORN_MAX_REQUESTS_JITTER", 100)

workers = env("GUNICORN_WORKERS", multiprocessing.cpu_count() * 2)
