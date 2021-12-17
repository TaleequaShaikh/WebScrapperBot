import requests #obtain info from the url in the form of html
from bs4 import BeautifulSoup # use to parse that info
import time
import csv
import send_mail
from datetime import date

urls = ["https://finance.yahoo.com/quote/AMZN?p=AMZN&.tsrc=fin-srch", "https://finance.yahoo.com/quote/GOOG?p=GOOG&.tsrc=fin-srch", "https://finance.yahoo.com/quote/MSFT?p=MSFT&.tsrc=fin-srch"]
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'}

today = str(date.today()) + ".csv"
csv_file = open(today, "w") #write method
csv_writer = csv.writer(csv_file) # initiating writer i.e (csv_writer) & passing csv file
csv_writer.writerow(['Stock Name', 'Current Price', 'Previous Close', 'Open', 'Bid', 'Ask', 'Day Range', '52 Week Range', 'Volume', 'Avg. Volume' ])
 #creating our 1st heading row with 10 elements(stock_title,current_price , remaining 8 values from the for loop)



for url in urls:
    stock = []
    html_page = requests.get(url, headers=headers) # extract info of that page
    soup = BeautifulSoup(html_page.content, 'lxml') # creating soup object , lxml is parser
    

    header_info = soup.find_all("div", id="quote-header-info")[0] #find_all returns list, extracts header
    stock_title = header_info.find("h1").get_text()
    current_price = header_info.find("div", class_="My(6px) Pos(r) smartphone_Mt(6px)").find("span").get_text()
    stock.append(stock_title) # adding stock title in the empty list stock = []
    stock.append(current_price) # adding current price in the empty list stock = []

    table_info = soup.find_all("div", class_="D(ib) W(1/2) Bxz(bb) Pend(12px) Va(t) ie-7_D(i) smartphone_D(b) smartphone_W(100%) smartphone_Pend(0px) smartphone_BdY smartphone_Bdc($seperatorColor)")[0].find_all("tr")
    
    for i in range(0,8):
        value = table_info[i].find_all("td")[1].get_text()
        stock.append(value)


    csv_writer.writerow(stock)
    time.sleep(5)   

csv_file.close() 
send_mail.send(filename=today)    


