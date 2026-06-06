import sys
import os

# Add project root to sys.path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from backend.db import get_db_connection

def test_biba():
    print("Testing Biba Ethnic Kurta Product...")
    conn = get_db_connection()
    row = conn.execute("SELECT * FROM products WHERE id = 58").fetchone()
    conn.close()
    
    if not row:
        print("[ERROR] Biba Ethnic Kurta product not found in database!")
        return False
        
    print(f"Database Product Info: ID={row['id']}, Name='{row['name']}', Image='{row['image']}'")
    if row['image'] == "/static/biba_ethnic_kurta_set.png":
        print(f"[SUCCESS] Biba ID {row['id']} image is correctly set in Database!")
        return True
    else:
        print(f"[ERROR] Biba ID {row['id']} image mismatch in Database!")
        return False

if __name__ == "__main__":
    if test_biba():
        print("\nTEST PASSED SUCCESSFULLY!")
    else:
        print("\nTEST FAILED!")
