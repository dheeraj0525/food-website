from db.mysql import get_db_connection
from werkzeug.security import generate_password_hash, check_password_hash

def create_user(name, email, password):
    conn = get_db_connection()
    cursor = conn.cursor()

    password_hash = generate_password_hash(password)

    query = """
        INSERT INTO users (name, email, password_hash)
        VALUES (%s, %s, %s)
    """

    cursor.execute(query, (name, email, password_hash))
    conn.commit()

    cursor.close()
    conn.close()

def get_user_by_email(email):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    query = "SELECT * FROM users WHERE email = %s"
    cursor.execute(query, (email,))
    user = cursor.fetchone()
    cursor.close()
    conn.close()

    return user

def verify_user(email, password):
    user = get_user_by_email(email)

    if not user:
        return None

    if check_password_hash(user["password_hash"], password):
        return user

    return None