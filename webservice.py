import socket
import json
import re
class Message:
    def __init__(self, sender, receiver, subject, content):
        self.sender = sender
        self.receiver = receiver
        self.subject = subject
        self.content = content  

class MailService:
    def __init__(self):
        self.messages = []

    def listMessages(self):
        return {"status": "200", "data": [vars(m) for m in self.messages]}

    def sendMessage(self, message):
        self.messages.append(message)
        return {"status": "200", "message": "Mensagem enviada com sucesso."}

    def deleteMessage(self, index):
        if index >= len(self.messages):
            return {"status": "404", "message": "Índice inválido."}
        self.messages.pop(index)
        return {"status": "200", "message": "Mensagem excluída com sucesso."}

    def openMessage(self, index):
        if index >= len(self.messages):
            return {"status": "404", "message": "Índice inválido."}
        return {"status": "200", "data": vars(self.messages[index])}

    def forwardMessage(self, index, sender, receiver):
        if index >= len(self.messages):
            return {"status": "404", "message": "Índice da mensagem inválido."}
        message = self.messages[index]
        newMessage = Message(sender, receiver, "FW: "+message.subject, message.content)
        self.messages.append(newMessage)
        return {"status": "200", "message": "Mensagem encaminhada com sucesso."}

    def replyMessage(self, index, content):
        if index >= len(self.messages):
            return {"status": "404", "message": "Índice inválido."}
        message = self.messages[index]
        newMessage = Message(message.receiver, message.sender, "RE: "+message.subject, content)
        self.messages.append(newMessage)
        return {"status": "200", "message": "Mensagem respondida com sucesso."}

def parseRequest(request):
    jsonPattern = r'\{.*\}'
    match = re.search(jsonPattern, request, re.DOTALL)
    method, url, httpVersion = request.split("\n")[0].split(" ")
    body = match.group(0) if match else None
    return method, url, body

def parseResponse(response):
    responseHeaders = "HTTP/1.1 " + response["status"] + "\n"
    responseHeaders += "Content-Type: application/json\n"
    responseBody = json.dumps(response)
    responseHeaders += "Content-Length: " + str(len(responseBody)) + "\n\n"
    response = responseHeaders + responseBody
    return response

## Web Service Start ##
messageService = MailService()

socketServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socketServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
socketServer.bind(('localhost', 8081))
socketServer.listen()

print("Servidor iniciado na porta 8081...")

while True:
    (connection, adress) = socketServer.accept()
    request = connection.recv(4096).decode()

    method, url, body = parseRequest(request)

    if url == "/list" and method == "GET":
        response = messageService.listMessages()

    elif url == "/send" and method == "POST":
        message_data = json.loads(body)
        message = Message(**message_data)
        response = messageService.sendMessage(message)

    elif url.startswith("/delete") and method == "DELETE":
        index = int(url.split("/")[-1])
        response = messageService.deleteMessage(index)

    elif url.startswith("/open") and method == "GET":
        index = int(url.split("/")[-1])
        response = messageService.openMessage(index)

    elif url.startswith("/forward") and method == "POST":
        message_data = json.loads(body)
        index = int(message_data["messageID"])
        sender = message_data["sender"]
        receiver = message_data["receiver"]
        response = messageService.forwardMessage(index, sender, receiver)

    elif url.startswith("/reply") and method == "POST":
        message_data = json.loads(body)
        index = int(message_data["messageID"])
        content = message_data["content"]
        response = messageService.replyMessage(index, content)

    else:
        response = {"status": "404", "message": "URL não encontrada."}

    response = parseResponse(response)
    connection.sendall(response.encode())
    connection.close()