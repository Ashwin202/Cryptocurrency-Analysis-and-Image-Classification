import streamlit as st
import pandas as pd
import plotly.graph_objs as go
from utils.crypto_utils import fetch_all_coins_list, fetch_historical_data, unix_to_datetime
from lib.coin_detail_fn import create_coin_selection_box, load_and_prepare_data


def display_crypto_comparison():
    st.title('Cryptocurrency Comparison App')

    coins_list = fetch_all_coins_list()
    coins_dict = {coin['id']: coin['name'] for coin in coins_list}

    coin1_id = create_coin_selection_box('coin1', coins_dict, 'Select the first cryptocurrency:')
    coin2_id = create_coin_selection_box('coin2', coins_dict, 'Select the second cryptocurrency:')

    if coin1_id == coin2_id:
        st.error('Please select two different cryptocurrencies for comparison.')
        return

    time_frames = {'1 week': 7, '1 month': 30, '1 year': 365}
    selected_time_frame = st.selectbox('Select time frame:', options=list(time_frames.keys()))
    days = time_frames[selected_time_frame]

    coin1_df = load_and_prepare_data(coin1_id, days)
    coin2_df = load_and_prepare_data(coin2_id, days)

    if not coin1_df.empty and not coin2_df.empty:
        plot_comparison_chart(coin1_df, coin2_df, coins_dict, coin1_id, coin2_id, selected_time_frame)
    else:
        st.error('Could not fetch data for the selected cryptocurrencies.')

def plot_comparison_chart(coin1_df, coin2_df, coins_dict, coin1_id, coin2_id, time_frame):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=coin1_df['date'], y=coin1_df['price'], mode='lines', name=coins_dict[coin1_id], yaxis='y1'))
    fig.add_trace(go.Scatter(x=coin2_df['date'], y=coin2_df['price'], mode='lines', name=coins_dict[coin2_id], yaxis='y2'))

    fig.update_layout(
        title=f'Price Comparison: {coins_dict[coin1_id]} vs {coins_dict[coin2_id]} over {time_frame}',
        xaxis_title='Date',
        yaxis=dict(title=f'{coins_dict[coin1_id]} Price in USD', side='left'),
        yaxis2=dict(title=f'{coins_dict[coin2_id]} Price in USD', side='right', overlaying='y', showgrid=False),
        legend=dict(x=0.05, y=1.1, orientation='h')
    )
    st.plotly_chart(fig, use_container_width=True)

if __name__ == "__main__":
    display_crypto_comparison()
