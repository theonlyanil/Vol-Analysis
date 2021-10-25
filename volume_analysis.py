"""
    Volume Analysis Micro App
    (streamlit)

    by Anil Sardiwal
"""

import streamlit as st
import pandas as pd
import yahfin.yahfin as yf
from datetime import date, timedelta
st.write("""
    # Volume Analysis
    """)
symbol = st.text_input("Symbol", "ITC")
sym = yf.Symbol(symbol + ".NS")

st.header("Select Period & Interval")
start_date = st.date_input('Start Date')
end_date = st.date_input('End Date')
interval = st.selectbox("Choose Interval",
            ('1m','2m','5m','15m','30m','60m','90m','1h','1d','5d','1wk','1mo','3mo'))


df = sym.history(start=start_date, end=end_date, interval=interval)
df = df.fillna(0)
df


# Takes in open and close price series (cols), and the volume column.
# Does a simple check - if close is greater than open, price went up. Bought.
# And opposit for Sold.
# Outputs cumulative bought and sold volumes in an array
def vol_analyse(open_series, close_series, volume_series):
    bought_vol = 0
    sold_vol = 0
    for index, volume in enumerate(volume_series):
        # Green
        if open_series[index] < close_series[index]:
            bought_vol = bought_vol + volume
        # Red
        else:
            sold_vol = sold_vol + volume

    return [bought_vol, sold_vol]

[bought, sold] = vol_analyse(df['Open'], df['Close'], df['Volume'])
st.text(f"Bought: {bought}")
st.text(f"Sold: {sold}")
st.text(f"Net: {bought-sold}")

st.write('### Made by Anil Sardiwal')
