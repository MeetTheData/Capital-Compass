import streamlit as st
import sidebar as comp
import stockTools as tools
import default
import portfolio
import model

st.set_page_config(
    page_title="Capital Compass",
    page_icon="🧭",
    layout="wide"
)

tools.remove_white_space()

st.title("Dynamic Risk Analysis for Your Portfolio")

comp.load_sidebar()

if "load_portfolio_check" not in st.session_state:
    st.session_state["load_portfolio_check"] = False

if "run_simulation_check" not in st.session_state:
    st.session_state["run_simulation_check"] = False

if not st.session_state.load_portfolio_check:
    default.load_page()

elif not st.session_state.run_simulation_check and st.session_state.load_portfolio_check:
    portfolio.load_page()

elif st.session_state.run_simulation_check:
    model.load_page()