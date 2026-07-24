import sqlite3

def show_stored_leads():
    conn = sqlite3.connect("saas_database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, client_name, email, message FROM leads")
    rows = cursor.fetchall()
    
    print("============================================================")
    print("         📋 STORED LEADS & EMAILS DATABASE 📋             ")
    print("============================================================")
    if not rows:
        print(" [Notice] No leads found in database yet.")
    else:
        for row in rows:
            print(f" ID: {row[0]} | Name: {row[1]} | Email: {row[2]}")
            print(f" Message: {row[3]}")
            print("-" * 50)
    conn.close()

if __name__ == "__main__":
    show_stored_leads()
