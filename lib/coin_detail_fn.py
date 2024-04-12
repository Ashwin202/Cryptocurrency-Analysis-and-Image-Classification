from utils.crypto_utils import fetch_all_coins_list, fetch_historical_data, unix_to_datetime
import pandas as pd
import plotly.graph_objs as go
import streamlit as st
def fetch_coins_list():
        response = fetch_all_coins_list()
        return response if response is not None else []

def fetch_historical_price_data(coin_id):
    response = fetch_historical_data(coin_id, 365)
    return response if response is not None else {}

def plot_historical_prices(coin_name, price_data):
    """Plots the historical price data of a cryptocurrency."""
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=price_data['date'], y=price_data['price'], mode='lines', name='Price'))
    fig.update_layout(title=f'{coin_name.capitalize()} Price Chart (Last Year)', xaxis_title='Date', yaxis_title='Price in USD')
    st.plotly_chart(fig, use_container_width=True)
    
def display_price_extremes(price_data):
    """Displays the maximum and minimum prices on Streamlit columns."""
    max_price = price_data['price'].max()
    min_price = price_data['price'].min()
    max_date = price_data.loc[price_data['price'].idxmax()]['date']
    min_date = price_data.loc[price_data['price'].idxmin()]['date']

    col1, col2 = st.columns(2)
    col1.metric("Maximum Price", f"${max_price:.3f}", f"On {max_date.strftime('%Y-%m-%d')}")
    col2.metric("Minimum Price", f"${min_price:.3f}", f"On {min_date.strftime('%Y-%m-%d')}", delta_color="inverse")
    
def create_coin_selection_box(key, coins_dict, label='Select cryptocurrency:'):
    """Create a selection box for choosing a cryptocurrency."""
    index = 0 if key == 'coin1' else 1
    return st.selectbox(label, options=list(coins_dict.keys()), format_func=lambda x: coins_dict[x], index=index, key=key)

def load_and_prepare_data(coin_id, days):
    """Fetch and prepare cryptocurrency data for plotting."""
    data = fetch_historical_data(coin_id, days)
    if data:
        df = pd.DataFrame(data, columns=['timestamp', 'price'])
        df['date'] = df['timestamp'].apply(unix_to_datetime)
        return df
    return pd.DataFrame()