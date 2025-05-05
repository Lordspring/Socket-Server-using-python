import socketserver as SKT

class MyTCPServer(SKT.TCPServer):
    pass

class MyRequestHandler(SKT.BaseRequestHandler):
    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        # print(type(self.data))
        # print(self.data)
        recievedstr = str(self.data)
        recievedstr = recievedstr[2:]
        # print(type(recievedstr))
        # print(recievedstr)
        words = int(recievedstr.count(' '))
        words += 1
        lowerCase = 0
        upperCase = -1
        digits = 0
        
        for i in recievedstr:
            if(i.islower()):
                lowerCase+=1
            elif(i.isupper()):
                upperCase+=1
            elif (i.isnumeric()):
                digits += 1
        if(recievedstr.startswith('W')):
            print(f"The number of words is: {words}")
            self.request.sendall(bytes(str(words), "utf-8"))
        elif(recievedstr.startswith('L')):
            print(f"The number of lowercase letters is: {lowerCase}")
            # print(f"number of lowercase letters = {bytes(lowerCase)}")
            self.request.sendall(bytes(str(lowerCase), "utf-8"))
        elif(recievedstr.startswith('U')):
            print(f"The number of uppercase letters is: {upperCase}")
            self.request.sendall(bytes(str(upperCase), "utf-8"))
        elif(recievedstr.startswith('R')):
            print(f"The number of numeric characters is: {digits}")
            self.request.sendall(bytes(str(digits), "utf-8"))
        elif(recievedstr.startswith('T')):
            print(f"The number of characters is: {len(recievedstr) - 1}")
            self.request.sendall(bytes(str(len(recievedstr) - 1), "utf-8"))
        elif(recievedstr == "exit"):
            server.shutdown()
        else:
            self.request.sendall(bytes(recievedstr, "utf-8"))

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999
    server = MyTCPServer((HOST, PORT), MyRequestHandler)
    server.serve_forever()