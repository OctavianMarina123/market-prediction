# Bitcoin Trend Analysis Application

This Python-based application analyzes Bitcoin's trend using the Exponential Moving Average (EMA). The application provides a graphical interface for users to select between a long-term (1-day interval) or short-term (1-hour interval) analysis, and displays:
- The current trend (Uptrend/Downtrend).
- A graph showing Bitcoin's price with the EMA line.

---

## Features
- Fetches real-time Bitcoin price data from Binance.
- Calculates EMA for selected timeframes (long-term or short-term).
- Displays the trend (Uptrend/Downtrend) in the graphical interface.
- Visualizes Bitcoin's price movements and the EMA.

---

## Prerequisites
Ensure you have the following installed:
- Python 3.8 or higher
- Required Python libraries: `ccxt`, `pandas`, `matplotlib`, `tkinter` (tkinter is built-in with Python).

Install the necessary libraries using:
```bash
pip install ccxt pandas matplotlib

bitcoin-trend-analysis/
│
├── README.md                   # Documentation for the project
├── appinfo.txt                 # Details about the application
├── app.py                      # Main script for the application
├── market_prediction.ipynb     # Jupyter Notebook for further market analysis
└── .gitignore                  # Specifies files to ignore in the repository
