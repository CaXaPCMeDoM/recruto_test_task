class Message:
    def __init__(self, name: str, message: str):
        self.name = name
        self.message = message
    
    def get_formatted_message(self) -> str:
        return f"Hello {self.name}! {self.message}!"