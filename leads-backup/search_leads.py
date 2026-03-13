#!/usr/bin/env python3
import sqlite3
import sys

db_path = "/home/chris/daily-reports/leads-backup/leads_consolidated.db"

def search(query_type, value, limit=10):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    if query_type == "city":
        cursor.execute("SELECT * FROM leads WHERE city LIKE ? LIMIT ?", (f"%{value}%", limit))
    elif query_type == "email":
        cursor.execute("SELECT * FROM leads WHERE email LIKE ? LIMIT ?", (f"%{value}%", limit))
    elif query_type == "category":
        cursor.execute("SELECT * FROM leads WHERE category LIKE ? LIMIT ?", (f"%{value}%", limit))
    elif query_type == "state":
        cursor.execute("SELECT * FROM leads WHERE state = ? LIMIT ?", (value, limit))
    elif query_type == "company":
        cursor.execute("SELECT * FROM leads WHERE company_name LIKE ? LIMIT ?", (f"%{value}%", limit))
    else:
        print("Unknown type. Use: city, email, category, state, company")
        return
    
    results = cursor.fetchall()
    conn.close()
    
    print(f"Found {len(results)} leads:")
    for r in results:
        print(f"  {r[1]} | {r[2]} | {r[5]}")  # company | email | city

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 search_leads.py <type> <value>")
        print("Types: city, email, category, state, company")
        sys.exit(1)
    
    query_type = sys.argv[1]
    value = sys.argv[2]
    limit = int(sys.argv[3]) if len(sys.argv) > 3 else 10
    search(query_type, value, limit)
