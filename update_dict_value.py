data = {
    "_id": "123",
    "name": "John Doe",
    "email": "john@example.com",
    "orders": [
        {"orderId": "A100", "amount": 50},
        {"orderId": "A101", "amount": 100}
    ]
}

for order in data["orders"]:
    if order['orderId'] == 'A100':
        order['amount'] = '150'
        break

print(data)
