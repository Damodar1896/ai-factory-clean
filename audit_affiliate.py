import json, os

log_file = "affiliate_swarm_execution.json"
if os.path.exists(log_file):
    with open(log_file, "r") as f:
        data = json.load(f)
    print("=== [DAMODAR AFFILIATE EMPIRE LIVE AUDIT] ===")
    print(f"Total Registered Partnerships : {data.get("total_registered", 0)}")
    partnerships = data.get("partnerships", [])
    if partnerships:
        print("\nLast 5 Secure Partnerships Locked:")
        for idx, p in enumerate(partnerships[-5:], 1):
            print(f"  {idx}. Network: {p.get("network_name")} | Email Used: {p.get("corporate_email")} | Status: {p.get("status")}")
    else:
        print("\n[INFO] Daemon is in pacing mode. Waiting for next organic jitter window to execute.")
else:
    print("[INFO] Execution log pending creation as daemon paces its first cycle.")
print("=============================================")
