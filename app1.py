# app1.py
from http.server import SimpleHTTPRequestHandler
import socketserver

# set ip and port to listen (vpn)
http_port = 8080
http_ip = "10.0.0.1"

class Handler(SimpleHTTPRequestHandler):
    server_version = 'Lab Server'
    sys_version = 'Simple HTTPS'

handler = Handler
httpd = socketserver.TCPServer((http_ip, http_port), handler)
print("Starting HTTP Server", "on Port:", http_port)

if __name__ == '__main__':
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
