import requests
import pandas as pd
import joblib

# Load the trained model
model = joblib.load('stock_price_model.pkl')

def get_real_time_data(symbol, api_key):
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=1min&apikey={api_key}'
    response = requests.get(url)
    data = response.json()

    last_refreshed = data['Meta Data']['3. Last Refreshed']
    latest_data = data['Time Series (1min)'][last_refreshed]

    new_data = pd.DataFrame([{
        'open': float(latest_data['1. open']),
        'high': float(latest_data['2. high']),
        'low': float(latest_data['3. low']),
        'close': float(latest_data['4. close']),
        'volume': int(latest_data['5. volume'])
    }])

    return new_data

def predict_stock_price(new_data):
    prediction = model.predict(new_data)
    return prediction

if __name__ == "__main__":
    api_key = 'Enter your alpha vantage api key'
    symbol = 'AAPL'

    real_time_data = get_real_time_data(symbol, api_key)
    prediction = predict_stock_price(real_time_data)
    print(f'Predicted Close Price: {prediction[0]}')


    #WDP2TU4CMU42BYR3