import pyupbit
import sqlite3
import datetime

def date_range(start,end):
    start = datetime.datetime.strptime(start,"%Y-%m-%d")
    start = start+datetime.timedelta(days=1)
    end=datetime.datetime.strptime(end,"%Y-%m-%d")
    end=end+datetime.timedelta(days=1)
    dates=[(start+datetime.timedelta(days=i)).strftime("%Y-%m-%d") for i in range((end-start).days+1)]
    return dates

dates = date_range("2025-02-05","2025-03-05")

print(dates)

for day in reversed(dates):
    myDay=day+' 00:00'
    print(myDay)

    ticker='KRW-BTC'
    interval='minute1'
    to=myDay
    count=1440
    price_now=pyupbit.get_ohlcv(ticker=ticker,interval=interval,to=to,count=count)

    print(price_now)

    db_path=r"C:\2025ncc\2025ncc\#25_cryptoDB\coin.db"
    con=sqlite3.connect(db_path,isolation_level=None)
    price_now.to_sql('BTC',con,if_exists='append')

    con.close