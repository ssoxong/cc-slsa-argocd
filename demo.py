from http.server import BaseHTTPRequestHandler, HTTPServer

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain; charset=utf-8")
        self.end_headers()
        self.wfile.write(b"Hello, SLSA Level 3!")

if __name__ == "__main__":
    server_address = ("", 8080)
    httpd = HTTPServer(server_address, MyHandler)
    print("Server running on :8080")
    httpd.serve_forever()
