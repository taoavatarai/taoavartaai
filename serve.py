import http.server
import socketserver
import socket

PORT = 5000
HOST = "0.0.0.0"

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.path = "/avatar_ai_spatial.html"
        return super().do_GET()

    def log_message(self, format, *args):
        pass

class ReusableTCPServer(socketserver.TCPServer):
    allow_reuse_address = True

with ReusableTCPServer((HOST, PORT), Handler) as httpd:
    print(f"Serving on {HOST}:{PORT}", flush=True)
    httpd.serve_forever()
