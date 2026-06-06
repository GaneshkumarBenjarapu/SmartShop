// Dynamic Configuration
const API_BASE_URL = window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1'
  ? 'http://localhost:5000'
  : 'https://smartshop-web.onrender.com'; // Render backend URL

// Global state
let session = { user: null, user_name: null };
let isLoggedIn = false;

// Initialize layout on DOM load
document.addEventListener('DOMContentLoaded', async () => {
    // 1. Fetch Session from Backend API
    session = await fetchSession();
    isLoggedIn = !!session.user;

    // 2. Inject Styles and Layout
    injectStyles();
    injectLayout();

    // 3. Initialize Interactive Components
    initFilterDropdown();
    initProfileDropdown();
    if (isLoggedIn) {
        refreshSavedCount();
    }
    initChatbot();
});

async function fetchSession() {
    try {
        const res = await fetch(`${API_BASE_URL}/`, { credentials: 'include' });
        const data = await res.json();
        return data.session || {};
    } catch (err) {
        console.error("Failed to load session:", err);
        return { user: null, user_name: null };
    }
}

function injectStyles() {
    // Add Fonts and Icons
    const fontLink = document.createElement('link');
    fontLink.href = 'https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap';
    fontLink.rel = 'stylesheet';
    document.head.appendChild(fontLink);

    const faLink = document.createElement('link');
    faLink.href = 'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css';
    faLink.rel = 'stylesheet';
    document.head.appendChild(faLink);

    // CSS variables and base layouts from base.html
    const style = document.createElement('style');
    style.innerHTML = `
        body {
            margin: 0;
            padding: 0;
            background: linear-gradient(135deg, #a56df9 0%, #ffcda5 100%);
            background-attachment: fixed;
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            color: #0F1111;
        }
        a {
            text-decoration: none;
            color: #007185;
        }
        a:hover {
            color: #C7511F;
            text-decoration: underline;
        }
        .navbar {
            background-color: #131921;
            color: white;
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 10px 20px;
            height: 60px;
        }
        .nav-left {
            display: flex;
            align-items: center;
            gap: 15px;
        }
        .logo {
            font-size: 24px;
            font-weight: bold;
            color: white;
            text-decoration: none !important;
        }
        .logo span {
            color: #FF9900;
        }
        .nav-search {
            display: flex;
            flex: 1;
            margin: 0 20px;
            max-width: 600px;
            overflow: visible !important;
        }
        .filter-dropdown {
            position: relative;
            display: inline-block;
        }
        .nav-search button.filter-btn {
            background-color: #f3f4f6 !important;
            color: #333 !important;
            padding: 0 15px;
            font-size: 14px;
            border: none;
            border-right: 1px solid #ccc;
            border-radius: 4px 0 0 4px;
            cursor: pointer;
            display: flex;
            align-items: center;
            gap: 5px;
            height: 100%;
            background-image: none !important;
        }
        .dropdown-content {
            display: none;
            position: absolute;
            background-color: white;
            min-width: 400px;
            box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
            z-index: 1400;
            border-radius: 4px;
            top: 100%;
            left: 0;
            margin-top: 2px;
            padding: 15px;
            grid-template-columns: 1fr 1fr;
            gap: 20px;
        }
        .filter-dropdown.open .dropdown-content {
            display: grid;
        }
        .filter-section {
            display: flex;
            flex-direction: column;
        }
        .filter-section-title {
            font-size: 14px;
            font-weight: 700;
            margin-bottom: 8px;
            color: #111;
            border-bottom: 1px solid #eee;
            padding-bottom: 4px;
        }
        .filter-section a {
            color: #333;
            padding: 6px 0;
            text-decoration: none;
            font-size: 13px;
        }
        .filter-section a:hover {
            color: #007185;
            text-decoration: underline;
        }
        .nav-search input {
            flex: 1 1 auto;
            min-width: 0;
            padding: 10px 15px;
            border: none;
            outline: none;
            font-size: 15px;
            box-sizing: border-box;
        }
        .nav-search button.search-btn {
            background-color: #FEBD69;
            border: none;
            padding: 0 15px !important;
            width: 45px !important;
            min-width: 45px !important;
            cursor: pointer;
            color: #333;
            font-size: 16px;
            border-radius: 0 4px 4px 0;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .nav-search button.search-btn:hover {
            background-color: #F3A847;
        }
        .nav-right ul {
            list-style: none;
            display: flex;
            align-items: center;
            gap: 20px;
            margin: 0;
            padding: 0;
        }
        .nav-right a {
            color: white;
            text-decoration: none;
            font-size: 14px;
            font-weight: bold;
            display: flex;
            flex-direction: column;
        }
        .nav-right a span {
            font-size: 12px;
            font-weight: normal;
            color: #ccc;
        }
        .nav-right a:hover {
            outline: 1px solid white;
            padding: 2px;
            margin: -3px;
        }
        .profile-dropdown-content a {
            display: flex;
            align-items: center;
            gap: 10px;
            color: #333;
            padding: 8px 0;
            text-decoration: none;
            font-size: 14px;
            font-weight: 500;
        }
        .profile-dropdown-content a:hover {
            outline: none !important;
            margin: 0 !important;
            padding: 8px 0 !important;
            color: #007185;
            text-decoration: underline;
        }
        footer {
            background-color: #232F3E;
            color: white;
            text-align: center;
            padding: 30px;
            margin-top: 40px;
            font-size: 14px;
        }
        .category-bar {
            background-color: #232F3E;
            color: white;
            display: flex;
            gap: 25px;
            padding: 10px 20px;
            align-items: center;
            overflow-x: auto;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        .category-bar .category-item {
            display: flex;
            flex-direction: column;
            align-items: center;
            text-decoration: none;
            color: white;
            min-width: 70px;
            gap: 5px;
        }
        .category-bar .category-item img {
            width: 45px;
            height: 45px;
            border-radius: 50%;
            object-fit: cover;
            border: 2px solid transparent;
            background-color: white;
        }
        .category-item.active img, .category-bar .category-item:hover img {
            border-color: #FF9900;
        }
        .category-bar .category-item span {
            font-size: 12px;
            font-weight: 500;
        }
        #toast {
            visibility: hidden;
            background-color: #4CAF50;
            color: white;
            text-align: center;
            border-radius: 2px;
            padding: 16px;
            position: fixed;
            z-index: 1000;
            left: 50%;
            bottom: 30px;
            font-size: 17px;
            transform: translateX(-50%);
        }
    `;
    document.head.appendChild(style);
}

