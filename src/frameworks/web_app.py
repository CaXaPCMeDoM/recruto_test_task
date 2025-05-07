from flask import Flask, request
from src.interfaces.message_controller import MessageController
from src.use_cases.message_use_case import MessageUseCase

def create_app():
    app = Flask(__name__)

    message_use_case = MessageUseCase()
    message_controller = MessageController(message_use_case)

    @app.route('/')
    def index():
        name = request.args.get('name')
        message = request.args.get('message')

        if name is None or message is None:
            return "Please provide both 'name' and 'message' parameters in the URL. Example: /?name=Recruto&message=Давай дружить"

        return message_controller.handle_greeting_request(name, message)

    return app
