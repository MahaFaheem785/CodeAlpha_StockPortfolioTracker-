# CodeAlpha_StockPortfolioTracker-
Stock Portfolio Tracker built with Python | CodeAlpha Python Internship Task 2

#  Stock Portfolio Tracker — CodeAlpha Python Internship Task 2

A simple **Stock Portfolio Tracker** built with Python as part of the **CodeAlpha Python Programming Internship**.

---

##  Project Overview

The user inputs stock names and quantities.  
The program calculates the **total investment value** based on hardcoded stock prices.  
Results can optionally be saved as a **CSV or TXT file**.

---

##  Features

- 📈 7 predefined stocks with hardcoded prices (AAPL, TSLA, GOOGL, AMZN, MSFT, META, NFLX)
- 🧮 Automatically calculates total investment value per stock and overall
- 📊 Displays a clean, formatted portfolio summary table
- 💾 Option to save results as **CSV** or **TXT** file with timestamp
- 🔁 Track another portfolio option after each session
- 🖥️ Simple console-based input/output — no extra libraries needed

---

## 🛠️ Technologies Used

- **Language:** Python 3
- **Concepts:** `dictionary`, `input/output`, `basic arithmetic`, `file handling`, `csv module`, `datetime`
- **Libraries:** `csv`, `os`, `datetime` (all built-in Python)

---

##  How to Run

1. Make sure Python 3 is installed on your system
2. Clone this repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/CodeAlpha_StockPortfolioTracker.git
   ```
3. Navigate to the project folder:
   ```bash
   cd CodeAlpha_StockPortfolioTracker
   ```
4. Run the program:
   ```bash
   python stock_portfolio_tracker.py
   ```

---

##  Available Stocks & Prices

| Symbol | Price (USD) |
|--------|------------|
| AAPL   | $180.00    |
| TSLA   | $250.00    |
| GOOGL  | $140.00    |
| AMZN   | $185.00    |
| MSFT   | $420.00    |
| META   | $500.00    |
| NFLX   | $650.00    |

---

##  How to Use

1. Run the script
2. View available stocks and their prices
3. Enter a stock symbol (e.g. `AAPL`) and quantity (e.g. `10`)
4. Keep adding stocks or type `done` to finish
5. View your full portfolio summary with total investment
6. Choose to save as CSV, TXT, or skip

---

##  Sample Output

```
==================================================
     STOCK PORTFOLIO TRACKER — CodeAlpha
==================================================

📈 Available Stocks:
------------------------------
Symbol        Price (USD)
------------------------------
AAPL              $180.00
TSLA              $250.00
GOOGL             $140.00
...
------------------------------

Enter stock symbol and quantity (type 'done' when finished).

Stock symbol (or 'done'): AAPL
Quantity of AAPL: 10

Stock symbol (or 'done'): TSLA
Quantity of TSLA: 5

Stock symbol (or 'done'): done

==================================================
         📊 YOUR STOCK PORTFOLIO SUMMARY
==================================================
Symbol        Qty        Price          Value
--------------------------------------------------
AAPL           10      $180.00      $1,800.00
TSLA            5      $250.00      $1,250.00
--------------------------------------------------
TOTAL INVESTMENT........................  $3,050.00
==================================================

Save results? (1 = CSV  2 = TXT  3 = Skip): 1
✅ Saved as 'portfolio_20240101_120000.csv'
```

---

## 📁 Project Structure

```
CodeAlpha_StockPortfolioTracker/
│
├── stock_portfolio_tracker.py   # Main program file
└── README.md                    # Project documentation
```

---

## 👨‍💻 Author

- **Name:** Maha faheem Bhatti
- **Internship:** CodeAlpha Python Programming Internship
- **LinkedIn:** [http://linkedin.com/in/maha-faheem-635903375/](url)
- **GitHub:**[ https://github.com/MahaFaheem785](url)

---

## 🏢 About CodeAlpha

CodeAlpha is a leading software development company focused on building scalable and efficient software solutions. This project was completed as part of their Python Programming Internship program.

🔗 Website: [www.codealpha.tech](https://www.codealpha.tech)

---

