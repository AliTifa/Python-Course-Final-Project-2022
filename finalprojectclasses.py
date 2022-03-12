# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 18:02:43 2022

@author: HP
"""

import mysql.connector
import numpy as np
import matplotlib.pyplot as plt


mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "root",
    database = 'ali'
    )
    
my_cursor = mydb.cursor()

class signup:
    
    def Signup(self):
        print('please insert the following data')
        name = input('first and last name: ')
        password = int(input('Password(should be a integer): '))
        country = input('Country: ')
        nation = input('Nationality: ') 
        Profession = input('Profession: ')
        favfood = input('Fav Food: ')
        favdrink = input('Fav Drink: ')
        hob = input('Hobby: ')
        x = 'INSERT INTO users (name,pass,country,nationality,profession,favfood,favdrink,hobbies) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)'
        a = (name,password,country,nation,Profession,favfood,favdrink,hob)
        
        my_cursor.execute("SELECT name FROM users")
        myresult = my_cursor.fetchall()
        arr = np.asarray(myresult)
        name_column = np.concatenate(arr)
        if name in name_column:
            print('This name already exist!')
        else:    
            my_cursor.execute(x,a)
            mydb.commit()
            print('Thank you, Your data have been added')

class login:    
    def Login(self):
    
        condition = 0 #condition to repeat a loop until the correct password is entered
        print('Enter the following')
        while(condition == 0):
            username = input('Name: ')
            passwd = int(input('Password (integer value): '))
            my_cursor.execute("SELECT name FROM users")
            myresult = my_cursor.fetchall()
            arr = np.asarray(myresult)
            name_column = np.concatenate(arr) #array of the name column
            
            row_num = 0 #counter to know which row number the person data are in
            
            
            for x in name_column:
                if username == x:
                    my_cursor.execute("SELECT pass FROM users ")
                    myresult = my_cursor.fetchall()
                    arr = np.asarray(myresult)
                    pass_column = np.concatenate(arr)
                    if passwd == pass_column[row_num]:
                        condition = 1
                        break
                    else:
                        print('Wrong Password,try again!')
                        break
                row_num = row_num+1   
                
            if username not in name_column:
                print('The Username doesnot exist, try again!')
        return username              
            
class visual:
    
    def datavis(self):
        cond = 0
        while(cond == 0):
            category = input('Enter the name of the category to visualize: \n 1. name \n 2. pass \n 3. country \n 4. nationality \n 5. profession \n 6. favfood \n 7. favdrink \n 8. hobbies \n 9. To Exit enter E \n ')
            if category == 'E': 
                break
            s = 'SELECT FROM users'
            m = s[:7] + category +' '+ s[7:]
            
            my_cursor.execute(m)
            myresult = my_cursor.fetchall()
            arr = np.asarray(myresult)
            country_column = np.concatenate(arr)
            bars = np.unique(country_column)
            height = []
            unique,counts = np.unique(country_column,return_counts=True)
            repeated_values = np.asarray((unique, counts)).T
            for i in range(0,len(bars)):
                height.append(int(repeated_values[i][1]))
            
            
            plt.bar(bars, height)
            plt.xticks(bars, rotation=45)
            plt.show()
        
class modifydata:
    
    def modify(self,name):
        while(1):
            category = input('Enter the name of the category to modify (to exist enter E): \n 1. name \n 2. pass \n 3. country \n 4. nationality \n 5. profession \n 6. favfood \n 7. favdrink \n 8. hobbies \n')
            if category == 'E':
                break
            new_value  = input('enter the update: ')
            if category == 'pass':
                s = "UPDATE users SET WHERE name = '' "
                m = s[:17] + category +' '+ '=' + new_value +' '+ s[17:31] + name + s[31:]
            else: 
                s = "UPDATE users SET '' WHERE name = '' "
                m = s[:17] + category +' '+ '=' + s[18:19]+ new_value + s[18:34] + name + s[34:]   
            
            my_cursor.execute(m)
            mydb.commit()
            print('Your data have been Modified \n')

class stats:
        
    def Stats(self,name):
        while(1):
            category = input('which category to show similarities? \n 1. country \n 2. nationality \n 3. profession \n 4. favfood \n 5. favdrink \n 6. hobbies \n 7. To Exit enter E \n' )
        
            if category == 'E':
                break
            else:
                mydict = {"country": 2,  "nationality": 3,"profession": 4,"favfood": 5, "favdrink": 6,"hobbies": 7  }
                s = "SELECT * FROM users WHERE name = ''"
                m = s[:34] + name +s[34:]
                my_cursor.execute(m) 
                myresult = my_cursor.fetchall()
                arr = np.asarray(myresult)
                user_row_data = np.concatenate(arr) #array of the entire row of the data of the user
                user_value = user_row_data[mydict[category]] #this is the value which the user what to compare    
                
                
                s = "SELECT * FROM users WHERE ''"
                m = s[:26] + category + ' '+ '=' +s[27:28]+ user_value +s[27:]
                my_cursor.execute(m)
                myresult2 = my_cursor.fetchall()
                
                print('There are '+str(len(myresult2))+ ' users who have the same '+ category+' as you \n')
                
        
        
        
        