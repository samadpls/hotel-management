#!/usr/bin/env python
# coding: utf-8

# In[ ]:



#           *HOTEL MANAGEMENT*
file = open("D:\hotel\management.txt", "r")
data=[]
#data from file each line in making a dict and all dic are adding in list
for line in file:
    d={}   
    b=line.strip().split(",")
    b.pop()
    for i in range(len(b)):
        if i%2==0:
            d[b[i]]=b[i+1]
    data.append(d)
print(data)      
# global variable that will use below    
lstvalue=[]
name=''
code=''
chk_in=''
chk_out=''
Cdata=''
total=0
num=0
price_bed=0
password=''
stay_days=0
#for booking
def booking():
    
    global name
    global lstvalue
    global chk_in
    global stay_days
    
    name=input("Name ")
    
    phone=int(input("Phone number \n"))
    chk_in = input('Enter check in date(dd-mm-yyyy): \n') 
    stay_days=int(input("enter the number of days you want to stay: \n"))
    
    lstvalue.append(name)
    lstvalue.append(phone)
    lstvalue.append(chk_in)

    roominfo()
#roominfo
def roominfo():
    
    global stay_days
    global data
    global Cdata
    global price_bed
    global lstvalue
    global total
    
    print ("=====We have the rooms available for you======:-")
    print()


    print ("First enter number of Beds you want in your Room:")
    print()
    bed=input("Bed--> ")
    print()

    for index in range(len(data)):
        if data[index]['bed']==str(bed):

            if data[index]['booking']=="False":
                data[index]['booking']='True'

                price_bed=1000*int(bed)

                print("RS.",price_bed, " price per night")
            
                break
               
            else:
                print(bed,"Bed are not available")
                roominfo()

    Cdata=data
    #bill
    total=price_bed*stay_days

    print("Your total is ", total)

    print("----------------------------")

    print(""" Cancel booking anytime by typing "Yes" """)
    print()

    cancel=input("Want to Cancel? ")

    if cancel=="Yes":
        lstvalue.clear()
   
    



    payment()
def payment():
    global lstvalue
    global Cdata

    print("         ====Payment====")
    print()
    print(" --------------------------------"*2)
    print()
    print("    ----MODE OF PAYMENT-----")
    print("Press the respective number for the service you want to avail: ")

    print(" 1- Credit/Debit Card")
    print(" 2- Online")
    print(" 3- Cash")
    x=int(input("-> "))
    if x==1:
        acc=input("----Account number-- ")
        code=input("----Code-- ")
        if acc!="" and code!="":
            print(" \t\t\t\t\t--Payment has been made--")
        else:
            print("---Acount or Code is invalid---")
            payment()
    elif x==2:
        paypal=input("--Your paypal account---")
        if paypal!="":
            print("--Payment has been made--")
        else:
            print("==Info is invalid==")
    elif x==3:
        print("--Payment has been made--")
    
    print("TO ACCESS ROOM SERVICES YOU NEED TO REMEMBER YOUR PASSWORD")
    
    #password
    print()
    password=str(input("Set password----> "))
    
    password=password.lower()
    #encrypyting
    alphabet='abcdefghijklmnopqrstuvwxyz'
    Epass=''
    for p in password:
        for i in range(len(alphabet)):
            if p==alphabet[i]:
                if i<22:
                    Epass+=alphabet[i+3]
                elif i>=22:
                    Epass+=alphabet[25-i]
    lstvalue.append(Epass)
    
    #record saving
   
    lstkey=['name','phonenumber','chkin',"password"]
    dic={}
    for i in range(len(lstkey)):
        for j in range(len(lstvalue)):
            if i==j:
                dic[lstkey[i]]=lstvalue[j]
                
    #writing the customer data            
    infile = open('D:\\test\\customer.txt', 'a')
    for key,value in dic.items():
        char=key+","+str(value)+","
        infile.write(char)
    infile.write('\n')
    infile.close()  

    #re writing the changed data 
    file = open("D:\hotel\management.txt", "w")
    for dic in Cdata:
        char=''
        for key,value in dic.items():
            char=key+","+value+","
            file.write(char)
        file.write('\n')
    file.close()   

              
    home()
    
