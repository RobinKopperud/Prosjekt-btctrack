import os
from tracker import plot_crypto_ticker
from datetime import datetime
from flask import Flask, render_template, jsonify, request, url_for, session, redirect

# Secret key setup
# It's better to set the secret key on the app configuration directly

# Adjust the paths accordingly
template_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../webFront')
static_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../static')

app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

app.secret_key = os.urandom(24)


# Dummy credentials for demonstration purposes
# In a real application, use a secure method for handling and storing passwords
VALID_USERNAME = 'admin'
VALID_PASSWORD = 'password'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Validate credentials
        if username == VALID_USERNAME and password == VALID_PASSWORD:
            session['logged_in'] = True
            return redirect(url_for('index'))
        else:
            return "Invalid username or password", 403
    
    return render_template('login.html')

@app.route('/')
def index():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('web.html')

@app.route('/get_chart')
def get_chart():
    try:
        symbol = request.args.get('symbol',)
        interval = request.args.get('interval')
        limit = request.args.get('limit', type=int)
        
        # Validation example (You can expand upon this based on your needs)
        if not symbol or not interval or not limit:
            raise ValueError("Missing required parameters.")
        
        filename = f'{static_dir}/images/{symbol.lower()}_price_chart.png'
        
        plot_crypto_ticker(symbol, interval, limit, filename)
        
        chart_url = url_for('static', filename=f'images/{symbol.lower()}_price_chart.png')
        
        return jsonify({'status': 'success', 'chartUrl': chart_url})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})


if __name__ == '__main__':
    app.run(debug=True)
