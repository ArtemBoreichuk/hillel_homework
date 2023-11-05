data = [
    {"name": "Alisa", "country": "UA", "item": "socks", "price": 15},
    {"name": "Alisa", "country": "UA", "item": "socks", "price": 25},
    {"name": "Ben", "country": "US", "item": "pencil", "price": 95},
    {"name": "Alisa", "country": "UA", "item": "pencil", "price": 45},
    {"name": "Oleg", "country": "GB", "item": "socks", "price": 100},
    {"name": "Ben", "country": "US", "item": "pencil", "price": 10}
       ]
workers = set(item["name"] for item in data)
worker_sales = {}
for worker in workers:
    total_sales = sum(item["price"] for item in data if item["name"] == worker)
    worker_sales[worker] = total_sales
print("Список працівників:", workers)
print("Суми виторгу за тиждень:")
for worker, total_sales in worker_sales.items():
    print(f"{worker}: {total_sales}")
