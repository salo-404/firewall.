from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse

MALICIOUS_PATH = "/tomcatwar.jsp"
MALICIOUS_KEYS = [
    "class.module.classLoader.resources.context.parent.pipeline.first.pattern"
]
MALICIOUS_HEADER_VALUES = ["suffix=%>//", "c1=Runtime", "c2=<%"]
MALICIOUS_PAYLOAD_SIGNATURES = ["Runtime.getRuntime", "%>//", "<%"]

class FirewallHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path == MALICIOUS_PATH:
            content_length = int(self.headers.get('Content-Length', 0))
            post_data = self.rfile.read(content_length).decode("utf-8")
            post_params = urllib.parse.parse_qs(post_data)

            for key in post_params:
                if key in MALICIOUS_KEYS:
                    self.block_request("Malicious key detected in POST data.")
                    return

            for values in post_params.values():
                for val in values:
                    if any(sig in val for sig in MALICIOUS_PAYLOAD_SIGNATURES):
                        self.block_request("Suspicious Java payload detected in POST values.")
                        return

            for header, value in self.headers.items():
                if any(indicator in value for indicator in MALICIOUS_HEADER_VALUES):
                    self.block_request("Malicious pattern found in headers.")
                    return

        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"POST request processed safely.")

    def block_request(self, reason):
        print(f"[BLOCKED] {self.client_address[0]} - {reason}")
        self.send_response(403)
        self.end_headers()
        self.wfile.write(f"Request blocked by firewall: {reason}".encode("utf-8"))

def run(server_class=HTTPServer, handler_class=FirewallHTTPRequestHandler, port=8080):
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    print(f"Firewall HTTP server running on port {port}...")
    httpd.serve_forever()

if __name__ == "__main__":
    run()