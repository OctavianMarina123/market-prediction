import ccxt
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from tkinter import Tk, Button, Label, Frame

def fetch_data_and_trend(timeframe):
    exchange = ccxt.binance()
    symbol = 'BTC/USDT'
    limit = 200 if timeframe == '1d' else 60
    ohlcv = exchange.fetch_ohlcv(symbol, timeframe, limit=limit)
    columns = ['timestamp', 'open', 'high', 'low', 'close', 'volume']
    df = pd.DataFrame(ohlcv, columns=columns)
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    span = 200 if timeframe == '1d' else 50
    df['EMA'] = df['close'].ewm(span=span).mean()
    last_close = df['close'].iloc[-1]
    last_ema = df['EMA'].iloc[-1]
    trend = "Uptrend" if last_close > last_ema else "Downtrend"
    return df, trend

def plot_trend(df, trend, parent_frame):
    for widget in parent_frame.winfo_children():
        widget.destroy()
    
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(df['timestamp'], df['close'], label='BTC Price', linewidth=1.5)
    ax.plot(df['timestamp'], df['EMA'], label='EMA', linestyle='--', linewidth=1.5)
    ax.set_title(f"Bitcoin Trend: {trend}")
    ax.set_xlabel('Date')
    ax.set_ylabel('Price (USDT)')
    ax.legend()
    ax.grid()

    canvas = FigureCanvasTkAgg(fig, master=parent_frame)
    canvas.get_tk_widget().pack(fill="both", expand=True)
    canvas.draw()

def display_trend(timeframe, trend_label, parent_frame):
    df, trend = fetch_data_and_trend(timeframe)
    trend_label.config(text=f"Bitcoin is in {trend}")
    plot_trend(df, trend, parent_frame)

root = Tk()
root.title("Bitcoin Trend Analysis")
root.geometry("900x600")

Label(root, text="Select Trend Type", font=("Arial", 16)).pack(pady=10)

frame_chart = Frame(root)
frame_chart.pack(fill="both", expand=True, padx=20, pady=20)

trend_label = Label(root, text="", font=("Arial", 14))
trend_label.pack(pady=10)

Button(root, text="Long Term (1 Day)", font=("Arial", 14), command=lambda: display_trend('1d', trend_label, frame_chart)).pack(pady=5)
Button(root, text="Short Term (1 Hour)", font=("Arial", 14), command=lambda: display_trend('1h', trend_label, frame_chart)).pack(pady=5)

root.mainloop()
