import pandas as pd
import datetime as dt 

start = dt.datetime(2021, 1, 1)
end = dt.datetime(2021,1, 15)

pdt = pd.date_range(start, end, freq='B')
f = open("url.ini", "r")
NSE_URL = f.readline().split('=')[1]
f.close()
try: 
  for dates in pdt:
    dd = dt.datetime.strftime(dates, "%d%b%Y").upper()
    mm = dt.datetime.strftime(dates, "%b").upper()
    year = dt.datetime.strftime(dates, "%Y")
    url_bhav = NSE_URL +year +'/'+mm+'/cm'+dd+'bhav.csv.zip'
    data = pd.read_csv(url_bhav)
    data = data[data['SERIES']=='EQ']
    print(len(data))
    result = data[['SYMBOL','TIMESTAMP','OPEN', 'HIGH','LOW','CLOSE','TOTTRDQTY','TOTALTRADES']]
    result.to_csv(dd+".txt", header=False, index=False)
    print("imported data for "+dd)
except Exception as e: 
  print("Error Occured "+ str(e))
  
print(NSE_URL)