function injectLayout() {
    const isAuthPage = window.location.pathname.includes('login') || 
                       window.location.pathname.includes('register') || 
                       window.location.pathname.includes('verify_otp');

    // 1. Header Navbar
    let userSection = '';
    if (isLoggedIn) {
        userSection = `
        <div class="profile-dropdown" style="position: relative; display: inline-block;">
            <a href="/profile" style="color: white; text-decoration: none; display: flex; flex-direction: column; align-items: flex-start;">
                <span><i class="fas fa-user-circle"></i> Profile</span>
                Account
            </a>
            <div class="profile-dropdown-content" style="display: none; position: absolute; background-color: white; min-width: 250px; box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2); z-index: 1400; border-radius: 4px; top: 100%; right: -50px; margin-top: 10px; padding: 15px; color: #333; text-align: left;">
                <div style="border-bottom: 1px solid #eee; padding-bottom: 10px; margin-bottom: 10px;">
                    <div style="font-size: 16px; font-weight: bold; margin-bottom: 5px; color: #111;">${session.user_name || 'Guest User'}</div>
                    <div style="font-size: 13px; color: #444; margin-bottom: 3px; display: flex; align-items: center; gap: 8px;"><i class="fas fa-envelope" style="width: 14px; text-align: center; color: #666;"></i> ${session.user.includes('@') ? session.user : 'user@smartshop.com'}</div>
                    <div style="font-size: 13px; color: #444; margin-bottom: 3px; display: flex; align-items: center; gap: 8px;"><i class="fas fa-phone" style="width: 14px; text-align: center; color: #666;"></i> ${!session.user.includes('@') ? session.user : '+91 9876543210'}</div>
                    <div style="font-size: 13px; color: #444; display: flex; align-items: center; gap: 8px;"><i class="fas fa-map-marker-alt" style="width: 14px; text-align: center; color: #666;"></i> 123 SmartShop St, Tech City</div>
                </div>
                <a href="/orders"><i class="fas fa-box" style="width: 16px; text-align: center; color: #007185;"></i> Your Orders</a>
                <a href="#" id="logout-btn" style="color: #e11d48;"><i class="fas fa-sign-out-alt" style="width: 16px; text-align: center;"></i> Sign out</a>
            </div>
        </div>`;
    } else {
        userSection = `
        <a href="/login">
            <span><i class="fas fa-user-circle"></i> Hello, sign in</span>
            Account & Lists
        </a>`;
    }

    const navbarHtml = `
    <nav class="navbar">
        <div class="nav-left">
            <a href="/dashboard" title="Home" style="color: white; margin-right: 10px; display:flex; align-items:center;">
                <i class="fas fa-home" style="font-size:20px; color: white;"></i>
            </a>
            <a href="/" class="logo">Smart<span>Shop</span></a>
        </div>

        <div class="nav-search">
            <div class="filter-dropdown">
                <button type="button" id="filterToggle" class="filter-btn">
                    <i class="fas fa-filter"></i> <i class="fas fa-caret-down" style="font-size: 10px; margin-left: 2px;"></i>
                </button>
                <div class="dropdown-content">
                    <div>
                        <div class="filter-section">
                            <div class="filter-section-title">Brand</div>
                            <a href="/products?brand=Samsung">Samsung</a>
                            <a href="/products?brand=Apple">Apple</a>
                            <a href="/products?brand=Nike">Nike</a>
                            <a href="/products?brand=Sony">Sony</a>
                        </div>
                        <div class="filter-section" style="margin-top: 15px;">
                            <div class="filter-section-title">Discount</div>
                            <a href="/products?discount=25">25% off</a>
                            <a href="/products?discount=30">30% off</a>
                            <a href="/products?discount=40">40% off</a>
                        </div>
                    </div>
                    <div>
                        <div class="filter-section">
                            <div class="filter-section-title">Price</div>
                            <a href="/products?price=under_1000">Under ₹1000</a>
                            <a href="/products?price=1000_5000">₹1000 - ₹5000</a>
                            <a href="/products?price=over_5000">Over ₹5000</a>
                        </div>
                        <div class="filter-section" style="margin-top: 15px;">
                            <div class="filter-section-title">Rating</div>
                            <a href="/products?rating=4">4★ and above</a>
                            <a href="/products?rating=3">3★ and above</a>
                            <a href="/products?rating=2">2★ and above</a>
                        </div>
                        <div class="filter-section" style="margin-top: 15px;">
                            <div class="filter-section-title">Popularity</div>
                            <a href="/products?popularity=bestsellers">Best sellers</a>
                            <a href="/products?popularity=trending">Trending</a>
                        </div>
                    </div>
                </div>
            </div>
            <form class="search-form" action="/products" method="get" style="display:flex; flex:1; gap:0; align-items:center; margin:0; padding:0;">
                <input name="search" type="text" placeholder="Search SmartShop" style="height: 100%; border-radius: 0; padding: 10px 15px; outline: none; border: none; flex: 1;" required>
                <button type="submit" class="search-btn" style="height: 100%; border-radius: 0 4px 4px 0;"><i class="fas fa-search"></i></button>
            </form>
        </div>

        <div class="nav-right">
            <ul>
                <li>${userSection}</li>
                <li><a href="/admin"><span><i class="fas fa-user-shield"></i> Seller Central</span>Admin Panel</a></li>
                <li><a href="/dashboard"><span><i class="fas fa-undo-alt"></i> Returns</span>& Recommendations</a></li>
                <li style="margin-left: 10px;"><a href="/products">All Products</a></li>
                <li style="margin-left: 6px;">
                    <a href="/saved" style="position: relative; display: flex; align-items: center; gap: 8px;">
                        <i class="fas fa-heart" style="font-size: 22px; color: #e11d48;"></i>
                        <span id="saved-count" style="position: absolute; top: -6px; left: 14px; background-color: #e11d48; color: white; border-radius: 50%; padding: 2px 6px; font-size: 11px; font-weight: bold;">0</span>
                        <span style="color: white; font-weight: bold; font-size: 16px; margin-left: 10px;">Wishlist</span>
                    </a>
                </li>
            </ul>
        </div>
    </nav>`;

    document.body.insertAdjacentHTML('afterbegin', navbarHtml);

    // Bind logout button handler
    const logoutBtn = document.getElementById('logout-btn');
    if (logoutBtn) {
        logoutBtn.addEventListener('click', async (e) => {
            e.preventDefault();
            await fetch(`${API_BASE_URL}/logout`, { credentials: 'include' });
            window.location.href = '/';
        });
    }

    // 2. Category Navigation Bar (skip on auth/checkout pages)
    if (!isAuthPage && !window.location.pathname.includes('checkout')) {
        const activeCat = new URLSearchParams(window.location.search).get('category') || '';
        const categoryBarHtml = `
        <div class="category-bar" style="justify-content: center; gap: 30px;">
            <a href="/quiz" class="category-item" style="color: #FF9900; transform: scale(1.05);">
                <i class="fas fa-magic" style="font-size: 36px; margin-bottom: 8px; text-shadow: 0 0 10px rgba(255,153,0,0.5);"></i>
                <span style="font-weight: bold;">Take Quiz</span>
            </a>
            <a href="/mood" class="category-item" style="color: #63b3ed; transform: scale(1.05);">
                <i class="fas fa-smile-beam" style="font-size: 36px; margin-bottom: 8px; text-shadow: 0 0 10px rgba(99,179,237,0.5);"></i>
                <span style="font-weight: bold;">Vibe Check</span>
            </a>
            <div style="width: 1px; height: 40px; background: rgba(255,255,255,0.2); margin: 0 5px;"></div>
            <a href="/products?category=Electronics" class="category-item ${activeCat === 'Electronics' ? 'active' : ''}">
                <i class="fas fa-laptop" style="font-size: 36px; margin-bottom: 8px;"></i>
                <span>Electronics</span>
            </a>
            <a href="/products?category=Books" class="category-item ${activeCat === 'Books' ? 'active' : ''}">
                <i class="fas fa-book" style="font-size: 36px; margin-bottom: 8px;"></i>
                <span>Books</span>
            </a>
            <a href="/products?category=Home Appliances" class="category-item ${activeCat === 'Home Appliances' ? 'active' : ''}">
                <i class="fas fa-blender" style="font-size: 36px; margin-bottom: 8px;"></i>
                <span>Appliances</span>
            </a>
            <a href="/products?category=Beauty" class="category-item ${activeCat === 'Beauty' ? 'active' : ''}">
                <i class="fas fa-spa" style="font-size: 36px; margin-bottom: 8px;"></i>
                <span>Beauty</span>
            </a>
            <a href="/products?category=Women Fashion" class="category-item ${activeCat === 'Women Fashion' ? 'active' : ''}">
                <i class="fas fa-female" style="font-size: 36px; margin-bottom: 8px;"></i>
                <span>Women</span>
            </a>
            <a href="/products?category=Men Fashion" class="category-item ${activeCat === 'Men Fashion' ? 'active' : ''}">
                <i class="fas fa-user-tie" style="font-size: 36px; margin-bottom: 8px;"></i>
                <span>Men</span>
            </a>
            <a href="/products?category=Kidsware" class="category-item ${activeCat === 'Kidsware' ? 'active' : ''}">
                <i class="fas fa-baby" style="font-size: 36px; margin-bottom: 8px;"></i>
                <span>Kidsware</span>
            </a>
            <a href="/products?category=Toys" class="category-item ${activeCat === 'Toys' ? 'active' : ''}">
                <i class="fas fa-gamepad" style="font-size: 36px; margin-bottom: 8px;"></i>
                <span>Toys</span>
            </a>
            <a href="/products?category=Shoes" class="category-item ${activeCat === 'Shoes' ? 'active' : ''}">
                <i class="fas fa-shoe-prints" style="font-size: 36px; margin-bottom: 8px;"></i>
                <span>Shoes</span>
            </a>
        </div>`;
        document.body.querySelector('.navbar').insertAdjacentHTML('afterend', categoryBarHtml);
    }

    // 3. Inject Toast
    const toastHtml = `<div id="toast"><i class="fas fa-check-circle"></i> Item added successfully!</div>`;
    document.body.insertAdjacentHTML('beforeend', toastHtml);

    // 4. Inject Footer
    const footerHtml = `<footer><p>© 2026 SmartShop | Powered by Group-3</p></footer>`;
    document.body.insertAdjacentHTML('beforeend', footerHtml);
}

