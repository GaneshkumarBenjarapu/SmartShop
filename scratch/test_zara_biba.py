import sys
import os

# Add project root to sys.path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from backend.db import get_db_connection

def test_db_entries():
    conn = get_db_connection()
    row1 = conn.execute("SELECT * FROM products WHERE id = 131").fetchone()
    row2 = conn.execute("SELECT * FROM products WHERE id = 138").fetchone()
    conn.close()
    
    success = True
    
    if not row1:
        print("[ERROR] Zara Floral Dress 51 not found in database!")
        success = False
    else:
        print(f"Zara Product Info: ID={row1['id']}, Name='{row1['name']}', Image='{row1['image']}'")
        if row1['image'] == "/static/zara_floral_dress_51.png":
            print("[SUCCESS] Zara Floral Dress 51 image is correctly set in Database!")
        else:
            print("[ERROR] Zara Floral Dress 51 image mismatch in Database!")
            success = False
            
    if not row2:
        print("[ERROR] Biba Handloom Saree 48 not found in database!")
        success = False
    else:
        print(f"Biba Product Info: ID={row2['id']}, Name='{row2['name']}', Image='{row2['image']}'")
        if row2['image'] == "https://images.unsplash.com/photo-1610030469983-98e550d6193c?q=80&w=1000&auto=format&fit=crop":
            print("[SUCCESS] Biba Handloom Saree 48 image is correctly set in Database!")
        else:
            print("[ERROR] Biba Handloom Saree 48 image mismatch in Database!")
            success = False
            
    return success

if __name__ == "__main__":
    if test_db_entries():
        print("\nTESTS PASSED SUCCESSFULLY!")
    else:
        print("\nTESTS FAILED!")
