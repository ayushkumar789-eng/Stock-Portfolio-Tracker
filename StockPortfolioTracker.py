"""
Stock Portfolio Tracker
-----------------------
A simple Python program to track stock investments.

Features:
- User inputs stock name and quantity
- Uses predefined stock prices
- Calculates total investment
- Saves result to a file

Author: Ayush Kumar
Internship: CodeAlpha - Python Programming
Task: Task 2
"""

# Predefined stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 2700,
    "AMZN": 3300
}

portfolio = {}
total_investment = 0

print("📊 Welcome to Stock Portfolio Tracker")

while True:
    stock = input("\nEnter stock name (or 'done' to finish): ").strip().upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("❌ Stock not available. Try again.")
        continue

    try:
        quantity = int(input(f"Enter quantity of {stock}: "))
    except ValueError:
        print("❌ Please enter a valid number.")
        continue

    portfolio[stock] = portfolio.get(stock, 0) + quantity

# Calculate total investment
print("\n📈 Your Portfolio:")
for stock, qty in portfolio.items():
    price = stock_prices[stock]
    investment = price * qty
    total_investment += investment
    print(f"{stock} → {qty} shares × ${price} = ${investment}")

print(f"\n💰 Total Investment Value: ${total_investment}")

# Save to file
save = input("\nDo you want to save this to a file? (yes/no): ").lower()

if save == "yes":
    with open("portfolio.txt", "w") as file:
        file.write("Stock Portfolio Summary\n")
        file.write("------------------------\n")
        for stock, qty in portfolio.items():
            price = stock_prices[stock]
            investment = price * qty
            file.write(f"{stock} → {qty} × ${price} = ${investment}\n")
        file.write(f"\nTotal Investment: ${total_investment}")

    print("✅ Portfolio saved to portfolio.txt")

print("\n👋 Thank you for using the tracker!")
