from models.customer import Customer
from models.transaction import Transaction
from models.product import Product

def get_recommendations_by_location(location, limit=5):
    customers = Customer.query.filter_by(location=location).all()
    if not customers:
        return {"message": f"No customers found in {location}"}

    customer_ids = [c.customer_id for c in customers]

    transactions = Transaction.query.filter(
        Transaction.customer_id.in_(customer_ids)
    ).all()
    if not transactions:
        return {"message": f"No transactions found for {location}"}

    counts = {}
    for t in transactions:
        counts[t.product_id] = counts.get(t.product_id, 0) + (t.quantity or 1)

    sorted_products = sorted(counts.items(), key=lambda x: x[1], reverse=True)[:limit]

    result = []
    for pid, count in sorted_products:
        p = Product.query.get(pid)
        if p:
            result.append({
                "product_id": p.product_id,
                "product_name": p.product_name,
                "description": p.description,
                "price": p.price,
                "popularity": count
            })

    if not result:
        return {"message": "No popular products found"}

    return {"location": location, "recommended_products": result}
