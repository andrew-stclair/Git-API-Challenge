# Python 3 server example
from http.server import BaseHTTPRequestHandler, HTTPServer
import git
import os

hostName = "0.0.0.0"
serverPort = 80

git = git.Repo('.').git
repoHash = git.rev_parse("HEAD", short=True)
repoTag = git.describe(tags=True)
repoName = os.path.basename(git.rev_parse(show_toplevel=True))

class WebServer(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            self.send_response(200)
            self.send_header("Content-type", "text/json")
            self.end_headers()
            self.wfile.write(bytes("{\"hash\": \"%s\", \"name\": \"%s\", \"version\": \"%s\"}" % (repoHash, repoName, repoTag), "utf-8"))
        else:
            self.send_response(404)

if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), WebServer)
    print("Server started at http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")