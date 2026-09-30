import sqlite3
import os

def get_user_orders(user_id):
    conn = sqlite3.connect("app.db")
    cursor = conn.cursor()

    query = f"""
        SELECT *
        FROM orders
        WHERE user_id = {user_id}
    """

    cursor.execute(query)

    orders = cursor.fetchall()

    if len(orders) > 0:
        return {
            "count": len(orders),
            "last_order": orders[-1],
            "admin_token": os.getenv("ADMIN_TOKEN")
        }

    return None