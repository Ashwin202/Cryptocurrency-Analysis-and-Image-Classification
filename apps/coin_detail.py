import streamlit as st
import pandas as pd
import plotly.graph_objs as go
from lib.coin_detail_fn import fetch_coins_list, fetch_historical_price_data, plot_historical_prices, display_price_extremes

def display_cryptocurrency_details():
    """Display details and historical price chart of a cryptocurrency."""
    st.title('Cryptocurrency Details App')

    # Fetch the list of all coins
    all_coins = fetch_coins_list()
    coin_names = [coin['name'] for coin in all_coins]

    # User input for cryptocurrency selection
    default_coin_index = coin_names.index('Bitcoin') if 'Bitcoin' in coin_names else 0
    selected_coin = st.selectbox('Select the cryptocurrency:', options=coin_names, index=default_coin_index).lower()
    selected_coin_id = next((coin['id'] for coin in all_coins if coin['name'].lower() == selected_coin), None)

    if selected_coin_id:
        # Fetch historical price data for the selected coin
        historical_data = fetch_historical_price_data(selected_coin_id)
        if historical_data:
            price_data = pd.DataFrame(historical_data, columns=['timestamp', 'price'])
            price_data['date'] = pd.to_datetime(price_data['timestamp'], unit='ms')
            
            # Plot historical price data if available
            if not price_data.empty:
                plot_historical_prices(selected_coin, price_data)
                # Display maximum and minimum prices
                display_price_extremes(price_data)
            else:
                st.error("No price data available for the selected cryptocurrency.")
        else:
            st.error("Failed to fetch historical data.")
    else:
        st.info("Please select a valid cryptocurrency name.")

if __name__ == "__main__":
    display_cryptocurrency_details()
