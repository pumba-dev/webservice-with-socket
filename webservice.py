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
        return {"Mensagem enviada com sucesso."}

def parseRequest(request):
    json_pattern = r'\{.*\}'
    match = re.search(json_pattern, request, re.DOTALL)
    method, url, http_version = request.split("\n")[0].split(" ")
    body = match.group(0) if match else None
    return method, url, body

def parseResponse(response):
    response_headers = "HTTP/1.1 " + response["status"] + "\n"
    response_headers += "Content-Type: application/json\n"
    response_body = json.dumps(response)
    response_headers += "Content-Length: " + str(len(response_body)) + "\n\n"
    response = response_headers + response_body
    return response

## Web Service Start ##
message_server = MailService()

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 8081))
server_socket.listen()

print("Servidor iniciado na porta 8081...")

while True:
    (client_socket, client_address) = server_socket.accept()
    request = client_socket.recv(4096).decode()

    method, url, body = parseRequest(request)

    if url == "/send" and method == "POST":
        message_data = json.loads(body)
        message = Message(**message_data)
        response = message_server.sendMessage(message)

    elif url == "/list" and method == "GET":
        response = message_server.listMessages()

    response = parseResponse(response)
    client_socket.sendall(response.encode())
    client_socket.close()