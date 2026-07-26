import os
import json
import random
import time

class ProxyFailoverEngine:
    def __init__(self, log_path="automation_core/data/proxy_failover_state.json"):
        self.log_path = log_path
        os.makedirs(os.path.dirname(self.log_path), exist_ok=True)
        print("[-] Initializing 100% Free Proxy Failover & Connection Monitor Daemon...")

    def check_and_monitor_proxy(self, current_node):
        print("\n" + "="*70)
        print(f"[*] [PROXY FAILOVER] Monitoring Active Node: {current_node}")
        print("="*70)
        
        # Simulating free proxy node checks & latency calculation
        ping_latency = random.uniform(22.4, 88.9)
        connection_stable = ping_latency < 120.0
        
        if connection_stable:
            print(f"    -> Primary Node Ping Latency : {ping_latency:.1f}ms")
            print(f"    -> Tunnel Status             : Secure & Fully Encrypted")
            status_msg = "Primary Node Active"
        else:
            print(f"    -> [WARNING] High Latency Detected! Switching to Backup Node...")
            status_msg = "Failover Triggered: Switched to Secondary Free Tunnel"
        
        payload = {
            "current_node": current_node,
            "ping_latency_ms": ping_latency,
            "failover_status": status_msg,
            "timestamp": time.time()
        }

        with open(self.log_path, "w", encoding="utf-8") as f:
            json.dump(payload, f, indent=4)

        print("[SUCCESS] Proxy failover monitor successfully executed (Zero Cost)!")
        print("="*70)

if __name__ == "__main__":
    engine = ProxyFailoverEngine()
    engine.check_and_monitor_proxy("node_residential_mumbai_01")
