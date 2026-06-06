import sys
import os

# Add project root to sys.path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from backend.db import get_db_connection

def test_boat():
    print("Testing Boat Rockerz 450 Products...")
    conn = get_db_connection()
    rows = conn.execute("SELECT * FROM products WHERE name LIKE '%Rockerz%'").fetchall()
    conn.close()
    
    if not rows:
        print("[ERROR] Boat Rockerz products not found in database!")
        return False
        
    all_ok = True
    for row in rows:
        print(f"Database Product Info: ID={row['id']}, Name='{row['name']}', Image='{row['image']}'")
        if row['image'] == "/static/boat_rockerz_450_headphones.png":
            print(f"[SUCCESS] Boat ID {row['id']} image is correctly set in Database!")
        else:
            print(f"[ERROR] Boat ID {row['id']} image mismatch in Database!")
            all_ok = False
    return all_ok

if __name__ == "__main__":
    if test_boat():
        print("\nTEST PASSED SUCCESSFULLY!")
    else:
        print("\nTEST FAILED!")
