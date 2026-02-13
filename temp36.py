"""1. Total Revenue from Active Customers
Problem Statement
You are given a list of customer dictionaries.
Each customer has:
• name
• purchases → list of purchase amounts
• active → boolean
Calculate the total revenue generated only by active customers, but:
• Ignore purchase amounts less than 100
• Apply a 10% tax to each valid purchase before summing

customers = [
    {"name": "A", "purchases": [50, 200, 300], "active": True},
    {"name": "B", "purchases": [500, 20], "active": False},
    {"name": "C", "purchases": [150, 250], "active": True}
]
Output
990.0
"""
def main():
    customers = [
        {"name": "A", "purchases": [50, 200, 300], "active": True},
        {"name": "B", "purchases": [500, 20], "active": False},
        {"name": "C", "purchases": [150, 250], "active": True}
    ]
    
    valid = list(filter(lambda customer:  customer["active"], customers))
    total_revenue = 0
    for customer in valid:
        valid_purchases = filter(lambda p: p >= 100, customer["purchases"])
        total_revenue += sum(map(lambda x: x*1.1, valid_purchases))
    print(total_revenue)
if __name__=="__main__":
    main()