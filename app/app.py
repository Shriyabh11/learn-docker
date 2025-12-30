from http.server import HTTPServer, BaseHTTPRequestHandler
import os

DATA_FILE = "/data/count.txt"

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Hello from Docker\n")

        elif self.path == "/count":
            count = 0
            if os.path.exists(DATA_FILE):
                with open(DATA_FILE) as f:
                    count = int(f.read())

            count += 1
            os.makedirs("/data", exist_ok=True)
            with open(DATA_FILE, "w") as f:
                f.write(str(count))

            self.send_response(200)
            self.end_headers()
            self.wfile.write(f"Count: {count}\n".encode())

httpd = HTTPServer(("0.0.0.0", 8000), Handler)
print("Server running on port 8000")
httpd.serve_forever()
