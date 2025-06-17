#!/usr/bin/python3
import http.server
import SimpleHTTPServer
import json

class the_server(http.server.BaseHTTPRequestHandler):
    def DO_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write("Hello, this is a simple API!")
        elif self.path == '/data':
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(data).encode('utf8'))
        elif self.path == '/status':
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(json.dumps(data).encode('utf8'))
        elif self.path == '/info':
            info = {
                "version": 1.0,
                "description": "A simple API built with http.server"
            }
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(info).encode('utf8'))
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write("Endpoint not found")

if __name__ == "__main__":
    port = 8000
    adress = ("", port)
    server = http.server.HTTPServer
    handler = http.server.SimpleHTTPRequestHandler
    httpd = server(adress, handler)
    httpd.serve_forever()
