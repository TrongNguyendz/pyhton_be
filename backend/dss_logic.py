import sqlite3

def recommend_products(db_path, skin_type, problem, budget):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    query = """
    SELECT name, brand, price, suitable_for, problem, image_url
    FROM products
    WHERE suitable_for=? AND problem=? AND price <= ?
    ORDER BY price ASC
    LIMIT 5
    """
    cursor.execute(query, (skin_type, problem, budget))
    rows = cursor.fetchall()
    conn.close()

    results = []
    for row in rows:
        results.append({
            "name": row[0],
            "brand": row[1],
            "price": row[2],
            "suitable_for": row[3],
            "problem": row[4],
            "image_url": row[5]
        })
    return results
