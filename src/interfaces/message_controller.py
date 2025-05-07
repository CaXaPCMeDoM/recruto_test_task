from src.use_cases.message_use_case import MessageUseCase

class MessageController:
    def __init__(self, message_use_case: MessageUseCase):
        self.message_use_case = message_use_case
    
    def handle_greeting_request(self, name: str, message: str) -> str:
        return self.message_use_case.generate_greeting(name, message)