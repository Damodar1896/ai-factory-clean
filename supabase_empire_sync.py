import os, json, time, urllib.request

SUPABASE_URL = os.getenv("SUPABASE_URL", "https://zhdrghjygatcqsyjmvdl.supabase.co")
SUPABASE_KEY = os.getenv("SUPABASE_KEY", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InpoZHJnaGp5Z2F0Y3FzeWptdmRsIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc4NTA0MTU2MiwiZXhwIjoyMTAwNjE3NTYyfQ.siqScmP8G0RVCMLw_bOtxe8fRAEc5V_TgZZuIkHUD9s")

def sync_file_to_supabase(table_name, file_path):
    if SUPABASE_URL == "https://your-project.supabase.co":
        print(f"[☁️ SUPABASE MOCK SYNC]: Skipping cloud push for {table_name} (Credentials pending)...", flush=True)
        return
        
    if not os.path.exists(file_path):
        return
        
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            
        # Push payload to Supabase REST endpoint
        url = f"{SUPABASE_URL}/rest/v1/{table_name}"
        payload = json.dumps({"payload": data, "updated_at": "now()"}).encode("utf-8")
        
        req = urllib.request.Request(url, data=payload, method="POST")
        req.add_header("apikey", SUPABASE_KEY)
        req.add_header("Authorization", f"Bearer {SUPABASE_KEY}")
        req.add_header("Content-Type", "application/json")
        req.add_header("Prefer", "resolution=merge-duplicates")
        
        urllib.request.urlopen(req, timeout=15)
        print(f"[☁️ SUPABASE CLOUD SYNC] Successfully synced [{file_path}] to table [{table_name}]!", flush=True)
    except Exception as e:
        print(f"[⚠️ SUPABASE SYNC ERROR for {table_name}]: {e}", flush=True)

def run_cloud_sync_daemon():
    print("=== [DAMODAR SUPABASE CLOUD SYNC DAEMON STARTED] ===", flush=True)
    while True:
        try:
            sync_file_to_supabase("email_vault", "persistent_email_vault.json")
            sync_file_to_supabase("affiliate_partnerships", "affiliate_swarm_execution.json")
            sync_file_to_supabase("outreach_history", "outreach_sent_history.json")
            
            # Sync every 30 minutes
            time.sleep(1800)
        except Exception as err:
            print(f"[⚠️ CLOUD SYNC EXCEPTION]: {err}", flush=True)
            time.sleep(60)

if __name__ == "__main__":
    run_cloud_sync_daemon()
