from src.domain.message_entity import Message

class MessageUseCase:
    def generate_greeting(self, name: str, message: str) -> str:
        message_entity = Message(name, message)
        return message_entity.get_formatted_message()