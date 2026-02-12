from http.server import HTTPServer, BaseHTTPRequestHandler

class OurHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write("<h1>Hello from Effective Mobile!</h1>".encode('utf-8'))
        elif self.path == '/health':
            self.send_response(200)
            self.end_headers()
        else:
            self.send_response(404)
            self.end_headers()


if __name__ == "__main__":
    with HTTPServer(('', 8080), OurHandler) as server:
        server.serve_forever()
