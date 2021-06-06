import re
import pickle
class CustomerProcessor:
    def __init__(self):
        self.logFile = open('log.txt')
        self.VIP_customer_dict = dict()
        self.customer_dict = dict()
        self.item_sale = dict()
        self.price = 0
        self.accumulate_price = 0
    def run(self):
        self.process()

        VIP_customer = self.show_VIPcustomer()
        customer = self.show_customer()
        item_sale = self.show_item_sale()
        print(VIP_customer)
        print(customer)
        print(item_sale)

        with open("Analysis_result.txt", "wb") as fp:
            pickle.dump(VIP_customer + customer + item_sale, fp)

    def process(self):
        for line in self.logFile:

            VIP_customer = re.findall("\[VIP\] (\S+) buys", line)
            if(len(VIP_customer)!=0): # 是 VIP 顧客
                if(VIP_customer[0] not in self.VIP_customer_dict):
                    self.VIP_customer_dict[VIP_customer[0]] = {}

                item = re.findall("buys (\S+)", line)
                
                price_with_dollarSign = re.findall("for (\S+)", line)
                self.price = re.findall("[0-9.]+", str(price_with_dollarSign))
                self.price = float(self.price[0])

                if(item[0] not in self.VIP_customer_dict[VIP_customer[0]]): #若先前顧客沒購買此項目
                    self.VIP_customer_dict[VIP_customer[0]][item[0]] = self.price

                else:   #若先前顧客有購買此項目
                    self.accumulate_price = self.VIP_customer_dict[VIP_customer[0]][item[0]]
                    self.accumulate_price = self.accumulate_price + self.price #累積金額
                    self.VIP_customer_dict[VIP_customer[0]][item[0]] = self.accumulate_price


                if(item[0] not in self.item_sale):
                    self.item_sale[item[0]] = self.price
                else:
                    self.item_sale_accumulate_price = self.item_sale[item[0]]
                    self.item_sale_accumulate_price = self.item_sale_accumulate_price + self.price
                    self.item_sale[item[0]] = self.item_sale_accumulate_price
                
                
            else:   # 非 VIP 顧客
                customer = re.findall("(\S+) buys", line)
                if(len(customer)!=0):
                    if(customer[0] not in self.customer_dict):
                        self.customer_dict[customer[0]] = {}
                
                    item = re.findall("buys (\S+)", line)
                    
                    price_with_dollarSign = re.findall("for (\S+)", line)
                    self.price = re.findall("[0-9.]+", str(price_with_dollarSign))
                    self.price = float(self.price[0])

                    if(item[0] not in self.customer_dict[customer[0]]): #若先前顧客沒購買此項目
                        self.customer_dict[customer[0]][item[0]] = self.price

                    else:   #若先前顧客有購買此項目
                        self.accumulate_price = self.customer_dict[customer[0]][item[0]]
                        self.accumulate_price = self.accumulate_price + self.price #累積金額
                        self.customer_dict[customer[0]][item[0]] = self.accumulate_price
 

                    if(item[0] not in self.item_sale):
                        self.item_sale[item[0]] = self.price
                    else:
                        self.item_sale_accumulate_price = self.item_sale[item[0]]
                        self.item_sale_accumulate_price = self.item_sale_accumulate_price + self.price
                        self.item_sale[item[0]] = self.item_sale_accumulate_price
            

    def show_VIPcustomer(self):
        PrintAll_VIP_customer = "\n==== VIP customer list ====\n"
        for VIP_customer_name, VIP_customer_info in self.VIP_customer_dict.items():
            PrintAll_VIP_customer += "\n\nName: " + VIP_customer_name
            for key in VIP_customer_info:
                PrintAll_VIP_customer += "   item:" + str(key) + " $" + str(VIP_customer_info[key])
        PrintAll_VIP_customer += "\n======================\n"

        return PrintAll_VIP_customer

    def show_customer(self):
        PrintAll_customer = "\n====  Member list (without VIP) ====\n"
        for customer_name, customer_info in self.customer_dict.items():
            PrintAll_customer += "\n\nName: " + customer_name
            for key in customer_info:
                PrintAll_customer += "   item:" + str(key) + " $" + str(customer_info[key])
        PrintAll_customer += "\n======================\n"

        return PrintAll_customer

    def show_item_sale(self):
        PrintAll_item_sale = "\n====  Total item sale list  ====\n"
        for item_sale_name, item_sale_info in self.item_sale.items():
            PrintAll_item_sale += "\n\nItem Name: " + item_sale_name
            PrintAll_item_sale += "   sales: $" + str(item_sale_info)
                
        PrintAll_item_sale += "\n======================\n"

        return PrintAll_item_sale

if __name__ == '__main__':
    customer_processor = CustomerProcessor()
    customer_processor.run()