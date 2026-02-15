import uvicorn
from fin_app import create_app
from fin_app.settings.config import HOST, PORT

if __name__ == "__main__":
    server_port = int(PORT)  # SR: safety for docker
    app = create_app()
    uvicorn.run("main:app", host=HOST, port=server_port, reload=True)
