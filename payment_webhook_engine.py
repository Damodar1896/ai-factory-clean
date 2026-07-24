import time

def simulate_payment_webhook_listener(transaction_id, client_email, amount):
    print(f"\n[Payment Webhook] Incoming transaction detected! ID: {transaction_id} | Amount: ₹{amount} | From: {client_email}")
    print("[Webhook Engine] Verifying UPI signature & bank confirmation...")
    time.sleep(1)
    print(f"[SUCCESS] Payment verified! Automatically dispatching secure database download link to {client_email}")

if __name__ == "__main__":
    simulate_payment_webhook_listener("UPI_TXN_987654321", "client@targetbusiness.com", 1999)
