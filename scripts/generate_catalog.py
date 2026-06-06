import json
import random

initial_products = [
    {
        "id": 1, 
        "name": "Sony WH-1000XM4", 
        "price": 24999, 
        "description": "Premium over-ear headphones with 30hr battery life and immersive sound quality.",
        "category": "Electronics",
        "rating": 4.8,
        "image": "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?q=80&w=1000&auto=format&fit=crop",
        "badge_class": "badge-blue",
        "badge_icon": "fa-info-circle",
        "badge_text": "You previously viewed Sony WH-1000XM4"
    },
    {
        "id": 2, 
        "name": "Apple Watch Series 9", 
        "price": 41900, 
        "description": "Keep track of your fitness and notifications with this sleek, modern smartwatch.",
        "category": "Electronics",
        "rating": 4.5,
        "image": "https://images.unsplash.com/photo-1546868871-7041f2a55e12?q=80&w=1000&auto=format&fit=crop",
        "badge_class": "badge-green",
        "badge_icon": "fa-users",
        "badge_text": "Popular among users who buy Electronics"
    },
    {
        "id": 4, 
        "name": "The Great Gatsby by F. Scott Fitzgerald", 
        "price": 450, 
        "description": "A classic novel exploring themes of decadence and idealism.",
        "category": "Books",
        "rating": 2.5,
        "image": "https://covers.openlibrary.org/b/isbn/9780141182636-L.jpg",
        "badge_class": "",
        "badge_icon": "",
        "badge_text": ""
    },
    {
        "id": 5, 
        "name": "Samsung Smart Microwave", 
        "price": 8500, 
        "description": "Voice-controlled microwave for all your smart home appliance needs.",
        "category": "Home Appliances",
        "rating": 3.8,
        "image": "https://images.unsplash.com/photo-1574269909862-7e1d70bb8078?q=80&w=1000&auto=format&fit=crop",
        "badge_class": "",
        "badge_icon": "",
        "badge_text": ""
    },
    
    {
        "id": 7, "name": "Apple iPad 10th Gen", "price": 39900, "description": "Powerful iPad for work and play.", "category": "Electronics", "rating": 4.7, "image": "https://images.unsplash.com/photo-1544244015-0df4b3ffc6b0?q=80&w=1000&auto=format&fit=crop", "badge_class": "", "badge_icon": "", "badge_text": ""
    },
    {
        "id": 8, "name": "Dell Inspiron Laptop", "price": 45000, "description": "Reliable laptop for daily use.", "category": "Electronics", "rating": 4.1, "image": "https://images.unsplash.com/photo-1496181133206-80ce9b88a853?q=80&w=1000&auto=format&fit=crop", "badge_class": "", "badge_icon": "", "badge_text": ""
    },
    {
        "id": 11, "name": "The Alchemist", "price": 299, "description": "A novel by Paulo Coelho.", "category": "Books", "rating": 4.8, "image": "https://covers.openlibrary.org/b/isbn/9780062315007-L.jpg", "badge_class": "", "badge_icon": "", "badge_text": ""
    },
    {
        "id": 12, "name": "Atomic Habits", "price": 499, "description": "Tiny changes, remarkable results.", "category": "Books", "rating": 4.9, "image": "https://covers.openlibrary.org/b/isbn/9780735211292-L.jpg", "badge_class": "", "badge_icon": "", "badge_text": ""
    },
    {
        "id": 13, "name": "Rich Dad Poor Dad", "price": 399, "description": "What the rich teach their kids about money.", "category": "Books", "rating": 4.7, "image": "https://covers.openlibrary.org/b/isbn/9781612681139-L.jpg", "badge_class": "", "badge_icon": "", "badge_text": ""
    },
    {
        "id": 14, "name": "Philips Air Fryer", "price": 7500, "description": "Healthy frying with Rapid Air technology.", "category": "Home Appliances", "rating": 4.4, "image": "/static/philips_air_fryer.png", "badge_class": "", "badge_icon": "", "badge_text": ""
    },
    {
        "id": 15, "name": "LG Washing Machine", "price": 28000, "description": "Front load washing machine.", "category": "Home Appliances", "rating": 4.6, "image": "https://images.unsplash.com/photo-1610557892470-55d9e80c0bce?q=80&w=1000&auto=format&fit=crop", "badge_class": "", "badge_icon": "", "badge_text": ""
    },
    {
        "id": 16, "name": "Prestige Induction Cooktop", "price": 2500, "description": "Efficient and safe cooking.", "category": "Home Appliances", "rating": 4.2, "image": "/static/mock_induction_cooktop.png", "badge_class": "", "badge_icon": "", "badge_text": ""
    },
    {
        "id": 17, "name": "Apple iPhone 15", "price": 79900, "description": "Dynamic Island, 48MP camera.", "category": "Electronics", "rating": 4.8, "popularity": True, "image": "https://images.unsplash.com/photo-1510557880182-3d4d3cba35a5?q=80&w=1000&auto=format&fit=crop", "badge_class": "", "badge_icon": "", "badge_text": ""
    },
    {
        "id": 18, "name": "Apple AirPods Pro", "price": 24900, "description": "Active noise cancellation.", "category": "Electronics", "rating": 4.7, "image": "https://images.unsplash.com/photo-1600294037681-c80b4cb5b434?q=80&w=1000&auto=format&fit=crop", "badge_class": "", "badge_icon": "", "badge_text": ""
    },
    {
        "id": 19, "name": "Samsung Galaxy S23", "price": 64900, "description": "Epic camera, epic performance.", "category": "Electronics", "rating": 4.6, "image": "https://images.unsplash.com/photo-1610945415295-d9bbf067e59c?q=80&w=1000&auto=format&fit=crop", "badge_class": "", "badge_icon": "", "badge_text": ""
    },
    {
        "id": 20, "name": "Samsung 55\" Smart TV", "price": 45000, "description": "Crystal 4K UHD Ultra HD Smart LED TV.", "category": "Electronics", "rating": 4.5, "image": "https://images.unsplash.com/photo-1593305841991-05c297ba4575?q=80&w=1000&auto=format&fit=crop", "badge_class": "", "badge_icon": "", "badge_text": ""
    },
    {
        "id": 23, "name": "Kindle Paperwhite", "price": 13999, "description": "Now with a 6.8\" display and thinner borders.", "category": "Electronics", "rating": 4.8, "image": "https://images.unsplash.com/photo-1596524430615-b46475ddff6e?q=80&w=1000&auto=format&fit=crop", "badge_class": "", "badge_icon": "", "badge_text": ""
    },
    {
        "id": 24, "name": "Logitech MX Master 3 Mouse", "price": 8500, "description": "Advanced wireless mouse.", "category": "Electronics", "rating": 4.7, "image": "https://images.unsplash.com/photo-1527864550417-7fd91fc51a46?q=80&w=1000&auto=format&fit=crop", "badge_class": "", "badge_icon": "", "badge_text": ""
    },
    {
        "id": 25, "name": "Samsung Galaxy Watch 6", "price": 28000, "description": "The smartwatch that knows you best.", "category": "Electronics", "rating": 4.5, "popularity": True, "image": "https://images.unsplash.com/photo-1579586337278-3befd40fd17a?q=80&w=1000&auto=format&fit=crop", "badge_class": "", "badge_icon": "", "badge_text": ""
    },
    {
        "id": 26, "name": "Boat Rockerz 450 Headphones", "price": 1200, "description": "Wireless Bluetooth headphones.", "category": "Electronics", "rating": 4.1, "popularity": True, "image": "https://images.unsplash.com/photo-1618366712010-f4ae9c647dcb?q=80&w=1000&auto=format&fit=crop", "badge_class": "", "badge_icon": "", "badge_text": ""
    },
    
    {
        "id": 42, "name": "Nike Air Zoom Pro", "price": 6500, "description": "Professional running and athletic shoes.", "category": "Shoes", "rating": 4.7, "image": "https://images.unsplash.com/photo-1542291026-7eec264c27ff?q=80&w=1000&auto=format&fit=crop", "badge_class": "", "badge_icon": "", "badge_text": ""
    },
    { "id": 43, "name": "Adidas Ultraboost Shoes", "price": 15000, "description": "Premium running shoes.", "category": "Shoes", "rating": 4.8, "image": "https://images.unsplash.com/photo-1571008887538-b36bb32f4571?q=80&w=1000&auto=format&fit=crop" },
    { "id": 44, "name": "Puma Softride Sneakers", "price": 4500, "description": "Comfortable casual sneakers.", "category": "Shoes", "rating": 4.3, "image": "https://images.unsplash.com/photo-1487956382158-bb926046304a?q=80&w=1000&auto=format&fit=crop" },
    { "id": 45, "name": "Red Tape Men's Walking Shoes", "price": 2500, "description": "Comfortable and durable walking shoes.", "category": "Shoes", "rating": 4.1, "image": "https://images.unsplash.com/photo-1624028409599-ba168bfd6586?q=80&w=1000&auto=format&fit=crop" },
    { "id": 46, "name": "Skechers Go Walk Shoes", "price": 5500, "description": "Slip-on walking shoes for ultimate comfort.", "category": "Shoes", "rating": 4.6, "image": "https://images.unsplash.com/photo-1624028409583-eac582b51895?q=80&w=1000&auto=format&fit=crop" },
    
    { "id": 47, "name": "Samsung Smart Refrigerator", "price": 85000, "description": "Double door frost free smart fridge.", "category": "Home Appliances", "rating": 4.5, "image": "/static/samsung_smart_refrigerator.png" },
    { "id": 48, "name": "Samsung Galaxy Tablet", "price": 32000, "description": "High performance android tablet.", "category": "Electronics", "rating": 4.4, "image": "https://images.unsplash.com/photo-1589739900266-43b2843f4c12?q=80&w=1000&auto=format&fit=crop" },
    { "id": 49, "name": "Apple MacBook Pro", "price": 199900, "description": "Powerful laptop for creators.", "category": "Electronics", "rating": 4.9, "image": "https://images.unsplash.com/photo-1517336714731-489689fd1ca8?q=80&w=1000&auto=format&fit=crop" },
    { "id": 50, "name": "Sony Walkman Player", "price": 18000, "description": "High-Res audio portable player.", "category": "Electronics", "rating": 4.7, "image": "https://images.unsplash.com/photo-1611078489935-0cb964de46d6?q=80&w=1000&auto=format&fit=crop" },
    { "id": 51, "name": "LG Smart TV OLED", "price": 145000, "description": "Incredible picture quality with OLED.", "category": "Home Appliances", "rating": 4.8, "image": "https://images.unsplash.com/photo-1593305841991-05c297ba4575?q=80&w=1000&auto=format&fit=crop" },
    { "id": 52, "name": "Blue Star Inverter AC", "price": 42000, "description": "1.5 Ton 5 Star Split AC.", "category": "Home Appliances", "rating": 4.3, "image": "https://images.unsplash.com/photo-1623912175841-37f053dc71c3?q=80&w=1000&auto=format&fit=crop" },
    
    
    
    
    
    { "id": 56, "name": "Zara Flowy Summer Dress", "price": 2500, "description": "Vibrant and lightweight floral dress.", "category": "Women Fashion", "rating": 4.6, "image": "https://images.unsplash.com/photo-1572804013309-59a88b7e92f1?q=80&w=1000&auto=format&fit=crop" },
    { "id": 57, "name": "H&M Casual Crop Top", "price": 799, "description": "Comfortable cotton daily wear top.", "category": "Women Fashion", "rating": 4.2, "image": "https://images.unsplash.com/photo-1503342217505-b0a15ec3261c?q=80&w=1000&auto=format&fit=crop" },
    { "id": 58, "name": "Biba Ethnic Kurta Set", "price": 3200, "description": "Beautiful traditional embroidered kurta.", "category": "Women Fashion", "rating": 4.7, "image": "https://images.unsplash.com/photo-1583391733959-f18306364653?q=80&w=1000&auto=format&fit=crop" },
    { "id": 59, "name": "Fabindia Cotton Saree", "price": 4500, "description": "Authentic handloom cotton saree.", "category": "Women Fashion", "rating": 4.8, "image": "https://images.unsplash.com/photo-1610189013978-43d9b4b09b43?q=80&w=1000&auto=format&fit=crop" },
    
    { "id": 60, "name": "Roadster Premium T-Shirt", "price": 599, "description": "Soft durable solid color t-shirt.", "category": "Men Fashion", "rating": 4.3, "image": "/static/men_60_tshirt_1776789007432.png" },
    { "id": 61, "name": "Levi's Classic Denim", "price": 2999, "description": "501 Original Fit comfortable jeans.", "category": "Men Fashion", "rating": 4.7, "image": "/static/men_61_denim_1776789092505.png" },
    { "id": 62, "name": "Allen Solly Office Shirt", "price": 1800, "description": "Crisp formal wear shirt.", "category": "Men Fashion", "rating": 4.5, "image": "/static/men_62_shirt_1776789197032.png" },
    { "id": 63, "name": "Peter England Formal Trousers", "price": 2200, "description": "Tailored fit formal trousers.", "category": "Men Fashion", "rating": 4.4, "image": "/static/men_63_trousers_1776789296108.png" }
]

