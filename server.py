import http.server
import socketserver

PORT = 8081

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/prompt':
            self.handle_prompt_request()
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()

    def handle_prompt_request(self):
        print("receiving prompt")
        content_length = self.headers.get('Content-Length')
        if content_length is None:
            self.send_response(411)  # Length Required
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Content-Length header is missing.")
            return

        post_data = self.rfile.read(int(content_length))
        prompt_request = post_data.decode('utf-8')

        # Export to shell variable and call echo
        import os
        os.environ['PROMPT_REQUEST'] = prompt_request
        os.system(f'echo {prompt_request}')
        os.system(f'echo {prompt_request} > prompt_request.txt')
        print("running aider")
        os.system(f'./aider.sh')
        print("done!")

        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Prompt request received and processed.")

Handler = CustomHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()
