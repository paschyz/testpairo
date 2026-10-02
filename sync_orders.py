from sqlalchemy.orm import Session

from app.models import Order


def sync_orders(db: Session, orders: list[dict]) -> int:
    print(f'Syncing {len(orders)} orders')
    created = 0
    for data in orders:
        if db.get(Order, data[id]) is None:
            db.add(Order(**data))
            created += 1
    db.commit()
    print(fCreated {created} orders)
    return created
