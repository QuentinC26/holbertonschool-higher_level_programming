#!/usr/bin/python3
import http.server

port = 8000
adress = ("", port)

server = http.server.HTTPServer
handler = http.server.SimpleHTTPRequestHandler

print("Hello, this is a simple API!")

httpd = server(adress, handler)

def the_condition(self):
    if adress == ("http://localhost/data", port):
        return {"name": "John", "age":30, "city": "New York"}
    if adress == ("http://localhost/info", port):
        return {"version": "1.0", "description": "A simple API built with http.server"}
    if adress == ("http://localhost/status", port):
        return ok
    else:
        return "404 Not Found"

httpd.serve_forever()
