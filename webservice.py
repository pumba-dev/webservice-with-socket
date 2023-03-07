class Message:
    def __init__(self, sender, receiver, subject, content):
        self.sender = sender
        self.receiver = receiver
        self.subject = subject
        self.content = content  

class MailService:
    def __init__(self):
        self.messages = []

    def sendMessage(self, message):
        self.messages.append(message)
        return {"Mensagem enviada com sucesso."}