def checkout():
    #asking user to enter thier checkout date
    global chk_out
    global chk_in
    global lstvalue
    
    chk_out=input("Check out date(dd-mm-yy): ")
    
    chkI=chk_in.split('-')
    chkO=chk_out.split('-')
    day1=int(chkI[0])
    day2=int(chkO[0])
    mon1=int(chkI[1]) #converting string in int form
    mon2=int(chkO[1])
    year1=int(chkI[2])
    year2=int(chkO[2])
    
    
    
    #checking the either date is incorrect or not
    if mon1>mon2:
        print(' YOU ENTERED A WRONG MONTH ')
        checkout()
    if mon1==mon2:
        totalDays=day2-day1
  
    elif mon2>mon1:
        
        if mon2 in [1,3,5,7,8,10,12]:
            mon_diff=mon2-mon1
            days=mon_diff*31
            totalDays=days+day1
        
        elif mon2 in [4,6,9,11]:
            mon_diff=mon2-mon1
            days=mon_diff*30
            totalDays=days+day1
            
    elif mon2==2:
        mon_diff=mon2-mon1
        days=mon_diff*28
        totalDays=days+day1    
    if year1>year2:
        print(' YOU ENTERED A WRONG year')
        checkout()
    #checking if the difference 
    
    if stay_days<totalDays:
        xtr=totalDays-stay_days
        fine=150*xtr+price_bed*xtr
        print("Pay the following amount:---------",fine)
    else:
        exit()    



def roomservice():
    
    password=str(input("Enter password"))
    infile = open('D:\\test\\customer.txt', 'r')
    content=infile.read()
    infile.close()
    
    #decrypting
    alphabet='abcdefghijklmnopqrstuvwxyz'
    Epass=''
    for p in password:
        for i in range(len(alphabet)):
            if p==alphabet[i]:
                if i<22:
                    Epass+=alphabet[i+3]
                elif i>=22:
                    Epass+=alphabet[25-i]
    if Epass in content:
        
    
        print("----------------------------"*3)
        print("   What room serives would you like to get during your stay ?")
        print ("We have the following room services for you:-")
        print ('''Click a number to continue:- \n
        1)\t ROOM CLEANING--------2000 Rs\n
        2)\tDRY CLEANING--------3000 Rs\n
        3)\tFOOD ORDER--------10000 Rs\n''')
        #taking order
        
        n=int(input("Enter a number "))
        if n==1:
            price=200
            print("KINDLY PAY THE FOLLOWING AMOUNT")
            print("ROOM CLEANING--------",price," Rs")
            print("Your room will be cleaned soon\n THANK YOU FOR USING THE SERVICE")
            
        elif n==2:
            price=300
            print("KINDLY PAY THE FOLLOWING AMOUNT")
            print("Dry cleaning--------",price," Rs")
            print('''Your clothes will be dry cleaned soon and will be ready as soon as possible\n 
                  THANK YOU FOR USING THE SERVICE''')
            
        elif n==3:
            print ("We have the following food items for you:-")
            print("Press the respective number for the service you want to avail: ")
            print ("1. BREAKFAST----;700")
            print ("2. LUNCH----;1000")
            print ("3. DINNER----;1500")
            food=int(input("enter the number "))
            if food==1:
                price=700
                print("KINDLY PAY THE FOLLOWING AMOUNT")
            
            elif food==2:
                price=1000
                print("KINDLY PAY THE FOLLOWING AMOUNT")
                
            else:
                price=1500

                print("KINDLY PAY THE FOLLOWING AMOUNT")
                print("Order Food--------",price," Rs")
                
            
    else:
        print("Wrong Password")
        roomservice()
    home()
def record():
    print("       ONLY MANAGMENT CAN ACESS THIS")
    username='admin'
    password="myrasamad"
    user=str(input("Enter username"))
    pas=str(input('Enter password'))
    if user==username and pas==password:
        file = open('D:\\test\\customer.txt', 'r')
        content=file.read()
        print(content)
    else:
        print("Wrong Passswor\n Try again")
        record()
    home()    
def exit():
    #wrting the customer  chkout information
    global lstvalue
    global chk_out
    
    infile = open('D:\\test\\customer.txt', 'a')
    name='name'
    chk='chkout'
    char=name+','+lstvalue[0]+','+chk+','+chk_out
    infile.write(char)
    print('===='*5)
    print("             .....THANK YOU FOR VISTING ......")
    print("               ...visit again soon...🥰")
    print('===='*5)
def home():
    print("\t \t \t \t WELCOME TO MS HOTEL \n")
    
    print("\t \t \t \tPress the respective number for the service you want to avail: ")
    print()
    print('\t \t \t \t 1 Booking \n ',
    '\t \t \t \t 2 Room service \n ','\t \t \t \t 3 Checkout\n','\t \t \t \t 4 Record\n',' \t \t \t \t 0 EXIT \n')
    
    n=int(input("->"))
    if n==1:
        print(" ")
        booking()
    elif n==2:
        print(" ")
        roomservice()
    elif n==3:
        print(" ")
        checkout() 
    elif n==4:
        print(" ")
        record()     
    elif n==0:
        exit()
home()

