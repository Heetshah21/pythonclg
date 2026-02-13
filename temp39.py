"""Multi-Region Sales Analytics Engine
Problem Statement
You are given a list of regions. Each region contains multiple stores, and each store contains multiple transactions.
Each transaction has:
• amount (float)
• category (string)
• successful (boolean)
Task
• Consider only transactions that:
• Are successful
• Belong to category "Electronics"
• Have amount ≥ 100
Apply:
• 18% GST to each valid transaction
• Then apply an additional 5% regional surcharge
Compute:
• The total revenue per region
• Then return the grand total across all regions

Input:
regions = [
{
"region": "North",
"stores": [
{
"transactions": [
{"amount": 200, "category": "Electronics", "successful": True},
{"amount": 50, "category": "Electronics", "successful": True},
{"amount": 500, "category": "Clothing", "successful": True}
]
}
]
},
{
"region": "South",
"stores": [
{
"transactions": [
{"amount": 300, "category": "Electronics", "successful": True},
{"amount": 150, "category": "Electronics", "successful": False}
]
}
]
}
]

Final output: single float (grand total)"""
def main():
    regions = [
        {
            "region": "North",
            "stores": [
                {
                    "transactions": [
                        {"amount": 200, "category": "Electronics", "successful": True},
                        {"amount": 50, "category": "Electronics", "successful": True},
                        {"amount": 500, "category": "Clothing", "successful": True}
                    ]
                }
            ]
        },
        {
            "region": "South",
            "stores": [
                {
                    "transactions": [
                        {"amount": 300, "category": "Electronics", "successful": True},
                        {"amount": 150, "category": "Electronics", "successful": False}
                    ]
                }
            ]
        }
    ]

    grand_total = 0

    for region in regions:
        region_total = 0
        for store in region["stores"]:
            valid_txs = filter(lambda t: (
                t["successful"] and 
                t["category"] == "Electronics" and 
                t["amount"] >= 100
            ), store["transactions"])
            
            taxed_amounts = map(lambda t: t["amount"] * 1.18 * 1.05, valid_txs)
            
            region_total += sum(taxed_amounts)
            
        print(f"Region {region['region']} Total: {region_total:.2f}")
        grand_total += region_total

    print("-" * 30)
    print(f"Grand Total Revenue: {grand_total:.2f}")

if __name__ == "__main__":
    main()