function initFilterDropdown() {
    const toggle = document.getElementById('filterToggle');
    if (!toggle) return;
    const dropdown = toggle.closest('.filter-dropdown');

    toggle.addEventListener('click', (ev) => {
        ev.stopPropagation();
        dropdown.classList.toggle('open');
    });

    document.addEventListener('click', () => {
        dropdown.classList.remove('open');
    });

    const content = dropdown.querySelector('.dropdown-content');
    if (content) {
        content.addEventListener('click', (ev) => ev.stopPropagation());
    }
}

function initProfileDropdown() {
    const dropdown = document.querySelector('.profile-dropdown');
    if (!dropdown) return;
    const content = dropdown.querySelector('.profile-dropdown-content');

    dropdown.addEventListener('mouseenter', () => {
        content.style.display = 'block';
    });
    dropdown.addEventListener('mouseleave', () => {
        content.style.display = 'none';
    });
}

// Wishlist methods
async function refreshSavedCount() {
    try {
        const res = await fetch(`${API_BASE_URL}/api/saved/count`, { credentials: 'include' });
        const data = await res.json();
        const sc = document.getElementById('saved-count');
        if (sc) sc.innerText = data.saved_count || 0;
    } catch (err) {
        console.error('Failed to fetch wishlist count', err);
    }
}

