### Python Project made by Divya Jain,Prabhjot Singh Assi, Atharva Chavan.

import pandas as pd
import numpy as np
import sqlalchemy
import matplotlib.pyplot as plt


df = pd.DataFrame()

df_new = pd.DataFrame()
csv_file = "python.csv"
csv_output = "output.csv"
def read_csv_file():
    df=pd.read_csv(csv_file)
    print(df)



#name of function : clear
#purpose          : clear output screen
def clear ():
    for x in range (10):
        print()

def data_analysis_menu():
    df=pd.read_csv(csv_file)
    while True:
        clear()
        print('\n\nData Analysis Menu')
        print ('_'*100)
        print ('1. Show whole dataframe\n')
        print ('2. Show columns\n')
        print ('3. Show top rows\n')
        print ('4. Show bottom rows\n')
        print ('5. Show specific column\n')
        print ('6. Show specific Row(record)\n')
        print ('7. Add a new record\n')
        print ('8. Add new column\n')
        print ('9. Delete a column\n')
        print ('10. Delete a record\n')
        print ('11. Check for avablity\n')
        print ('12. Advance filtering\n')
        print ('13. Genre Wise books')
        print ('14. Data summary\n')
        print ('15. Export data)\n')
        print ('16. Exit (back to main menu\n')
        ch= int(input('Enter your choise: '))
        if ch==1:
            print(df)
            wait= input()
        elif ch==2:
            print(df.columns)
            wait= input()
        elif ch==3:
            n=int(input('Enter total rows you want to show: '))
            print(df.head(n))
            wait= input()
        elif ch==4:
            n=int(input('Enter total rows you want to show: '))
            print(df.tail(n))
            wait= input()
        elif ch==5:
            print(df.columns)
            col_name= input('Enter column Name that you want to print: ')
            print(df[col_name])
            wait=input()
        elif ch ==6 :
            print("Enter index no. of row that you what to see from 0-",len(df)-1)
            k= int(input(":"))
            print (df.iloc[k])
            wait =input()
            
        elif ch==7:
            a=input('Title :')
            b= input('Author : ')
            c= input('Genre : ')
            d= int(input('Total pg. : '))
            e= input('Publisher : ')
            f= float(input('Price : '))
            g= float(input('Rating : '))
            h= int(input('Currently available :'))
            i= int(input('Rented :'))
            df.loc[len(df)]=[a,b,c,d,e,f,g,h,i,h+i]
            print(df)
            wait=input()
        elif ch==8:
            col_name =input('Enter new column name: ')
            print()
            print ("Default value for  column ", col_name , " will be  1. string or 2. numeric  ")
            x= int(input(": "))
            if x == 1:
                col_value =  input('Enter default column value: ')
                 
            elif x == 2:
                col_value = eval (input('Enter default column value: '))
                
            else :
                print("Wrong input !! enter either 1 or 2 ")
            df[col_name]=col_value
            print(df)
            print('\n\nPress enter key to continue.... ')
            wait=input()
        elif ch==9:
            print(df.columns)
            col_name =input ('Enter column name to delete: ')
            del df [col_name]
            print(df)
            print('\n\nPress enter key  to continue.... ')
            wait = input()
        elif ch==10:
            print('Choose row index from 0 to',len(df)-1)
            index_no =int(input('Enter the index number that you want to delet: '))
            df=df.drop(index_no)
            print(df)
            print('\n\nPress any key to continue....')
            wait= input()
        elif ch ==11:
            print("Enter 1 to see all the  Currently avalable books ")
            print("Enter 2  to see all the Currently  unavalible books")
            r =int (input("Enter   your choice : "))
            if r==1:
                df1=df.loc[(df["Currently_available"]!=0),:]
                print(df1)
            elif r==2:
                df1=df.loc[(df["Currently_available"]==0),:]
                print(df1)
            else :
                print(' Wrong choice ')
            print('\n\nPress enter key to continue....')
            wait = input ()
            
        elif ch==12:
            print ("Advance fcatures menu")
            print ('_'*100)
            print ()
            print('1. Price wice sotrtting\n ')
            print('2. Rating wise sortting\n')
            print('3. Total no. of pages wise sortting \n')
            g= int (input("Enter  your choice : "))
            if g ==1:
                print("1. All books with  price  <= 300\n")
                print("2. All books with  price 300 > and  <= 600\n")
                print("3. All books with  price 600 > and <=1000\n")
                print("4. All books with  price  >1000 \n")
                print('5. Custom filtering.\n')
                h =int(input("Enter your choice : "))
                if h==1:
                    df1=df.loc[(df["Price"] <=300),:]
                    print(df1)
                elif h==2 :
                    df1=df.loc[(df["Price"] >300) & (df["Price"] <=600),:]
                    print(df1)
                elif h==3 :
                    df1=df.loc[(df["Price"] >600) & (df["Price"] <=1000),:]
                    print(df1)
                elif h==4:
                    df1=df.loc[(df["Price"] >1000),:]
                    print(df1)
                elif h==5:
                    print("\n\nThis will show all the books available in your Price range\n ")
                    y = float(input("Enter your min. Price : "))
                    z = float(input("Enter your max. Prince : "))
                    print()
                    df1=df.loc[(df["Price"] >=y) & (df["Price"] <=z),:]
                    print(df1)
                else :
                    print('Invalid Choice')
                    print('\n\nPress any key to continue....')
                    wait=input()
            elif g== 2:
                print("1. Books with high rating  (rating 4+)")
                print("2. Books with Avg. rating (rating 2.5-4)")
                print("3. Books with low rating  (rating 2.5>)")
                print("4. Custom Rating filter : ")
                i = int(input("Enter your choice : "))
                if i==1: 
                    df1=df.loc[(df["Rating"])>= 4 ,:]
                    print(df1)
                elif i==2:
                    df1=df.loc[(df["Rating"]>= 2.5) & (df["Rating"]< 4 ),:]
                    print(df1)
                elif i==3:
                    df1=df.loc[(df["Rating"]< 2.5 ),:]
                    print(df1)
                elif i==4:
                    m = float(input("Enter min. value  of Rating required : "))
                    n = float(input("Enter max. value  of Rating required : "))
                    df1=df.loc[(df["Rating"] >=  m ) & (df["Rating"]<= n ),:]
                    print(df1)
                else :
                    print ("Invalid Choice")
                wait=input()
            elif g==3 :
                print("1. Large books ( pg. >500)")
                print("2. Small books(pg. <500)")
                print("3. Custom filtring \n ")
                o=int(input("Enter your choice : "))
                if o == 1:
                    df1= df.loc[(df["Total_Pages"]>=500),:]
                    print(df1)
                    wait = input()
                elif o ==2 :
                    df1=df.loc[(df["Total_Pages"]<500),:]
                    print(df1)
                    wait = input()
                elif o==3:
                    p = int(input("Enter minimum value of pages : "))
                    q =int(input("Enter  maximum value of pages : "))
                    df1=df.loc[(df["Total_Pages"]>=p)& (df ["Total_Pages"]<=q)]
                    print(df1)
                    wait = input()
                else :
                    print("Invalid Choice ")
                    wait = input()
                
        elif ch==13 :
            print(df.loc[df["Genre"]])
            xyz=input("Enter the genre name that you want to view: ")
            print (df.loc[df["Genre"]==xyz])
            wait=input()
            
            
        elif ch==14:
           print(df.info())
           print('\n\nPress any key  to continue....')
           wait=input()
        elif ch ==15:
            df.to_csv(csv_output)
            print('\n\nCheck your new file at : ',csv_output)
            wait= input()
        
        elif ch==16:
            break
        
        
