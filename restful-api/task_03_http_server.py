#!/usr/bin/python3
import http.server
import socketserver
import json

PORT = 8000
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Hello, this is a simple API!", PORT)
    httpd.serve_forever()