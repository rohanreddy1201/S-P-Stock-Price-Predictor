import streamlit as st
import pandas as pd
import requests
import joblib
import matplotlib.pyplot as plt

# Load the trained model
model = joblib.load('stock_price_model.pkl')

# Load the historical stock data to get the list of stock names
df = pd.read_csv('all_stocks_5yr.csv')
stock_names = df['Name'].unique()

def get_real_time_data(symbol, api_key):
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=1min&apikey={api_key}'
    response = requests.get(url)
    data = response.json()
    
    if 'Meta Data' not in data:
        return None, data.get('Note', 'Error: Could not fetch data.')

    time_series = data['Time Series (1min)']
    df = pd.DataFrame.from_dict(time_series, orient='index')
    df = df.astype(float)
    df.index = pd.to_datetime(df.index)
    
    # Get the latest data point
    last_refreshed = data['Meta Data']['3. Last Refreshed']
    latest_data = df.loc[last_refreshed]

    new_data = pd.DataFrame([{
        'open': latest_data['1. open'],
        'high': latest_data['2. high'],
        'low': latest_data['3. low'],
        'close': latest_data['4. close'],
        'volume': latest_data['5. volume']
    }])

    return new_data, df, None

def predict_stock_price(new_data):
    prediction = model.predict(new_data)
    return prediction

st.title('Real-Time Stock Market Predictor')

# Dropdown menu for stock selection
selected_stock = st.selectbox('Select a stock:', stock_names)

# Input for Alpha Vantage API key
api_key = st.text_input('Enter Alpha Vantage API key:')

if st.button('Predict'):
    real_time_data, stock_data, error_message = get_real_time_data(selected_stock, api_key)
    if error_message:
        st.error(error_message)
    else:
        prediction = predict_stock_price(real_time_data)
        st.write(f'Predicted Close Price: {prediction[0]}')

        # Display stock data for the last 24 hours
        st.subheader('Stock Performance Metrics and Trends (Last 24 Hours)')

        # Plot the closing prices
        fig, ax = plt.subplots()
        ax.plot(stock_data.index, stock_data['4. close'], label='Close Price')
        ax.set_xlabel('Time')
        ax.set_ylabel('Price')
        ax.set_title(f'{selected_stock} Closing Prices (Last 24 Hours)')
        ax.legend()
        fig.autofmt_xdate()  # Automatically format x-axis labels
        st.pyplot(fig)

        # Plot the volume
        fig, ax = plt.subplots()
        ax.bar(stock_data.index, stock_data['5. volume'])
        ax.set_xlabel('Time')
        ax.set_ylabel('Volume')
        ax.set_title(f'{selected_stock} Trading Volume (Last 24 Hours)')
        fig.autofmt_xdate()  # Automatically format x-axis labels
        st.pyplot(fig)
