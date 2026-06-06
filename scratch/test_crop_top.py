import sys
import os

# Add project root to sys.path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from backend.db import get_db_connection

def test_db_entry():
    conn = get_db_connection()
    row = conn.execute("SELECT * FROM products WHERE id = 57").fetchone()
    conn.close()
    
    if not row:
        print("[ERROR] H&M Casual Crop Top not found in database!")
        return False
        
    print(f"H&M Product Info: ID={row['id']}, Name='{row['name']}', Image='{row['image']}'")
    if row['image'] == "/static/hm_casual_crop_top.png":
        print("[SUCCESS] H&M Casual Crop Top image is correctly set in Database!")
        return True
    else:
        print("[ERROR] H&M Casual Crop Top image mismatch in Database!")
        return False

if __name__ == "__main__":
    if test_db_entry():
        print("\nTEST PASSED SUCCESSFULLY!")
    else:
        print("\nTEST FAILED!")
