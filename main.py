import streamlit as st
from streamlit_option_menu import option_menu

from apps.coin_comparison import display_crypto_comparison
from apps.coin_detail import display_cryptocurrency_details
from apps.digit_classifier import display_digit_classifier

st.set_page_config(page_title="My Streamlit App", page_icon=":sparkles:", layout="wide")

def main():
    with st.container():
        tab_selector = option_menu(
            menu_title="A00476511- Assignment",
            options=["Crypto Tracker", "Digit Classifier"],
            icons=["wallet2", "cpu-fill"],
            menu_icon="cast",
            default_index=0,
            orientation="horizontal",
            styles={
                "container": {"padding": "5px", "background-color": "#fafafa"},
                "icon": {"color": "black", "font-size": "25px"},
                "nav-link": {"font-size": "18px", "text-align": "center", "margin": "0px", "color": "black", "border-radius": "0px"},
                "nav-link-selected": {"background-color": "#808080", "border-radius": "5px"},
            }
        )

    if tab_selector == 'Crypto Tracker':
        detail_tab, comparison_tab = st.tabs(["Detailed View", "Comparison View"])

        with detail_tab:
            display_cryptocurrency_details()

        with comparison_tab:
            display_crypto_comparison()

    elif tab_selector == 'Digit Classifier':
        display_digit_classifier()

if __name__ == "__main__":
    main()
