import pandas as pd
import numpy as np
import random as rnd
import smtplib
from GoogleConnect import Get_GSheet_Values

#Get_GSheet_Values()
df = pd.read_csv(r'path\to\csv\Secret.csv')

print(df)

names = df['Name']
names = list(names)
print(names)

items = df['Wish List Items']
items = list(items)
print(items)

email = df['Email address']
email = list(email)
print(email)

family = dict(zip(names,email))
wishItem = dict(zip(names,items))

rnd.shuffle(names)

recvr = []
for k in range(-1, len(names)-1):
    print(names[k])
    recvr.append(names[k])

print(names)
print(recvr)

Santa = []
Reciever = []
Item = []
for i in range(0, len(names)):     
    recieverEmail = family[names[i]]
    msg = '\n Hi %s ! You are buying a gift for %s . They requested for a %s . \n\n' % (names[i], recvr[i], wishItem[recvr[i]])
    print()
    print(str(msg))
    print()
    Santa.append( names[i] )
    Reciever.append ( recvr[i] )
    Item.append ( wishItem[recvr[i]])

    to = recieverEmail
    fromUser = '<EMAIL ID>'
    fromUser_pwd = '<PASSWORD>' 

    smtpserver = smtplib.SMTP("smtp.gmail.com",587)

    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.login(fromUser, fromUser_pwd)

    header = 'To: ' + to + '\n' + 'From: ' + fromUser + '\n' + 'Subject: Secret Santa for Christmas 2020! \n'
    print (header)

    msg = header + msg

    smtpserver.sendmail(fromUser, to, msg)
    print ('Email sent to ' + to)

    smtpserver.close()

print(Santa, Reciever, Item)
secretSanta = {'Santa':Santa, 'Reciever':Reciever, 'Item':Item}
print(secretSanta)
newDF = pd.DataFrame(secretSanta)
print(newDF)
newDF.to_csv(r'path\to\csv\Santa.csv')