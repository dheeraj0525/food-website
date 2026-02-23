from db.mysql import get_db_connection

def create_order(user_id, total):
    conn = get_db_connection()
    cursor = conn.cursor()

    query = "INSERT INTO orders (user_id, total, status) VALUES (%s, %s, %s)"
    cursor.execute(query, (user_id, total, "pending"))

    order_id = cursor.lastrowid
    conn.commit()

    cursor.close()
    conn.close()

    return order_id

def add_order_item(order_id, food_id, quantity):
    conn = get_db_connection()
    cursor = conn.cursor()

    query = """
        INSERT INTO order_items (order_id, food_id, quantity)
        VALUES (%s, %s, %s)
    """

    cursor.execute(query, (order_id, food_id, quantity))
    conn.commit()

    cursor.close()
    conn.close()

def get_user_orders(user_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    query = "SELECT * FROM orders WHERE user_id = %s"
    cursor.execute(query, (user_id,))
    orders = cursor.fetchall()
    cursor.close()
    conn.close()
    return orders