def graph():
    df=pd.read_csv(csv_file)
    while True:
        clear()
        print ('\nGraph Menu')
        print ('_'*100)
        print ("1. Line chart\n")
        print ("2. Bar chart\n")
        print ("3. Histogram\n")
        print ('4. Exit (back to manin menu)\n')
        ch =int(input("Enter your choice :"))
        if ch == 1:
            print("\n1. Price Graph")
            print("\n2. Currently_available and Rented Graph ")
            print("\n3. Custom Graphs ")
            u=int(input("Enter you choice: "))
            if u==1:
                plt.plot(df['Title'],df['Price'],marker ='o',color = 'black')
                plt.xticks(rotation="vertical")
                plt.show()
                wait=input()
            elif u == 2:
                plt.plot(df["Title"],df["Currently_available"],marker ="o")
                plt.plot(df["Title"],df["Rented"],marker ="D")
                plt.xlabel("Book Name")
                plt.ylabel("NO. of Books")
                plt.legend(["Currently_available","Rented"])
                plt.xticks(rotation= "vertical")
                plt.show()
                wiat=input()
            elif u==3:
                print(df.columns)
                j=input("Enter the column(s) name you want on x axis : ")
                k=input("Enter the column(s) name you want on y axis : ")
                if k == "Title":
                    plt.plot(df[j],df[k],marker= 'o')
                elif k=="Author":
                    plt.plot(df[j],df[k],marker= 'o')
                elif k=="Genre":
                    plt.plot(df[j],df[k],marker= 'o')
                elif k=="Total_Pages":
                    plt.plot(df[j],df[k],marker= 'o')
                elif k=="Publisher":
                    plt.plot(df[j],df[k],marker= 'o')
                elif k=="Price":
                    plt.plot(df[j],df[k],marker= 'o')
                elif k=="Rating":
                    plt.plot(df[j],df[k],marker= 'o')
                elif k=="Currently_available":
                    plt.plot(df[j],df[k],marker= 'o')
                elif k=="Rented":
                    plt.plot(df[j],df[k],marker= 'o')
                elif k=="Total":
                    plt.plot(df[j],df[k],marker= 'o')
                else :
                    print("Enter both the names of y axis 1 by 1")
                    k1=input('1. ')
                    k2=input('2. ')
                    plt.plot(df[j],df[k1],marker= 'o')
                    plt.plot(df[j],df[k2],marker= 'D')
                
                if j=='Title':
                    plt.xticks(rotation ='vertical')
                else :
                    plt.xticks(rotation='horizontal')
                plt.legend([k])
                plt.xlabel(j)
                plt.ylabel(k)
                plt.show()
                wait=input()
        elif ch == 2:
            plt.barh(df["Genre"] , df["Total"])
            plt.show()
            wait=input()
        elif ch == 3:
            plt.hist(df["Genre"],bins=11,color="r", edgecolor="yellow" , hatch="+")
            plt.show()
        
        

