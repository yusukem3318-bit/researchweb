import http.server
import os

os.chdir('/Users/yusuke.m/Desktop/research-website')
handler = http.server.SimpleHTTPRequestHandler
with http.server.HTTPServer(('', 8765), handler) as httpd:
    httpd.serve_forever()
