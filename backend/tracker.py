import requests
import matplotlib.pyplot as plt
from datetime import datetime
import matplotlib.dates as mdates
import os
import matplotlib
matplotlib.use('Agg')  # Necessary for environments without a display
# Set matplotlib to use a non-interactive backend

def plot_crypto_ticker(symbol, interval, limit, filename):
    """
    Plots the price chart for a given cryptocurrency symbol and interval.

    Parameters:
    - symbol: Cryptocurrency symbol (e.g., 'BTCUSDT').
    - interval: Chart interval (e.g., '12h').
    - limit: Number of data points.
    - filename: Filename to save the plot image.
    """
    # Binance API endpoint for historical klines
    url = "https://api.binance.com/api/v3/klines"
    
    # Parameters for the API call
    params = {
        'symbol': symbol,
        'interval': interval,
        'limit': limit
    }
    
    # Make the API request
    response = requests.get(url, params=params)
    data = response.json()
    
    # Parse the response data
    dates = [datetime.fromtimestamp(item[0]/1000) for item in data]
    prices = [float(item[2]) for item in data]  # Closing prices
    
    # Plotting
    plt.figure(figsize=(9, 7))
    plt.plot(dates, prices, marker='o', linestyle='-', color='cyan')
    
    plt.title(f'{symbol} Price')
    plt.xlabel('Date')
    plt.ylabel('Price')
    
    # Adjust date formatting on the x-axis
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))  # Year-Month-Day
    plt.gca().xaxis.set_major_locator(mdates.DayLocator())  # One tick per day
    
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    # Ensure the directory exists
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    # Save the figure
    plt.savefig(filename)
    plt.close()
