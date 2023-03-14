from socket import *

#Create a TCP server socket
#Code Start
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('localhost', 12345))
serverSocket.listen()
#Code End

while True:
    #Establish the connection
    print("The server is ready to receive")
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(1024).decode()
        filename = message.split()[1]
        f = open("./html_files/" + filename[1:])
        outputdata = f.read()

        #Send HTTP OK and the Set-Cookie header into the socket
        # set the cookie to whatever value you'd like
        #Code Start
        response = 'HTTP/1.1 200 OK\r\n'
        response += 'Set-Cookie: mycookie=This is my cookie\r\n'
        response += f'Content-Length: {len(outputdata)}\r\n'
        response += 'Content-Type: text/html\r\n'
        response += '\r\n'
        connectionSocket.sendall(response.encode())
        #Code End

        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())

        # Close the socket
        #Code Start
        connectionSocket.close()
        #Code End

    except IOError:
        #Send HTTP NotFound response
        #Code Start
        response = 'HTTP/1.1 404 NotFound\r\n'
        response += 'Content-Length: 0\r\n'
        response += 'Content-Type: text/html\r\n'
        response += '\r\n'
        connectionSocket.sendall(response.encode())
        #Code End
        
        # Close the socket
        #Code Start
        connectionSocket.close()
        #Code End
        
serverSocket.close()
