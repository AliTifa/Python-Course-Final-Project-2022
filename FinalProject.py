# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""    

import finalprojectclasses as fp

"""
#Connect SQL to Python
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "root",
    database = 'ali'
    )
my_cursor = mydb.cursor()

#creating a table and insert with initial data 

my_cursor.execute('CREATE TABLE users (name VARCHAR(255) PRIMARY KEY, pass INTEGER(32), country VARCHAR(255), nationality VARCHAR(255), profession VARCHAR(255),favfood VARCHAR(255),favdrink VARCHAR(255),hobbies VARCHAR(255))')

x = 'INSERT INTO users (name,pass,country,nationality,profession,favfood,favdrink,hobbies) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)'

user1 = ('Ali',123,'Egypt','Egypt','physicist','Pizza','Tea','Football')
user2 = ('Electron',123,'England','England','Physicist','Bread-','Beer-','Dancing-')
user3 = ('Positron',123,'England','England','Physicist','Bread+','Beer+','Dancing+')
user4 = ('proton',123,'Germany','Germany','Chemist','Fish','Cola','Singing')
user5 = ('neutron',123,'Germany','Germany','Chemist','Chips','Soda','Decaying')
user6 = ('Z boson',123,'USA','USA','Particle Physicist','Pasta','Orange juice','Weak interaction')
user7 = ('W+ boson',123,'Italy','Italy','Particle Physicist','Pasta+','Apple juice+','Weak interaction+')
user8 = ('W- boson',123,'Italy','Italy','Particle Physicist','Pasta-','Apple juice-','Weak interaction-')

a = [user1,user2,user3,user4,user5,user6,user7,user8]

for i in a: 
        my_cursor.execute(x,i)
        mydb.commit()    
"""  




while (1):
    
    print('Choose from the following (write the word not the number): \n 1. Login \n 2. Signup \n 3. to Close the program enter E')
    choice = input()
    
    if choice == 'Login':
        z = fp.login()
        name = z.Login()
        print('welcome '+ name +'\n') 
        while (1):
            print('What do you want to do?\n 1. Data Visualisation = DV \n 2. Modify Data = MD \n 3. Search Similar values = SV \n 4. to Exit enter E')
            task = input()
            if task == 'DV':
                z = fp.visual()
                z.datavis()
            elif task == 'MD':            
                z = fp.modifydata()
                z.modify(name)
            elif task == 'SV':
                z = fp.stats()
                z.Stats(name)
            elif task == 'E':
                    break                          
    elif choice == 'Signup':
        z = fp.signup()
        z.Signup()            
                
    elif choice == 'E':
        break

    elif choice == 'E' : 
        break
