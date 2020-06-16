from http.server import HTTPServer, BaseHTTPRequestHandler
from cparser import Parser

class GraphRequestHandler(BaseHTTPRequestHandler):
    def do_POST(self, path):
        try:
            self.send_header("Access-Control-Allow-Origin", "*")

            if self.path == "/graphs":
                contentLength = int(self.headers.get("Content-Length"))
                body = self.rfile.read(contentLength)
                newData = Parser(body).parse()

                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.end_headers()

                self.wfile.write(newData)
                self.wfile.close()
            else:
                self.send_response(404)
                self.wfile.write("Unknown service!")
                self.wfile.close()
        except:
            self.send_response(500)
            self.wfile.write("Invalid data format!")
            self.wfile.close()

        
def runServer():
    server = HTTPServer(('', 8000), GraphRequestHandler)

    try:
        server.serve_forever()
    except:
        server.server_close()
