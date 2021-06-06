import re
import pickle
hand = open('log.txt')
price_list = list()
item_list = list()


VIP_customer_dict = dict()
customer_dict = dict()

for line in hand:

    VIP_customer = re.findall("\[VIP\] (\S+) buys", line)
    #customer = re.findall("(\S+) buys", line)
    if(len(VIP_customer)!=0): #是 VIP 顧客
        VIP_customer_dict[VIP_customer[0]] = {}
    else:   #非VIP
        customer = re.findall("(\S+) buys", line)
        if(len(customer)!=0):
            customer_dict[customer[0]] = {}

    item = re.findall("buys (\S+)", line)
    item_list.append(item[0])
    
    price_with_dollarSign = re.findall("for (\S+)", line)
    price = re.findall("[0-9.]+", str(price_with_dollarSign))
    price = float(price[0])
    price_list.append(price)

print(VIP_customer_dict)
print(customer_dict)
