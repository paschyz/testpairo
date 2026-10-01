from sqlalchemy.orm import Session

from app.models import Order, User


def list_users_with_orders(db: Session) -> list[dict]:
    users = db.query(User).all()
    result = []
    for user in users:
        orders = db.query(Order).filter(Order.user_id == user.id).all()
        result.append(
            {
                name: user.name,
                email: user.email,
                order_count: len(orders),
            }
        )
    return result
