
import urllib
import urllib2
import json
import requests
import time

currentBuyCycle = 7
buyCycle = 2
on = True

# count() 
countIOPlusUrl = ""
countIOMinusUrl = ""
r1 = ""
rf =""
count = ""
firstSplit=""
secoundSplit=""
strCount=""
intCount= 0


#check count.io
def count():
        

        countIOPlusUrl = "http://count.io/vb/smartthingsLaundry/rforgeon1+"

        countIOMinusUrl = "http://count.io/vb/smartthingsLaundry/rforgeon1-"

        #open and add to count
        r1 = requests.post(countIOPlusUrl)
    

        #open and subtract from count
        rf = requests.post(countIOMinusUrl)
        #print rf.text

        #convert to string
        count = str(rf.text);

        #parse out count
        firstSplit = count.split('"count":')
        secondSplit = firstSplit[1].split("}")
        strCount = secondSplit[0]
        #convert to int
        intCount = int(strCount)
        
        print "Current Count: "
        print intCount

        return intCount



#buy values
url = 'https://api.zinc.io/v0/order'
values = {
  "client_token": "XXXXXXXXXXXXXXXXXXX",
  "retailer": "amazon",
  "products": [{"product_id": "B00LN23HHM", "quantity": 1}],
  "max_price": 0,
  "shipping_address": {
    "first_name": "Bob",
    "last_name": "Builder",
    "address_line1": "2222 Mulberry Ln.",
    "address_line2": "",
    "zip_code": "95128",
    "city": "San Jose", 
    "state": "CA",
    "country": "US",
    "phone_number": "2087390043"
  },
  "is_gift": False,
  "gift_message": "Here's your package, Tim! Enjoy!",
  "shipping_method": "cheapest",
  "payment_method": {
    "name_on_card": "Bob Builder",
    "number": "1111111111111111",
    "security_code": "111",
    "expiration_month": 11,
    "expiration_year": 2021,
    "use_gift": False
  },
  "billing_address": {
    "first_name": "Bob", 
    "last_name": "Builder",
    "address_line1": "2222 Mulberry Ln.",
    "address_line2": "",
    "zip_code": "95128",
    "city": "San Jose", 
    "state": "CA",
    "country": "US",
    "phone_number": "2087390043"
  },
  "retailer_credentials": {
    "email": "bobBuilder7320@gmail.com",
    "password": "ilovemuffins"
  },
  "webhooks": {
    "order_placed": "http://mywebsite.com/zinc/order_placed",
    "order_failed": "http://mywebsite.com/zinc/order_failed",
    "tracking_obtained": "http://mywebsite.com/zinc/tracking_obtained"
  },
  "client_notes": {
    "our_internal_order_id": "abc123"
  }
}

data = ""
req = ""
response = ""
the_page = ""

#execute buy order
def buy():

        #place order with Zinc
        data = json.dumps(values)
        req = urllib2.Request(url, data, {'content-type': 'application/json'})
        response = urllib2.urlopen(req)
        the_page = response.read()

        #create new buy cycle
        global buyCycle
        global currentBuyCycle
        currentBuyCycle += buyCycle
        print the_page

#main
def main():
        while on:
                time.sleep(3)
                global buyCycle
                global currentBuyCycle
                print "currentBuyCycle: "
                print currentBuyCycle
                if count() == currentBuyCycle:
                        buy()
                        print "Order executed"
#Run Main
main()
