# Python 3 server example
from http.server import BaseHTTPRequestHandler, HTTPServer
import git
import time
import os
import json

hostName = "localhost"
serverPort = 80

git = git.Repo('.').git
repoHash = git.rev_parse("HEAD", short=True)
repoTag = git.describe(tags=True)
repoName = os.path.basename(git.rev_parse(show_toplevel=True))

class WebServer(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes("<html><head><title>Health</title></head>", "utf-8"))
            self.wfile.write(bytes("<p>Repo Hash: %s</p>" % repoHash, "utf-8"))
            self.wfile.write(bytes("<p>Repo Name: %s</p>" % repoName, "utf-8"))
            self.wfile.write(bytes("<p>Repo Version: %s</p>" % repoTag, "utf-8"))
        else:
            self.send_response(404)

if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), WebServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")