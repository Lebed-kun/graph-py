from http.server import HTTPServer, BaseHTTPRequestHandler
from cparser import Parser

class GraphRequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        try:
            self.send_header("Access-Control-Allow-Origin", "*")

            if self.path == "/graphs":
                contentLength = int(self.headers.get("Content-Length"))
                body = self.rfile.read(contentLength)
                newData = Parser(body).parse()

                self.send_response(200)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.end_headers()

                self.wfile.write(newData.encode())
            else:
                self.send_response(404)
                self.wfile.write("\nUnknown service!".encode())
        except Exception as e:
            self.send_response(500)
            self.wfile.write("\n" + str(e).encode())

        
def runServer():
    server = HTTPServer(('', 8000), GraphRequestHandler)

    server.serve_forever()

runServer()
