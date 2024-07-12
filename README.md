# Real-Time Stock Market Predictor

## Introduction

The Real-Time Stock Market Predictor is a web application that predicts the closing price of a stock using historical data and real-time data fetched from the Alpha Vantage API. This project leverages machine learning techniques to analyze stock trends and provides a user-friendly interface for real-time predictions and visualizations.

## Need for Usage

With the increasing volatility in stock markets, investors and traders seek tools that can help them make informed decisions. The Real-Time Stock Market Predictor aims to:

- Provide real-time stock price predictions.
- Visualize recent stock performance metrics and trends.
- Enhance decision-making processes for investors and traders.

## Tech Stack Used

- **Python**: Core programming language for data processing and machine learning.
- **Pandas**: Data manipulation and analysis.
- **Scikit-Learn**: Machine learning library for model training and evaluation.
- **Streamlit**: Web framework for building the user interface.
- **Matplotlib**: Visualization library for plotting stock performance metrics.
- **Alpha Vantage API**: Source for real-time stock data.
- **Joblib**: Model serialization and deserialization.

## Features

- **Real-Time Predictions**: Predicts the closing price of a stock using real-time data.
- **User-Friendly Interface**: Streamlit-based web application for easy interaction.
- **Visualizations**: Displays stock performance metrics and trends for the last 24 hours.
- **Dropdown Menu**: Allows users to select from a list of stocks.
- **API Integration**: Fetches real-time data from the Alpha Vantage API.

## Future Enhancements

- **Expanded Model**: Incorporate more sophisticated machine learning models for better accuracy.
- **Additional Metrics**: Include more financial metrics and indicators for comprehensive analysis.
- **Portfolio Management**: Allow users to track and predict multiple stocks in a portfolio.
- **Historical Data Analysis**: Provide insights and trends over longer historical periods.
- **Notifications**: Alert users about significant changes in stock prices.

## How to Use

### Prerequisites

- Python 3.x installed on your system.
- A GitHub account.
- An Alpha Vantage API key.

### Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/real-time-stock-market-predictor.git
   cd real-time-stock-market-predictor
   ```

2. **Install the Required Libraries:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Add Your Alpha Vantage API Key:**
   Replace your_alpha_vantage_api_key in app.py with your actual API key.

## Running the Application:

1. **Train the Model Using Historical Data:**
   ```bash
   python stock_predictor.py
   ```

2. **Run the Streamlit App:**
   ```bash
   streamlit run app.py
   ```

3. **Access the App in Your Web Browser:**
   Open your web browser and go to 'http://localhost:8501'


## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request or open an Issue to improve the project.

## Contact
For any questions or feedback, please contact [ackrohan@gmail.com].
