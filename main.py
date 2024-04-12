import streamlit as st
from streamlit_option_menu import option_menu

# Importing specific apps
from apps.coin_comparison import display_crypto_comparison
from apps.coin_detail import display_cryptocurrency_details
from apps.digit_classifier import display_digit_classifier

# Setting page configuration with a dark theme
st.set_page_config(page_title="My Streamlit App", page_icon=":sparkles:", layout="wide")

# Define the main function that will contain our UI elements
def main():
    # Apply default Streamlit styles for a dark theme
    st.markdown(
        """
        <style>
        .st-bx {color: white;} /* Base text color */
        .st-bs {color: #FF4B4B;} /* Highlight color */
        .css-1v3fvcr {border-color: #666666;} /* Widget borders */
        </style>
        """,
        unsafe_allow_html=True
    )
    
    # Create a container to host the navigation menu
    with st.container():
        tab_selector = option_menu(
            menu_title="Applicatin Hub",
            options=["Crypto Tracker", "Digit Classifier"],
            icons=["wallet2", "cpu-fill"],
            menu_icon="cast",
            default_index=0,
            orientation="horizontal",
            styles={
                "container": {"padding": "5px"},
                "icon": {"color": "white", "font-size": "25px"},
                "nav-link": {"font-size": "18px", "text-align": "center", "margin": "0px", "color": "white", "border-radius": "0px"},
                "nav-link-selected": {"color": "white", "background-color": "#4CAF50", "border-radius": "5px"},
            }
        )

    # Decision block to handle different tabs
    if tab_selector == 'Crypto Tracker':
        detail_tab, comparison_tab = st.tabs(["Detailed View", "Comparison View"])
        
        with detail_tab:
            display_cryptocurrency_details()
        
        with comparison_tab:
            display_crypto_comparison()
    
    elif tab_selector == 'Digit Classifier':
        display_digit_classifier()

# Ensure that the application runs when executed as a script
if __name__ == "__main__":
    main()
