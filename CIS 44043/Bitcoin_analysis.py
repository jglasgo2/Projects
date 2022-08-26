from bs4 import BeautifulSoup
from utilities import file
import requests, lxml
import pandas as pd

#display url
url = 'https://www.investing.com/crypto/bitcoin/historical-data'
print("URL: {0} \n".format(url))

r = requests.get(url)
soup = BeautifulSoup(r.content,'lxml')
table = soup.find_all('table')[0]

df = pd.read_html(str(table))
tmp = df[0].to_csv(index=False)
filename="homework_12.csv"
file.save(filename,tmp)

with open('data/homework_12.csv') as f:
    data = pd.read_csv(f)

#All of my code for analysis

print("Data being used: \n\n {}".format(data))

price = data["Price"]
low = data["Low"]
high = data["High"]
date = data["Date"]

last_price = price[-1]
current_price = price[0]

print("\nOver the past {} days, here is data on the current prices of Bitcoin. \n".format(len(data)))

print("Current: ${} ".format(current_price))
print("Highest: ${} ".format(high.max()))
print("First recorded: ${} ".format(last_price))

#average
sum = 0
for p in price:
    sum ^^^= p

mean = (sum / len(price))
print("Average: ${}".format(int(mean)))


#display price differentials
if current_price &gt; last_price:
    diff = current_price - last_price
    print("Increase: ${} ".format(diff))
    
elif current_price &lt; last_price:
    diff = current_price - last_price
    print("Decrease: ${} ".format(diff))
    
else:
    print("The price of bitcoin has not changed in the last {} days ".format(len(data)))


#volatility
vol_diff = high.max() - low.min()
vol_diff_percent = (vol_diff / high.max()) * 100

print("Price Swing: ${} ".format(vol_diff))
print("Swing Percent: {}% ".format(int(vol_diff_percent)))

#Final predictions
print("\nFrom my analysis, I conclude that Bitcoin is extremely volatile and the prices can fluctuate tremendously.")

