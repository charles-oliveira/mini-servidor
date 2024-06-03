import os
from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            filepath = self.path.lstrip('/')
            if not filepath:
                filepath = 'index.html'

            if not os.path.isfile(filepath):
                raise FileNotFoundError

            content_type = 'text/html'
            if filepath.endswith('.css'):
                content_type = 'text/css'
            elif filepath.endswith('.js'):
                content_type = 'application/javascript'

            with open(filepath, 'rb') as file:
                content = file.read()

            self.send_response(200)
            self.send_header('Content-type', content_type)
            self.end_headers()
            self.wfile.write(content)
            print(f"200 OK: {filepath}")

        except FileNotFoundError:
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b"<html><body><h1>404 Not Found</h1></body></html>")
            print(f"404 Not Found: {filepath}")

        except Exception as e:
            self.send_response(500)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b"<html><body><h1>500 Internal Server Error</h1></body></html>")
            print(f"500 Internal Server Error: {e}")

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler):
    server_address = ('', 8080)
    httpd = server_class(server_address, handler_class)
    print('Servidor HTTP rodando na porta 8080...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
