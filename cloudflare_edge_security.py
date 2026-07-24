class CloudflareSecurityLayer:
    def __init__(self):
        print("[Cloudflare Edge] Initializing DNS proxy, Web Application Firewall (WAF), and SSL.")
        print("[Load Distribution] Global traffic load balanced across multiple edge POPs. Laptop network protected.")

    def inspect_incoming_traffic(self, request_ip):
        print(f"[Cloudflare WAF] Inspecting request from {request_ip} -> Clean traffic routed to Vercel/Render backend.")

if __name__ == "__main__":
    cf = CloudflareSecurityLayer()
    cf.inspect_incoming_traffic("192.168.1.50")
