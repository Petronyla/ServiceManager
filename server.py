from http.server import BaseHTTPRequestHandler,HTTPServer
import sys
import random

class myHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == sys.argv[1]:
            if random.random() < float(sys.argv[3]):
                self.send_response(200)
                self.send_header('Content-type','text/html')
                self.end_headers()
                self.wfile.write("OK".encode())
            else:
                self.send_response(503)
                self.send_header('Content-type','text/html')
                self.end_headers()
                self.wfile.write("Error".encode())
        else:
            self.send_response(404)
            self.send_header('Content-type','text/html')
            self.end_headers()
            self.wfile.write("Not Found".encode())


server = HTTPServer(('', int(sys.argv[2])), myHandler)
print('Started httpserver')

server.serve_forever()
