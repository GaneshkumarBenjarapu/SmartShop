import sqlite3
import os

db_path = os.path.join('data', 'shop.db')
if os.path.exists(db_path):
    conn = sqlite3.connect(db_path)
    # Double single quote to escape it in SQL
    conn.execute("UPDATE products SET name = 'Symbol Men''s Regular Fit Polo T-Shirt' WHERE id = 60")
    conn.commit()
    print("Database updated. Changes:", conn.total_changes)
    conn.close()
else:
    print("shop.db not found.")