def generate_items():

    brand_specific_images = {
        "Apple Notebook Laptop": [
            "https://images.unsplash.com/photo-1517336714731-489689fd1ca8?q=80&w=1000&auto=format&fit=crop",
            "https://images.unsplash.com/photo-1531297172868-9f44cce6d1db?q=80&w=1000&auto=format&fit=crop",
            "https://images.unsplash.com/photo-1611186871348-b1ce696e52c9?q=80&w=1000&auto=format&fit=crop",
            "https://images.unsplash.com/photo-1498050108023-c5249f4df085?q=80&w=1000&auto=format&fit=crop"
        ],
        "Sony Notebook Laptop": [
            "https://images.unsplash.com/photo-1593642702749-b7d2a804fbcf?q=80&w=1000&auto=format&fit=crop",
            "https://images.unsplash.com/photo-1587614382346-4ec70e388b28?q=80&w=1000&auto=format&fit=crop"
        ],
        "Samsung Notebook Laptop": [
            "https://images.unsplash.com/photo-1603302576837-37561b2e2302?q=80&w=1000&auto=format&fit=crop",
            "https://images.unsplash.com/photo-1496181133206-80ce9b88a853?q=80&w=1000&auto=format&fit=crop",
        ],
        "Apple Wireless Headphones": [
            "https://images.unsplash.com/photo-1600294037681-c80b4cb5b434?q=80&w=1000&auto=format&fit=crop",
            "https://images.unsplash.com/photo-1628202926206-c63a34b1aba1?q=80&w=1000&auto=format&fit=crop"
        ],
        "Sony Wireless Headphones": [
            "https://images.unsplash.com/photo-1618366712010-f4ae9c647dcb?q=80&w=1000&auto=format&fit=crop",
            "https://images.unsplash.com/photo-1484704849700-f032a568e944?q=80&w=1000&auto=format&fit=crop",
            "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?q=80&w=1000&auto=format&fit=crop"
        ],
        "Samsung Wireless Headphones": [
            "https://images.unsplash.com/photo-1612222869049-d8ec83637a3c?q=80&w=1000&auto=format&fit=crop",
            "https://images.unsplash.com/photo-1599669500516-1ee19d201af5?q=80&w=1000&auto=format&fit=crop",
            "https://images.unsplash.com/photo-1546435770-a3e426fac365?q=80&w=1000&auto=format&fit=crop"
        ],
        "Apple Tablet Pro": [
            "https://images.unsplash.com/photo-1544244015-0df4b3ffc6b0?q=80&w=1000&auto=format&fit=crop",
            "https://images.unsplash.com/photo-1517055745132-ce53efc9ac99?q=80&w=1000&auto=format&fit=crop",
            "https://images.unsplash.com/photo-1585790050230-5dd28404ccb9?q=80&w=1000&auto=format&fit=crop"
        ],
        "Samsung Tablet Pro": [
            "https://images.unsplash.com/photo-1561154464-82e9adf32764?q=80&w=1000&auto=format&fit=crop",
            "https://images.unsplash.com/photo-1605810730467-68b201f80721?q=80&w=1000&auto=format&fit=crop"
        ],
        "Sony Tablet Pro": [
            "https://images.unsplash.com/photo-1515940175183-6798529cb860?q=80&w=1000&auto=format&fit=crop",
        ],
        "Apple Smartphone": [
            "https://images.unsplash.com/photo-1510557880182-3d4d3cba35a5?q=80&w=1000&auto=format&fit=crop",
            "https://images.unsplash.com/photo-1556656793-08538906a9f8?q=80&w=1000&auto=format&fit=crop",
            "https://images.unsplash.com/photo-1565849904461-04a58ad377e0?q=80&w=1000&auto=format&fit=crop"
        ],
        "Samsung Smartphone": [
            "https://images.unsplash.com/photo-1610945415295-d9bbf067e59c?q=80&w=1000&auto=format&fit=crop",
            "https://images.unsplash.com/photo-1598327105666-5b89351cb315?q=80&w=1000&auto=format&fit=crop"
        ],
        "Sony Smartphone": [
            "https://images.unsplash.com/photo-1533228100845-08145a01bc14?q=80&w=1000&auto=format&fit=crop",
            "https://images.unsplash.com/photo-1512499617640-c74ae3a79d37?q=80&w=1000&auto=format&fit=crop"
        ],
        "Samsung Smart TV": [
            "https://images.unsplash.com/photo-1593305841991-05c297ba4575?q=80&w=1000&auto=format&fit=crop",
            "https://images.unsplash.com/photo-1552820728-8b83bb6b773f?q=80&w=1000&auto=format&fit=crop"
        ],
        "Sony Smart TV": [
            "https://images.unsplash.com/photo-1593784991095-a205069470b6?q=80&w=1000&auto=format&fit=crop",
            "https://images.unsplash.com/photo-1461151304267-38535e780c79?q=80&w=1000&auto=format&fit=crop",
            "https://images.unsplash.com/photo-1601944177325-f8867652837f?q=80&w=1000&auto=format&fit=crop"
        ],
        "Apple Smart TV": [
            "https://images.unsplash.com/photo-1558888401-3cc1de77652d?q=80&w=1000&auto=format&fit=crop"
        ]
    }
    
    for k in brand_specific_images:
        random.shuffle(brand_specific_images[k])

    images = {
        "Shoes": {
            "Running Shoes": [
                "https://images.unsplash.com/photo-1542291026-7eec264c27ff?q=80&w=1000&auto=format&fit=crop",
                "https://images.unsplash.com/photo-1571008887538-b36bb32f4571?q=80&w=1000&auto=format&fit=crop",
                "https://images.unsplash.com/photo-1606107557195-0e29a4b5b4aa?q=80&w=1000&auto=format&fit=crop",
                "https://images.unsplash.com/photo-1560769629-975ec94e6a86?q=80&w=1000&auto=format&fit=crop",
                "https://images.unsplash.com/photo-1491553895911-0055eca6402d?q=80&w=1000&auto=format&fit=crop",
                "https://images.unsplash.com/photo-1597892657493-6847b9640bac?q=80&w=1000&auto=format&fit=crop"
            ],
            "Walking Sneakers": [
                "https://images.unsplash.com/photo-1487956382158-bb926046304a?q=80&w=1000&auto=format&fit=crop",
                "https://images.unsplash.com/photo-1624028409599-ba168bfd6586?q=80&w=1000&auto=format&fit=crop",
                "https://images.unsplash.com/photo-1624028409583-eac582b51895?q=80&w=1000&auto=format&fit=crop",
                "https://images.unsplash.com/photo-1635252261174-aa7945dc2902?q=80&w=1000&auto=format&fit=crop",
                "https://images.unsplash.com/photo-1624028409951-23bae5c11e3f?q=80&w=1000&auto=format&fit=crop",
                "https://images.unsplash.com/photo-1517519610343-021766b185c1?q=80&w=1000&auto=format&fit=crop",
                "https://images.unsplash.com/photo-1526573461737-b504d8040d92?q=80&w=1000&auto=format&fit=crop"
            ],
            "Casual Kicks": [
                "https://images.unsplash.com/photo-1603808033192-082d6919d3e1?q=80&w=1000&auto=format&fit=crop",
                "https://images.unsplash.com/photo-1587563871167-1ee9c731aefb?q=80&w=1000&auto=format&fit=crop",
                "https://images.unsplash.com/photo-1603808033176-9d134e6f2c74?q=80&w=1000&auto=format&fit=crop",
                "https://images.unsplash.com/photo-1603808033587-935942847de4?q=80&w=1000&auto=format&fit=crop"
            ],
            "Athletic Footwear": [
                "https://images.unsplash.com/photo-1460353581641-37baddab0fa2?q=80&w=1000&auto=format&fit=crop",
                "https://images.unsplash.com/photo-1637437757614-6491c8e915b5?q=80&w=1000&auto=format&fit=crop"
            ],
            "Performance Shoes": [
                "https://images.unsplash.com/photo-1676041669566-fead69bd7007?q=80&w=1000&auto=format&fit=crop"
            ]
        },
        "Home Appliances": ["https://images.unsplash.com/photo-1581092160562-40aa08e78837?q=80&w=1000&auto=format&fit=crop", "https://images.unsplash.com/photo-1623912175841-37f053dc71c3?q=80&w=1000&auto=format&fit=crop"],
        "Electronics": ["/static/mock_tablet.jpg", "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?q=80&w=1000&auto=format&fit=crop", "https://images.unsplash.com/photo-1517336714731-489689fd1ca8?q=80&w=1000&auto=format&fit=crop"],
        
        "Women Fashion": ["https://images.unsplash.com/photo-1572804013309-59a88b7e92f1?q=80&w=1000&auto=format&fit=crop", "https://images.unsplash.com/photo-1503342217505-b0a15ec3261c?q=80&w=1000&auto=format&fit=crop", "https://images.unsplash.com/photo-1583391733959-f18306364653?q=80&w=1000&auto=format&fit=crop", "https://images.unsplash.com/photo-1610189013978-43d9b4b09b43?q=80&w=1000&auto=format&fit=crop"],
        "Men Fashion": ["https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?q=80&w=1000&auto=format&fit=crop", "https://images.unsplash.com/photo-1542272604-787c3835535d?q=80&w=1000&auto=format&fit=crop", "https://images.unsplash.com/photo-1596755094514-f8b1e4c70fba?q=80&w=1000&auto=format&fit=crop", "https://images.unsplash.com/photo-1594938298603-c8148c4dae35?q=80&w=1000&auto=format&fit=crop"],
        "Kidsware": {
            "Party Dress": [
                "https://images.unsplash.com/photo-1578897366846-358bb1c2412a?q=80&w=1000&auto=format&fit=crop",
                "https://images.unsplash.com/photo-1620774760711-caa4c94d683a?q=80&w=1000&auto=format&fit=crop",
                "https://images.unsplash.com/photo-1768766928448-079971dcd07b?q=80&w=1000&auto=format&fit=crop"
            ],
            "Casual T-Shirt": [
                "https://images.unsplash.com/photo-1611428813653-aa606c998586?q=80&w=1000&auto=format&fit=crop",
                "https://images.unsplash.com/photo-1620905385976-9f191e837efd?q=80&w=1000&auto=format&fit=crop",
                "https://images.unsplash.com/photo-1627859774205-83c1279a6382?q=80&w=1000&auto=format&fit=crop",
                "https://images.unsplash.com/photo-1627639679690-db4d401aae84?q=80&w=1000&auto=format&fit=crop",
                "https://images.unsplash.com/photo-1622290291468-a28f7a7dc6a8?q=80&w=1000&auto=format&fit=crop"
            ],
            "School Uniform": [
                "https://images.unsplash.com/photo-1519238263530-99bdd11df2ea?q=80&w=1000&auto=format&fit=crop",
                "https://images.unsplash.com/photo-1706117386176-e0eab81b9abc?q=80&w=1000&auto=format&fit=crop",
                "https://images.unsplash.com/photo-1632232963035-bc14755747c9?q=80&w=1000&auto=format&fit=crop"
            ],
            "Cotton Sleepwear": [
                "https://images.unsplash.com/photo-1634188157846-c6e3bdf99420?q=80&w=1000&auto=format&fit=crop",
                "https://images.unsplash.com/photo-1767348823288-3273a3189496?q=80&w=1000&auto=format&fit=crop",
                "https://images.unsplash.com/photo-1558576997-eac36a2f8c7a?q=80&w=1000&auto=format&fit=crop",
                "https://images.unsplash.com/photo-1771419912747-df33d91c329d?q=80&w=1000&auto=format&fit=crop"
            ]
        },
        "Toys": ["https://images.unsplash.com/photo-1587654780291-39c9404d746b?q=80&w=1000&auto=format&fit=crop", "https://images.unsplash.com/photo-1558060370-d64111d52c14?q=80&w=1000&auto=format&fit=crop"]
    }

    target_counts = {
        "Shoes": { 'Adidas': 3, 'Puma': 3, 'Red Tape': 3, 'Nike': 3, 'Skechers': 3 },
        "Electronics": { 'Samsung': 3, 'Apple': 5, 'Sony': 5 },
        
        "Women Fashion": { 'Zara': 4, 'H&M': 4, 'Biba': 4, 'Fabindia': 3 },
        "Men Fashion": { 'Roadster': 4, "Levi's": 4, 'Allen Solly': 4, 'Peter England': 3 },
        "Kidsware": { 'Generic': 15 },
        "Toys": { 'Generic': 15 }
    }

    item_names = {
        "Shoes": ["Walking Sneakers", "Running Shoes", "Athletic Footwear", "Casual Kicks", "Performance Shoes"],
        "Home Appliances": ["Smart Refrigerator", "Inverter AC", "Washing Machine", "Microwave Oven"],
        "Electronics": ["Smart TV", "Notebook Laptop", "Wireless Headphones", "Tablet Pro", "Smartphone"],
        
        "Women Fashion": ["Floral Dress", "Cotton Kurta", "Casual Top", "Handloom Saree"],
        "Men Fashion": ["Classic Jeans", "Formal Shirt", "Casual T-Shirt", "Chino Trousers"],
        "Kidsware": ["Cotton Sleepwear", "School Uniform", "Party Dress", "Casual T-Shirt"],
        "Toys": ["Building Blocks", "Action Figure", "Board Game", "Educational Puzzle"]
    }

    next_id = 100
    for cat, brands in target_counts.items():
        for brand, count in brands.items():
            for i in range(count):
                item_name = random.choice(item_names[cat])
                b_name = "" if brand == 'Generic' else f"{brand} "
                
                if cat == "Electronics":
                    if brand == "Apple":
                        valid_items = ["Notebook Laptop", "Wireless Headphones", "Tablet Pro", "Smartphone"]
                        item_name = random.choice(valid_items)
                    elif brand == "Sony":
                        valid_items = ["Smart TV", "Notebook Laptop", "Wireless Headphones", "Smartphone"]
                        item_name = random.choice(valid_items)
                    elif brand == "Samsung":
                        valid_items = ["Smart TV", "Notebook Laptop", "Wireless Headphones", "Smartphone", "Tablet Pro"]
                        item_name = random.choice(valid_items)
                
                img_url = random.choice(images[cat]) if isinstance(images[cat], list) else ""
                
                # Assign type-specific images for categories with per-type image pools
                if isinstance(images[cat], dict) and item_name in images[cat]:
                    img_url = random.choice(images[cat][item_name])
                
                # Assign specific branding
                if cat == "Electronics":
                    key = brand + " " + item_name
                    if key in brand_specific_images and brand_specific_images[key]:
                        img_url = brand_specific_images[key].pop(0)

                initial_products.append({
                    "id": next_id,
                    "name": f"{b_name}{item_name} {random.randint(1,99)}",
                    "price": random.randint(5, 50) * 100,
                    "description": f"High quality {item_name.lower()} perfect for you.",
                    "category": cat,
                    "rating": round(random.uniform(4.0, 5.0), 1),
                    "image": img_url,
                    "badge_class": "", "badge_icon": "", "badge_text": ""
                })
                next_id += 1


    real_beauty = [
        {"name": "Luxury Rose Perfume", "desc": "A beautiful and long lasting fragrance.", "price": 1200, "img": "/static/perfume_luxury.png", "rating": 4.0},
        {"name": "Maybelline Fit Me Foundation", "desc": "Matte and poreless liquid foundation.", "price": 550, "img": "/static/foundation_maybelline.png", "rating": 4.5},
        {"name": "Lakme Absolute Foundation", "desc": "Flawless matte liquid foundation.", "price": 850, "img": "/static/foundation_lakme.png", "rating": 4.4},
        {"name": "Huda Beauty Nude Eyeshadow Palette", "desc": "Iconic high pigment eyeshadow palette with 18 shades.", "price": 4500, "img": "https://m.media-amazon.com/images/I/61Cg-A2J7gL._SL1500_.jpg", "rating": 4.8},
        {"name": "L'Oréal Paris Revitalift Serum", "desc": "Hyaluronic acid face serum.", "price": 999, "img": "/static/serum_loreal.png", "rating": 4.6},
        {"name": "MAC Matte Lipstick Ruby Woo", "desc": "Iconic vivid blue-red matte lipstick.", "price": 1900, "img": "https://m.media-amazon.com/images/I/51r26GZ0+4L._SL1500_.jpg", "rating": 4.7},
        {"name": "Clinique Moisture Surge", "desc": "100H auto-replenishing hydrator.", "price": 2950, "img": "https://m.media-amazon.com/images/I/61NfC95NlBL._SL1000_.jpg", "rating": 4.5},
        {"name": "Estee Lauder Night Repair", "desc": "Advanced night repair synchronised multi-recovery complex.", "price": 8500, "img": "https://m.media-amazon.com/images/I/51X5yU4D12L._SL1500_.jpg", "rating": 4.9},
        {"name": "Fenty Beauty Gloss Bomb", "desc": "Universal lip luminizer for explosive shine.", "price": 2100, "img": "https://m.media-amazon.com/images/I/51XHTxOhWXL._SL1000_.jpg", "rating": 4.8},
        {"name": "Anastasia Beverly Hills Brow Wiz", "desc": "Ultra-slim retractable detailing eyebrow pencil.", "price": 2400, "img": "https://m.media-amazon.com/images/I/51L8vC4t+1L._SL1000_.jpg", "rating": 4.6}
    ]

    for b in real_beauty:
        initial_products.append({
            "id": next_id,
            "name": b["name"],
            "price": b["price"],
            "description": b["desc"],
            "category": "Beauty",
            "rating": b["rating"],
            "image": b["img"],
            "badge_class": "", "badge_icon": "", "badge_text": ""
        })
        next_id += 1


    real_appliances = [
        {"name": "Samsung 28L Convection Microwave Oven", "desc": "Perfect for baking, grilling, reheating, and defrosting.", "price": 11500, "img": "https://m.media-amazon.com/images/I/81cKSsQS+GL._SL1500_.jpg", "rating": 4.5},
        {"name": "Samsung 1.5 Ton 5 Star Inverter Split AC", "desc": "Fast cooling energy efficient AC with copper condenser.", "price": 42000, "img": "https://m.media-amazon.com/images/I/715rBETRD9L._SL1500_.jpg", "rating": 4.7},
        {"name": "Samsung 6.5 kg Fully-Automatic Top Load", "desc": "Center Jet Technology for powerful washing.", "price": 15500, "img": "https://5.imimg.com/data5/SELLER/Default/2022/12/GO/UJ/PX/160638464/samsung-6-5-kg-fully-automatic-top-loading-washing-machine-1000x1000.jpg", "rating": 4.4},
        {"name": "LG 655 L Frost Free Side-by-Side Refrigerator", "desc": "Premium side-by-side refrigerator for large families.", "price": 75000, "img": "https://m.media-amazon.com/images/I/61KTSu7mEbL._SL1500_.jpg", "rating": 4.8},
        {"name": "LG 8 Kg 5 Star Front Load Washing Machine", "desc": "Inverter Direct Drive Technology.", "price": 35000, "img": "https://m.media-amazon.com/images/I/71b92zBZndL._SL1500_.jpg", "rating": 4.6},
        {"name": "LG 1.5 Ton 5 Star AI DUAL Inverter AC", "desc": "Super convertible 6-in-1 cooling.", "price": 45000, "img": "https://m.media-amazon.com/images/I/81wujRO8qLL._SL1500_.jpg", "rating": 4.7},
        {"name": "LG 32 L Charcoal Convection Microwave", "desc": "Healthy Heart auto cook menu.", "price": 18000, "img": "https://m.media-amazon.com/images/I/71LeVxnO4+L._SL1500_.jpg", "rating": 4.5},
        {"name": "LG 260 L 3 Star Frost Free Double Door", "desc": "Smart Inverter Compressor refrigerator.", "price": 26000, "img": "https://sesons.com/wp-content/uploads/2022/08/lg-260.5.jpg", "rating": 4.4},
        {"name": "Blue Star 1.5 Ton 3 Star Inverter Split AC", "desc": "Turbo cool technology.", "price": 35000, "img": "https://darlingretail.com/cdn/shop/files/20_41889eb2-b670-4b26-9f5b-3a9813c72d3f_800x.webp?v=1748351501", "rating": 4.3},
        {"name": "Blue Star 1 Ton 4 Star Inverter Split AC", "desc": "Perfect for small rooms.", "price": 31000, "img": "https://5.imimg.com/data5/SELLER/Default/2024/3/404815925/VH/DQ/UT/198908518/blue-star-4-star-1-ton-inverter-split-ac-1000x1000.jpg", "rating": 4.4},
        {"name": "Blue Star Water Purifier RO+UV+UF", "desc": "Alkaline water purifier with multi-stage filtration.", "price": 12000, "img": "https://choicebestforyou.com/wp-content/uploads/2020/07/blue-star-alkaline-water-purifier.jpg", "rating": 4.2},
        {"name": "Blue Star 1.5 Ton Window AC", "desc": "Highly efficient window AC.", "price": 29000, "img": "https://mycoolcare.com/wp-content/uploads/2024/12/Blue-Star-Window-AC-WFA309GN.jpg", "rating": 4.1},
        {"name": "Blue Star Portable Air Conditioner", "desc": "1 Ton portable compressor AC.", "price": 33000, "img": "https://arihantelectronics.org/wp-content/uploads/2020/05/bluestar-portable-1536x1536.png", "rating": 4.0}
    ]

    for app in real_appliances:
        initial_products.append({
            "id": next_id,
            "name": app["name"],
            "price": app["price"],
            "description": app["desc"],
            "category": "Home Appliances",
            "rating": app["rating"],
            "image": app["img"],
            "badge_class": "", "badge_icon": "", "badge_text": ""
        })
        next_id += 1


    real_books = [
        {"name": "To Kill a Mockingbird", "desc": "A classic of modern American literature detailing racial injustice.", "price": 499, "img": "https://covers.openlibrary.org/b/isbn/9780060935467-L.jpg", "rating": 4.9},
        {"name": "1984", "desc": "A dystopian social science fiction novel and cautionary tale.", "price": 399, "img": "https://covers.openlibrary.org/b/isbn/9780451524935-L.jpg", "rating": 4.8},
        {"name": "Pride and Prejudice", "desc": "An 1813 novel of manners written by Jane Austen.", "price": 350, "img": "https://covers.openlibrary.org/b/isbn/9780141439518-L.jpg", "rating": 4.7},
        {"name": "The Catcher in the Rye", "desc": "A classic novel exploring themes of teenage angst and alienation.", "price": 450, "img": "https://covers.openlibrary.org/b/isbn/9780316769488-L.jpg", "rating": 4.5},
        {"name": "Steve Jobs by Walter Isaacson", "desc": "The exclusive, authorized biography of Apple co-founder Steve Jobs.", "price": 799, "img": "https://covers.openlibrary.org/b/isbn/9781451648539-L.jpg", "rating": 4.8},
        {"name": "The Diary of a Young Girl", "desc": "The writings from the Dutch-language diary kept by Anne Frank.", "price": 299, "img": "https://covers.openlibrary.org/b/isbn/9780553296983-L.jpg", "rating": 4.9},
        {"name": "Long Walk to Freedom", "desc": "An autobiography written by South African President Nelson Mandela.", "price": 850, "img": "https://covers.openlibrary.org/b/isbn/9780316548182-L.jpg", "rating": 4.8},
        {"name": "Thinking, Fast and Slow", "desc": "A book on decision-making by Nobel laureate Daniel Kahneman.", "price": 599, "img": "https://covers.openlibrary.org/b/isbn/9780374533557-L.jpg", "rating": 4.6},
        {"name": "How to Win Friends and Influence People", "desc": "One of the best-selling self-help books ever published.", "price": 399, "img": "https://covers.openlibrary.org/b/isbn/9780671027032-L.jpg", "rating": 4.7},
        {"name": "The Power of Habit", "desc": "Explores the science behind habit creation and reformation.", "price": 499, "img": "https://covers.openlibrary.org/b/isbn/9780812981605-L.jpg", "rating": 4.5},
        {"name": "Good to Great", "desc": "Management book by Jim C. Collins that describes how companies transition.", "price": 699, "img": "https://covers.openlibrary.org/b/isbn/9780066620992-L.jpg", "rating": 4.6},
        {"name": "Zero to One", "desc": "Notes on Startups, or How to Build the Future.", "price": 550, "img": "https://covers.openlibrary.org/b/isbn/9780804139298-L.jpg", "rating": 4.5},
        {"name": "The Lean Startup", "desc": "How Today's Entrepreneurs Use Continuous Innovation.", "price": 599, "img": "https://covers.openlibrary.org/b/isbn/9780307887894-L.jpg", "rating": 4.6},
        {"name": "Think and Grow Rich", "desc": "A personal development and self-help book by Napoleon Hill.", "price": 299, "img": "https://covers.openlibrary.org/b/isbn/9781585424337-L.jpg", "rating": 4.7},
        {"name": "Sapiens: A Brief History of Humankind", "desc": "A book by Yuval Noah Harari mapping human history.", "price": 799, "img": "https://covers.openlibrary.org/b/isbn/9780062316097-L.jpg", "rating": 4.8}
    ]

    for b in real_books:
        initial_products.append({
            "id": next_id,
            "name": b["name"],
            "price": b["price"],
            "description": b["desc"],
            "category": "Books",
            "rating": b["rating"],
            "image": b["img"],
            "badge_class": "", "badge_icon": "", "badge_text": ""
        })
        next_id += 1
    
    with open('c:/Users/DELL/OneDrive/Desktop/Product recommendation/catalog.json', 'w', encoding='utf-8') as f:
        json.dump(initial_products, f, indent=4)

generate_items()
print("Generated catalog.json with", len(initial_products), "items")
