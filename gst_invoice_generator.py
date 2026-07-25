import json
from datetime import datetime

def generate_gst_invoice(client_name, amount, upi_ref):
    try:
        invoice = {
            "invoice_no": f"DTV-2026-{int(datetime.now().timestamp())}",
            "date": datetime.now().strftime("%Y-%m-%d"),
            "client": client_name,
            "amount_inr": amount,
            "gst_rate": "18% Inclusive",
            "payment_mode": "UPI (damodartechcraze@okaxis)",
            "upi_ref": upi_ref,
            "status": "PAID & VERIFIED",
            "seller": "Damodar Tech Craze Ventures"
        }
        filename = f"invoice_{client_name.lower().replace(' ', '_')}.json"
        with open(filename, "w") as f:
            json.dump(invoice, f, indent=4)
        print(f"[✅ SUCCESS] GST Invoice successfully compiled and saved: {filename}")
        return True
    except Exception as e:
        print(f"[!] Error generating invoice: {e}")
        return False

if __name__ == "__main__":
    print("=== [SETTING UP MODULE 2: GST INVOICE GENERATOR] ===")
    generate_gst_invoice("Rahul Sharma", 1999, "UPI_REF_987654321")
