import streamlit as st

from apps.coin_comparison import display_crypto_comparison
from apps.coin_detail import display_cryptocurrency_details
from apps.digit_classifier import display_digit_classifier

def main():
    tab_selector = st.sidebar.radio("Select Application", ['Crypto Tracker', 'Digit Classifier'])

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
