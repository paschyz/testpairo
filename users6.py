# users6.py
import pandas as pd
from db import get_session


def get_all_users():
    session = get_session()
    users = session.query(User).all()
    result = []
    for user in users:
        orders = session.query(Order).filter_by(user_id=user.id).all()
        result.append({
            name: user.name,
            email: user.email,
            order_count: len(orders),
            last_order: orders[-1].created_at if orders else None,
        })
    return result

