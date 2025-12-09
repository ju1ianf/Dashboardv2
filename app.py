import streamlit as st
import yfinance as yf
import plotly.express as px

st.title("F1 Dashboard – Daily Metrics")

ticker = st.text_input("Enter Ticker Symbol", "AAPL")

@st.cache_data
def load_data(symbol):
    stock = yf.Ticker(symbol)
    hist = stock.history(period="1y")
    info = stock.info
    return hist, info

if ticker:
    hist, info = load_data(ticker)

    st.subheader(f"{ticker} Price History (1Y)")
    fig_price = px.line(hist, x=hist.index, y="Close", title="Daily Close Price")
    st.plotly_chart(fig_price, use_container_width=True)

    if "regularMarketPrice" in info and "trailingEps" in info and info["trailingEps"]:
        current_pe = info["regularMarketPrice"] / info["trailingEps"]
        st.metric("Current P/E Ratio", f"{current_pe:.2f}")

    st.subheader("Daily Volume")
    fig_vol = px.bar(hist, x=hist.index, y="Volume", title="Daily Volume")
    st.plotly_chart(fig_vol, use_container_width=True)
