from http.server import HTTPServer, BaseHTTPRequestHandler

PORT_NUMBER = 80

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Hello, world!')


try:
  #Create a web server and define the handler to manage the
  #incoming request
  server = HTTPServer(('', PORT_NUMBER), SimpleHTTPRequestHandler)
  print('Started httpserver on port ' , PORT_NUMBER)

  #Wait forever for incoming htto requests
  server.serve_forever()

except KeyboardInterrupt:
  print('^C received, shutting down the web server')
  server.socket.close()
