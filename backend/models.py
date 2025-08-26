import sqlite3
from werkzeug.security import generate_password_hash

def init_db():
    conn = sqlite3.connect("cosmetics.db")
    cursor = conn.cursor()

    # User table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT UNIQUE,
        password TEXT
    )
    """)

    # Demo user
    cursor.execute("INSERT OR IGNORE INTO users (email, password) VALUES (?, ?)", 
                   ("test@example.com", generate_password_hash("123456")))

    # Products table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        brand TEXT,
        price REAL,
        suitable_for TEXT,
        problem TEXT,
        image_url TEXT
    )
    """)

    cursor.executemany("""
    INSERT INTO products (name, brand, price, suitable_for, problem, image_url)
    VALUES (?, ?, ?, ?, ?, ?)
    """, [
        ("Cleanser A", "BrandX", 200, "oily", "acne", "/images/cleanser.jpg"),
        ("Moisturizer B", "BrandY", 300, "dry", "wrinkles", "/images/moisturizer.jpg"),
        ("Serum C", "BrandZ", 400, "oily", "dark spots", "/images/serum.jpg"),
        ("Toner D", "BrandX", 150, "sensitive", "redness", "/images/toner.jpg"),
        ("Sunscreen E", "BrandY", 250, "all", "prevention", "/images/sunscreen.jpg")
    ])
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
