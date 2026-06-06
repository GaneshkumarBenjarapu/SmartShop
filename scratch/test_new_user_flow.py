import sys
import os

# Add project root to sys.path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from backend.app import app
from backend.db import get_db_connection

def test_ruby_woo():
    print("Testing Ruby Woo Product...")
    conn = get_db_connection()
    row = conn.execute("SELECT * FROM products WHERE id = 193").fetchone()
    conn.close()
    
    if not row:
        print("[ERROR] Ruby Woo product not found in database!")
        return False
        
    print(f"Database Product Info: ID={row['id']}, Name='{row['name']}', Image='{row['image']}'")
    if row['image'] == "/static/mac_ruby_woo_lipstick.png":
        print("[SUCCESS] Ruby Woo image is correctly set to /static/mac_ruby_woo_lipstick.png in Database!")
        return True
    else:
        print("[ERROR] Ruby Woo image mismatch in Database!")
        return False

def test_new_user_popup():
    print("\nTesting New User Verification & Popup Flow...")
    client = app.test_client()
    
    # 1. Clean test user if exists
    test_email = "tester_new_user@smartshop.com"
    conn = get_db_connection()
    conn.execute("DELETE FROM users WHERE email = ?", (test_email,))
    conn.commit()
    conn.close()
    
    # 2. Mock pending OTP in session
    with client.session_transaction() as sess:
        import time
        sess['pending_otp'] = {
            'code': '123456',
            'recipient': test_email,
            'expires': int(time.time()) + 120,
            'resend_count': 0
        }
    
    # 3. Post OTP code to verify
    response = client.post('/verify_otp', data={'otp_code': '123456'}, follow_redirects=True)
    
    # 4. Check if redirected to index/home and has show_new_user_modal in template context
    print(f"Status Code after verification: {response.status_code}")
    html = response.data.decode('utf-8')
    
    # The modal overlay should be rendered in the HTML!
    if "new-user-quiz-modal" in html:
        print("[SUCCESS] Personalization modal successfully rendered for the new user!")
    else:
        print("[ERROR] Personalization modal not found in verified new user HTML!")
        return False
        
    # Check that a second load does NOT have the modal (since session flag is popped)
    response_second = client.get('/', follow_redirects=True)
    html_second = response_second.data.decode('utf-8')
    if "new-user-quiz-modal" not in html_second:
        print("[SUCCESS] Personalization modal is NOT rendered on subsequent page loads!")
    else:
        print("[ERROR] Personalization modal is incorrectly rendered a second time!")
        return False

    return True

if __name__ == "__main__":
    success = True
    try:
        if not test_ruby_woo():
            success = False
        if not test_new_user_popup():
            success = False
            
        if success:
            print("\nALL TESTS PASSED SUCCESSFULLY!")
        else:
            print("\nSOME TESTS FAILED. PLEASE CHECK LOGS.")
    except Exception as e:
        print(f"Exception during testing: {e}")
