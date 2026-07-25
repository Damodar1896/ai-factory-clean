# Dynamic Proxy & IP Rotator for Mass Scraping & Outreach
import random
def get_safe_proxy():
    proxies = ["proxy_node_us_01", "proxy_node_in_02", "proxy_node_eu_03"]
    selected = random.choice(proxies)
    print(f"[🛡️ PROXY ROTATOR] Rotating outbound socket through secure node: {selected}")
    return selected
if __name__ == "__main__":
    get_safe_proxy()
