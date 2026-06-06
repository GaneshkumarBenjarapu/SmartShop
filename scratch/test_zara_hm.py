import sys
import os

# Add project root to sys.path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from backend.db import get_db_connection

def test_db_entries():
    conn = get_db_connection()
    row1 = conn.execute("SELECT * FROM products WHERE id = 130").fetchone()
    row2 = conn.execute("SELECT * FROM products WHERE id = 132").fetchone()
    conn.close()
    
    success = True
    
    if not row1:
        print("[ERROR] Zara Handloom Saree 89 not found in database!")
        success = False
    else:
        print(f"Zara Product Info: ID={row1['id']}, Name='{row1['name']}', Image='{row1['image']}'")
        if row1['image'] == "/static/zara_handloom_saree_89.png":
            print("[SUCCESS] Zara Handloom Saree 89 image is correctly set in Database!")
        else:
            print("[ERROR] Zara Handloom Saree 89 image mismatch in Database!")
            success = False
            
    if not row2:
        print("[ERROR] H&M Handloom Saree 33 not found in database!")
        success = False
    else:
        print(f"H&M Product Info: ID={row2['id']}, Name='{row2['name']}', Image='{row2['image']}'")
        if row2['image'] == "/static/hm_handloom_saree_33.png":
            print("[SUCCESS] H&M Handloom Saree 33 image is correctly set in Database!")
        else:
            print("[ERROR] H&M Handloom Saree 33 image mismatch in Database!")
            success = False
            
    return success

if __name__ == "__main__":
    if test_db_entries():
        print("\nTESTS PASSED SUCCESSFULLY!")
    else:
        print("\nTESTS FAILED!")
