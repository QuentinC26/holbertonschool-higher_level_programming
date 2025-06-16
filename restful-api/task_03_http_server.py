#!/usr/bin/python3
import http.server

port = 8000
adress = ("", port)

server = http.server.HTTPServer
handler = http.server.SimpleHTTPRequestHandler

print("Hello, this is a simple API!")

httpd = server(adress, handler)
httpd.serve_forever()
