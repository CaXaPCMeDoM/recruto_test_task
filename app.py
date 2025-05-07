import os
from dotenv import load_dotenv
from src.frameworks.web_app import create_app

load_dotenv()

app = create_app()

if __name__ == '__main__':
    host = os.environ['HOST']
    port = int(os.environ['PORT'])
    app.run(host=host, port=port)
