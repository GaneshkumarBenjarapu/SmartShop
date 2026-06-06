import sys
import os

# Add project root to sys.path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from backend.db import get_db_connection

def test_loreal_lipstick():
    print("Testing L'Oreal Red Velvet Lipstick Product...")
    conn = get_db_connection()
    row = conn.execute("SELECT * FROM products WHERE id = 9033").fetchone()
    conn.close()
    
    if not row:
        print("[ERROR] L'Oreal Red Velvet Lipstick not found in database!")
        return False
        
    print(f"Database Product Info: ID={row['id']}, Name='{row['name']}', Image='{row['image']}'")
    if row['image'] == "/static/loreal_red_velvet_lipstick.png":
        print("[SUCCESS] L'Oreal Red Velvet Lipstick image is correctly set to /static/loreal_red_velvet_lipstick.png in Database!")
        return True
    else:
        print("[ERROR] L'Oreal Red Velvet Lipstick image mismatch in Database!")
        return False

if __name__ == "__main__":
    if test_loreal_lipstick():
        print("\nTEST PASSED SUCCESSFULLY!")
    else:
        print("\nTEST FAILED!")
