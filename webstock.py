from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import csv

def checkstock(name):

    url = 'http://www.settrade.com/C04_02_stock_historical_p1.jsp?txtSymbol='+name+'&ssoPageId=10&selectPage=2'

    webopen = uReq(url)
    page_html = webopen.read()
    webopen.close()

    page_soup = soup(page_html, "html.parser")

    #print(page_soup)

    x = page_soup.findAll('div',{'class':'col-xs-6'})
    y = page_soup.findAll('span',{'class':'stt-remark'})

    
    
    
    #print(x)
    #print(x[2].text)

    price = float(x[2].text)
    sname = x[0].text
    dttext = y[0].text
    dtext = dttext[-19:]

    return price, sname, dtext



stockname = []
stockprice = []
stockdate = []
#-------------------------------------
price_ptt, name_ptt, date_ptt = checkstock('PTT')
stockname.append(name_ptt)
stockprice.append(price_ptt)
stockdate.append(date_ptt)

print("{} Price: {:.2f} baht".format(name_ptt,price_ptt))
print("Update: {}".format(date_ptt))
print("----------------------")
#-------------------------------------
price_tmb, name_tmb, date_tmb = checkstock('TMB')
stockname.append(name_tmb)
stockprice.append(price_tmb)
stockdate.append(date_tmb)
print("{} Price: {:.2f} baht".format(name_tmb,price_tmb))
print("Update: {}".format(date_tmb))
print("----------------------")
#-------------------------------------
def writecsv():
    filename = 'stockprice.csv'
    with open(filename, 'a' , newline='') as file:
        fw = csv.writer(file)
        
        for s,p,sd in zip(stockname,stockprice,stockdate):
            data = []
            data.append(s)
            data.append(p)
            data.append(sd)
            fw.writerow(data)

    print("CSV File saved. stockprice.csv")

writecsv()
