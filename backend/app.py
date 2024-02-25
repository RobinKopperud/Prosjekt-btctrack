from flask import Flask, render_template, jsonify, request, url_for
import os
from tracker import plot_crypto_ticker
from datetime import datetime

# Adjust the paths accordingly
template_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../webFront')
static_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../static')

app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

@app.route('/')
def index():
    return render_template('web.html')

@app.route('/get_chart')
def get_chart():
    symbol = request.args.get('symbol',)
    interval = request.args.get('interval')
    limit = request.args.get('limit', type=int)

    # Filename based on symbol for uniqueness
    filename = f'{static_dir}/images/{symbol.lower()}_price_chart.png'
    
    # Generate chart
    plot_crypto_ticker(symbol, interval, limit, filename)
    
    # Construct the URL for the generated chart image
    chart_url = url_for('static', filename=f'images/{symbol.lower()}_price_chart.png')
    
    return jsonify({'status': 'success', 'chartUrl': chart_url})

if __name__ == '__main__':
    app.run(debug=True)
