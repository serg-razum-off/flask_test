import os

# SR: will be set as env variables APP_HOST and APP_PORT on docker
HOST = os.getenv("APP_HOST", "127.0.0.1")
PORT = os.getenv("APP_PORT", 8000)
