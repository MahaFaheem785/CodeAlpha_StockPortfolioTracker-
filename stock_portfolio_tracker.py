import csv
import os
from datetime import datetime


STOCK_PRICES = {
    "AAPL":  180,
    "TSLA":  250,
    "GOOGL": 140,
    "AMZN":  185,
    "MSFT":  420,
    "META":  500,
    "NFLX":  650,
}

def show_available_stocks():
    print("\n Available Stocks:")
    print("-" * 30)
    print(f"{'Symbol':<10} {'Price (USD)':>12}")
    print("-" * 30)
    for symbol, price in STOCK_PRICES.items():
        print(f"{symbol:<10} ${price:>11,.2f}")
    print("-" * 30)

def get_portfolio():
    portfolio = {}
    print("\nEnter stock symbol and quantity (type 'done' when finished).")

    while True:
        symbol = input("\nStock symbol (or 'done'): ").strip().upper()

        if symbol == "DONE":
            break

        if symbol not in STOCK_PRICES:
            print(f"⚠  '{symbol}' not found. Choose from: {', '.join(STOCK_PRICES)}")
            continue

        try:
            qty = int(input(f"Quantity of {symbol}: ").strip())
            if qty <= 0:
                print("⚠  Quantity must be a positive number.")
                continue
        except ValueError:
            print("⚠  Please enter a valid integer.")
            continue

        if symbol in portfolio:
            portfolio[symbol] += qty          
        else:
            portfolio[symbol] = qty

    return portfolio

def display_portfolio(portfolio):
    if not portfolio:
        print("\n  No stocks entered.")
        return 0

    total = 0
    print("\n" + "=" * 50)
    print("        YOUR STOCK PORTFOLIO SUMMARY")
    print("=" * 50)
    print(f"{'Symbol':<10} {'Qty':>6} {'Price':>12} {'Value':>14}")
    print("-" * 50)

    for symbol, qty in portfolio.items():
        price = STOCK_PRICES[symbol]
        value = price * qty
        total += value
        print(f"{symbol:<10} {qty:>6} ${price:>11,.2f} ${value:>13,.2f}")

    print("-" * 50)
    print(f"{'TOTAL INVESTMENT':.<36} ${total:>13,.2f}")
    print("=" * 50)
    return total

def save_to_file(portfolio, total):
    choice = input("\nSave results? (1 = CSV  2 = TXT  3 = Skip): ").strip()

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    if choice == "1":
        filename = f"portfolio_{timestamp}.csv"
        with open(filename, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Symbol", "Quantity", "Price (USD)", "Total Value (USD)"])
            for symbol, qty in portfolio.items():
                price = STOCK_PRICES[symbol]
                writer.writerow([symbol, qty, price, price * qty])
            writer.writerow([])
            writer.writerow(["", "", "TOTAL", total])
        print(f"Saved as '{filename}'")

    elif choice == "2":
        filename = f"portfolio_{timestamp}.txt"
        with open(filename, "w") as f:
            f.write("STOCK PORTFOLIO REPORT\n")
            f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("=" * 45 + "\n")
            f.write(f"{'Symbol':<10} {'Qty':>6} {'Price':>10} {'Value':>12}\n")
            f.write("-" * 45 + "\n")
            for symbol, qty in portfolio.items():
                price = STOCK_PRICES[symbol]
                value = price * qty
                f.write(f"{symbol:<10} {qty:>6} ${price:>9,.2f} ${value:>11,.2f}\n")
            f.write("-" * 45 + "\n")
            f.write(f"Total Investment: ${total:,.2f}\n")
        print(f" Saved as '{filename}'")

    else:
        print("Results not saved.")

def main():
    print("=" * 50)
    print("     STOCK PORTFOLIO TRACKER — CodeAlpha")
    print("=" * 50)

    show_available_stocks()
    portfolio = get_portfolio()
    total     = display_portfolio(portfolio)

    if portfolio:
        save_to_file(portfolio, total)

    again = input("\nTrack another portfolio? (yes/no): ").strip().lower()
    if again in ("yes", "y"):
        main()
    else:
        print("\nGoodbye! Happy investing ")

if __name__ == "__main__":
    main()