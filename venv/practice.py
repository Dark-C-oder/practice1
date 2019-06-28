import random

import mysql.connector

class dbHelper():


    def saveCustomerInDB(self,customer):

        sql = f"insert into Customer values(null, '{customer.name}', '{customer.phone}', '{customer.email}',{customer.loyalty_pts},{customer.uid})"

        con = mysql.connector.connect(user = "root", password = "", host = "127.0.0.1", database = "dark_c_oder")

        cursor = con.cursor()
        cursor.execute(sql)

        con.commit()

        print("details of customer saved!!!!!!!!")


    def updateCustomerInDB(self,customer):

        sql = f"update Customer set name = '{customer.name}', email = '{customer.email}', phone = '{customer.phone}' where cid = {customer.cid}"

        con = mysql.connector.connect(user = "root", password = "", host = "127.0.0.1", database = "dark_c_oder")

        cursor = con.cursor()
        cursor.execute(sql)

        con.commit()

        print("details of customer UPDATED!!!!!!!!")

    def deleteCustomerInDB(self, cid):
        sql = f"delete from customer where cid = {cid}"

        con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="dark_c_oder")

        cursor = con.cursor()
        cursor.execute(sql)

        con.commit()

        print(f"details of customerID {cid} Deleted!!!!!!!!")

    def fetchAllCustomers(self):

        sql = "select * from Customer order by name desc"

        con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="dark_c_oder")

        cursor = con.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()



    def fetchCustomer(self, uid):
        sql = "select * from Customer where uid = {}".format(uid)

        con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="dark_c_oder")

        cursor = con.cursor()
        cursor.execute(sql)

        row = cursor.fetchone()
        print(row)





class customer():
    def __init__(self, name, phone, email, loyalty_pts,uid):
        self.name = name
        self.phone = phone
        self.email = email
        self.loyalty_pts = loyalty_pts
        self.uid = uid

    def showCustomerDetails(self):
        print(f"Name  : {self.name}")
        print(f"Phone : {self.phone}")
        print(f"Email : {self.email}")
        print(f"UID = {self.uid}")

print("1.  Add Customer Details!!!")

print("2. Already a Customer!!!")



choice = int(input("Enter your Choice : "))

if choice == 1:

    cRef = customer(None, None,None,100,None)
    cRef.name = input("Enter name of the customer : ")
    cRef.phone = input("Enter phone of the customer : ")
    cRef.email = input("Enter email of the customer : ")
    cRef.uid = random.randrange(1000,10000)


    save = input("Do you want to save the details of the customer (yes/no): ")
    if save == "yes":

        db = dbHelper()
        db.saveCustomerInDB(cRef)
        print("*****CONGRATULATIONS YOU HAVE BEEN GIVEN 100 Loyalty Points*********")
        print("")
        cRef.showCustomerDetails()
        #loyalty points assign

#=========================================================================================
if choice == 2:
    uid = int(input("Enter your unique Customer id : "))
    print("3.  Update Customer Details!!")
    print("4. Delete the customer Details")
    print("5.  shoe all customer!!!!")
    print("6.  Shopping")

    second_choice = int(input("Enter your Second Choice: "))



    if second_choice == 3:
        db = dbHelper()

        cRef = customer(None, None, None,None,None)
        db.fetchCustomer(cRef.uid)
        cRef.name = input("Enter name of the customer : ")
        cRef.phone = input("Enter phone of the customer : ")
        cRef.email = input("Enter email of the customer : ")

        save = input("Do you want to update the details (yes/no): ")
        if save == "yes":
            db = dbHelper()
            db.updateCustomerInDB(cRef)

    if second_choice == 4:



        save = input("Do you want to Delete the details (yes/no): ")
        if save == "yes":
            db = dbHelper()
            db.deleteCustomerInDB(cid)

    if second_choice == 5:
        db = dbHelper()
        db.fetchAllCustomers()

    if second_choice == 6:

        pass


 #======================================================================================





