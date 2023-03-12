import socket
import json
import re
class Message:
    def __init__(self, index, sender, receiver, subject, content):
        self.id = index
        self.sender = sender
        self.receiver = receiver
        self.subject = subject
        self.content = content  

class MailService:
    def __init__(self):
        self.messages = []
        self.listCount = 0

    def listMessages(self):
        return {"status": "200", "data": [vars(m) for m in self.messages]}

    def listByReceiver(self, receiver): 
        messages = [m for m in self.messages if m.receiver == receiver]
        return {"status": "200", "data": [vars(m) for m in messages]}
    
    def sendMessage(self, message):
        newMessage = Message(self.listCount, **message)
        self.messages.append(newMessage)
        self.listCount += 1
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
        newMessage = Message(self.listCount, sender, receiver, "FW: "+message.subject, message.content)
        self.messages.append(newMessage)
        self.listCount += 1
        return {"status": "200", "message": "Mensagem encaminhada com sucesso."}

    def replyMessage(self, index, content):
        if index >= len(self.messages):
            return {"status": "404", "message": "Índice inválido."}
        message = self.messages[index]
        newMessage = Message(self.listCount, message.receiver, message.sender, "RE: "+message.subject, content)
        self.messages.append(newMessage)
        self.listCount += 1
        return {"status": "200", "message": "Mensagem respondida com sucesso."}

def parseRequest(request):
    bodyPattern = r'\{.*\}'
    headerPattern = r'^(\w+) (\S+) (HTTP/\d+\.\d+)'
    bodyMatch = re.search(bodyPattern, request, re.DOTALL)
    headerMatch = re.search(headerPattern, request, re.MULTILINE)
    body = bodyMatch.group(0) if bodyMatch else ""
    method = headerMatch.group(1) if headerMatch else ""
    url = headerMatch.group(2) if headerMatch else ""
    return method, url, body

def parseResponse(response):
    responseHeaders = "HTTP/1.1 " + response['status'] + "\n"
    responseHeaders += "Content-Type: application/json\n"
    responseHeaders += 'Access-Control-Allow-Origin: *\r\n'
    responseHeaders += 'Access-Control-Allow-Headers: Content-Type, Access-Control-Allow-Origin\r\n'
    responseBody = json.dumps(response)
    responseHeaders += "Content-Length: " + str(len(responseBody)) + "\n\n"
    response = responseHeaders + responseBody
    return response

## Web Service Start ##
messageService = MailService()

socketServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socketServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
socketServer.bind(('', 8081))
socketServer.listen()

print("Servidor iniciado na porta 8081...")

while True:
    (connection, adress) = socketServer.accept()
    request = connection.recv(4096).decode()
    print('Recebido:', request)
    print()

    method, url, body = parseRequest(request)

    if method == "OPTIONS":
        response = {"status": "200 OK", "message": "Url não encontrada."}

    elif url == "/list" and method == "GET":
        response = messageService.listMessages()
    
    elif url.startswith("/listByReceiver") and method == "GET":
        receiver = url.split("/")[-1]
        response = messageService.listByReceiver(receiver)

    elif url.startswith("/send") and method == "POST":
        message_data = json.loads(body)
        response = messageService.sendMessage(message_data)

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
        response = {"status": "404", "message": "Url nao encontrada."}

    response = parseResponse(response)
    connection.sendall(response.encode())
    connection.close()