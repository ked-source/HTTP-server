# HTTP-server
<p align="justify">This is a Python script that creates a TCP server socket to serve HTTP requests. The server listens on port 12345 on the local host. When a client connects, it receives the request, extracts the filename from the request, and opens the corresponding file from a local directory. If the file is found, the server sends an HTTP OK response with the file's content as the response body. If the file is not found, the server sends an HTTP NotFound response.</p>

<p align="justify">Additionally, the server sets a cookie in the response with a value of "This is my cookie". The cookie is set in the Set-Cookie header of the response. This can be used to track user sessions or preferences.</P>

<p align="justify">The code includes error handling for file not found errors, and it closes the connection socket after sending the response. The server runs indefinitely in a loop, waiting for new connections. Once a connection is established, it processes the request and sends the response, then closes the connection. Finally, the server socket is closed.</p>