async function addToCart(productId, collection = 'Favorites') {
    if (!productId) return;
    if (!isLoggedIn) {
        showToast('Please sign in to save products to your wishlist.');
        setTimeout(() => { window.location.href = '/login'; }, 1500);
        return;
    }
    try {
        const res = await fetch(`${API_BASE_URL}/api/saved/add`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ product_id: productId, collection: collection }),
            credentials: 'include'
        });
        const data = await res.json();
        if (data && data.saved_count !== undefined) {
            const sc = document.getElementById('saved-count');
            if (sc) sc.innerText = data.saved_count;
            showToast('Product added to your wishlist successfully!');
        }
    } catch (err) {
        console.error('Failed to save product', err);
    }
}

async function deleteFromWishlist(productId) {
    try {
        const res = await fetch(`${API_BASE_URL}/api/saved/delete`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ product_id: productId }),
            credentials: 'include'
        });
        const data = await res.json();
        if (data && data.saved_count !== undefined) {
            const sc = document.getElementById('saved-count');
            if (sc) sc.innerText = data.saved_count;
        }
        location.reload();
    } catch (err) {
        console.error(err);
    }
}

function showToast(msg) {
    const toast = document.getElementById("toast");
    if (!toast) return;
    toast.innerHTML = `<i class="fas fa-check-circle"></i> ${msg || 'Product saved to wishlist!'}`;
    toast.style.visibility = "visible";
    setTimeout(() => { toast.style.visibility = "hidden"; }, 3000);
}

