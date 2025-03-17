import pyupbit
import sqlite3

ticker ='KRW-BTC'
interval = 'minute1'
to = '2025-03-05 09:20'
count = 20000
price_now = pyupbit.get_ohlcv(ticker=ticker,interval=interval,to=to,count=count)

db_path=r"C:\2025ncc\2025ncc\#25_cryptoDB\coin.db"

con=sqlite3.connect(db_path,isolation_level=None)
price_now.to_sql('BTC',con,if_exists='append')

con.close