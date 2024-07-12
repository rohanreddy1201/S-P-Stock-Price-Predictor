import pandas as pd
from sqlalchemy import create_engine
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Load historical stock data
df = pd.read_csv('all_stocks_5yr.csv')

# Preprocess data
df['date'] = pd.to_datetime(df['date'])
df.sort_values('date', inplace=True)
df['target'] = df.groupby('Name')['close'].shift(-1)
df.dropna(inplace=True)

# Filter for a specific stock, e.g., Apple (AAPL)
df = df[df['Name'] == 'AAPL']

X = df[['open', 'high', 'low', 'close', 'volume']]
y = df['target']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

# Build and train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse}')

# Function for real-time prediction
def predict_stock_price(new_data):
    prediction = model.predict(new_data)
    return prediction

# Save the model and other necessary objects if needed
import joblib
joblib.dump(model, 'stock_price_model.pkl')