// Inject Chatbot interface and load script dynamically
function initChatbot() {
    const chatbotHtml = `
    <!-- Chatbot trigger button -->
    <div id="chatbot-trigger" onclick="toggleChat()">
        <i class="fas fa-comment-dots"></i>
    </div>
    
    <!-- Chatbot Window -->
    <div id="chatbot-window">
        <div id="chatbot-header">
            <div style="display:flex; align-items:center; gap:10px;">
                <div class="bot-avatar">🤖</div>
                <div>
                    <div style="font-weight:bold; font-size:14px;">SmartShop AI Assistant</div>
                    <div style="font-size:11px; opacity:0.8;">Online | Personalized Shopping</div>
                </div>
            </div>
            <i class="fas fa-times close-btn" onclick="toggleChat()" style="cursor:pointer;"></i>
        </div>
        <div id="chatbot-messages">
            <div class="message bot-message">
                Hello! I am your SmartShop AI shopping assistant. How can I help you today?
            </div>
        </div>
        <div id="chatbot-input-area">
            <input type="text" id="chatbot-input" placeholder="Type a message..." onkeypress="handleChatKeypress(event)">
            <button onclick="sendChatMessage()"><i class="fas fa-paper-plane"></i></button>
        </div>
    </div>`;

    document.body.insertAdjacentHTML('beforeend', chatbotHtml);

    // Dynamically load chatbot stylesheet and script
    const botLink = document.createElement('link');
    botLink.href = '/static/chatbot.css';
    botLink.rel = 'stylesheet';
    document.head.appendChild(botLink);
}

// Global Chatbot UI functions
window.toggleChat = function() {
    const chatWindow = document.getElementById('chatbot-window');
    if (!chatWindow) return;
    chatWindow.classList.toggle('active');
};

window.sendChatMessage = async function() {
    const input = document.getElementById('chatbot-input');
    const msg = input.value.trim();
    if (!msg) return;

    appendMessage(msg, 'user-message');
    input.value = '';

    try {
        const response = await fetch(`${API_BASE_URL}/api/chat`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ message: msg }),
            credentials: 'include'
        });
        const data = await response.json();
        appendMessage(data.reply, 'bot-message');
    } catch (err) {
        console.error(err);
        appendMessage("Sorry, I'm having trouble connecting right now.", 'bot-message');
    }
};

window.handleChatKeypress = function(e) {
    if (e.key === 'Enter') {
        sendChatMessage();
    }
};

function appendMessage(text, className) {
    const chatMessages = document.getElementById('chatbot-messages');
    if (!chatMessages) return;
    const msgDiv = document.createElement('div');
    msgDiv.className = `message ${className}`;
    msgDiv.innerHTML = text;
    chatMessages.appendChild(msgDiv);
    chatMessages.scrollTop = chatMessages.scrollHeight;
}