def export_menu():
    df=pd.read_csv(csv_file)
    while True:
        clear()
        print ('\n\nExport Menu')
        print ('_'*100)
        print ()
        print ('1. csv file\n')
        print ('2. MySQL table\n')
        print ('3. Exit(back  to main menu) ')
        ch =int(input('Enter your choice: '))
        if ch==1:
            df.to_csv(csv_output)
            print('\n\nCheck your new file at : ',csv_output)
            wait= input()
           
        elif ch==2:
            '''engine= sqlalchemy.create_engine('sql+pymysql://root:deepu6localhost:3306/pythonproject')
            df.to_sql(con-engine,index=False,if_exists= replace , name ='libery' )
            print('\n\nPlease check pythonproject database for libery.....')'''
            wait=input()
            
        elif ch== 3:
            break
                        

def main_menu():
    while True:
        print()
        print ('Main Menu')
        print ('_'*100)
        print ()
        print ('1. Read csv file\n')
        print ('2. Data Analysis Menu\n')
        print ('3. Graph Menu\n')
        print ('4. Export Data\n')
        print ('5. Exit\n')
        choice= int(input('Enter your choice: '))

        if choice == 1:
            read_csv_file()
            wait=input()
        elif choice == 2:
            data_analysis_menu()
            wait=input()
        elif choice == 3:
            graph()
            wait=input()
        elif choice == 4:
            export_menu()
            wait=input()
        else :
            break


#call your main menu
main_menu()
       
        




