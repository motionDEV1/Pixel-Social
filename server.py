

from http.server import BaseHTTPRequestHandler, HTTPServer
import os

# Create custom HTTPRequestHandler class
class MyHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        rootdir = 'index.html'  # Set the directory where your HTML files are located
        try:
            if self.path.endswith('.html'):
                f = open(rootdir + self.path)  # Open the requested file
                self.send_response(200)  # Send a 200 OK response
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(f.read().encode())  # Send file content to the client
                f.close()
                return
        except IOError:
            self.send_error(404, 'File nost found')

def run():
    print('HTTP server is starting...')
    server_address = ('127.0.0.1', 8000)  # Set the IP address and port
    httpd = HTTPServer(server_address, MyHTTPRequestHandler)
    print('HTTP server is running...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
