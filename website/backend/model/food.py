from db.mysql import get_db_connection

def get_all_foods():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    query = "SELECT * FROM foods"
    cursor.execute(query)

    foods = cursor.fetchall()

    cursor.close()
    conn.close()

    return foods


def add_food(name, description, price, image_url):
    conn = get_db_connection()
    cursor = conn.cursor()

    query = """
        INSERT INTO foods (name, description, price, image_url)
        VALUES (%s, %s, %s, %s)
    """

    cursor.execute(query, (name, description, price, image_url))
    conn.commit()

    cursor.close()
    conn.close()