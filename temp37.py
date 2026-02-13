"""2. Problem Statement
You are given a list of products as tuples:

 Task:
• Keep only products in category "Electronics"
• Apply a 20% discount
• Return the total discounted price
Input
products = [
    ("Laptop", "Electronics", 1000),
    ("Shirt", "Clothing", 50),
    ("Phone", "Electronics", 500)
]
Output:
1200.0"""
def main():
    products = [
        ("Laptop", "Electronics", 1000),
        ("Shirt", "Clothing", 50),
        ("Phone", "Electronics", 500)
    ]
    electronics = filter(lambda p: p[1] == "Electronics", products)
    total_discounted_price = sum(map(lambda x: x[2]*0.8, electronics))
    print(total_discounted_price)
if __name__=="__main__":
    main()