import streamlit as st
import datetime
import pyupbit

d=st.date_input(
    "날짜를 선택하세요.",
    datetime.date.today())

st.write('bitcoin daily chart')

ticker='KRW-BTC'
interval='minute60'
to=str(d+datetime.timedelta(days=1))
count=24
price_now= pyupbit.get_ohlcv(ticker=ticker,interval=interval,to=to,count=count)

st.line_chart(price_now.close)
#streamlit run C:\2025ncc\2025ncc\#29_streamlit\streamlit_2.py