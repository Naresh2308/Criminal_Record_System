import mysql.connector
import matplotlib.pyplot as plt
mydb=mysql.connector.connect(host='localhost',user='root',password='TIRTHESH@3234')
mycursor=mydb.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS CRIMINAL")
mycursor.execute("use criminal")
sqls=("CREATE TABLE IF NOT EXISTS CRIMINAL_BASICINFO(CRIMINAL_NO INTEGER(4),NAME VARCHAR(20),JAIL VARCHAR(20),STATE VARCHAR(20),YEARSOFPUNISHMENT INTEGER(4),CAUGHTYEAR INTEGER(5),CASE_TYPE VARCHAR(15),gender varchar(8),DOB DATE,DEATH_PENALTY VARCHAR(3),ALIVE_OR_DEAD CHAR(5),NUMBER_OF_CASES INTEGER(3))")
mycursor.execute(sqls)
sqlstmnt1=("CREATE TABLE IF NOT EXISTS CRIMINAL_PHYSICALCLASSIFICATION(CRIMINAL_NO INT(4),HEIGHT INT(3),EYE_COLOUR VARCHAR(10),IDENTIFICATION_MARK VARCHAR(20),WEIGHT INT(4),HAIR_COLOUR VARCHAR(10))")
mycursor.execute(sqlstmnt1)

#FUNCTION TO ADD CRIMINAL RECORD
def addcriminalrecord():
    val1=[]
    val2=[]
    n=int(input("\nenter the number of records to be stored"))
    for i in range(n):
        criminal_no=int(input("\n\nENTER THE CRIMINAL NUMBER:"))
        criminal_name=input("\nENTER THE CRIMINALS NAME:")
        location=input("\nENTER THE NAME OF THE JAIL:")
        state=input("\nENETR THE STATE:")
        yp=int(input("\nENTER THE YEARS OF PUNISHMENT:"))
        caughtyear=input("\nENTER THE YEAR IN WHICH THE CRIMINAL WAS CAUGHT:")
        casetype=input("\nENTER THE CASE TYPE:")
        gender=input("\nENTER THE GENDER(MALE/FEMALE/OTHER):")
        birthdate=input("\nENTER THE DATE ON WHICH THE CRIMINAL WAS BORN IN THE FORMAT(YYYY/MM/DD):")
        deathpenalty=input("\nENTER WEITHER THE CRIMINAL IS GIVEN DEATH PENALTY OR NOT IN YES OR NO FORMAT:")
        aod=input("\nENTER WEITHER THE CRIMINAL IS ALIVE OR DEAD:")
        no_of_cases=int(input("\nENTER THE NUMBER OF CASES:"))
    for j in range(n):
        criminal_no=int(input("\n\nENTER THE CRIMINAL NUMBER:"))
        height=int(input("\nENTER THE HEIGHT OF THE CRIMINAL:"))
        eyecolour=input("\nENTER THE EYECOLOUR:")
        im=input("\nENTER THE IDENTIFICATION MARK ON THE CRIMINAL:")
        weight=int(input("\nENTER THE WEIGHT IN kg:"))
        haircolour=input("\nENTER THE HAIR COLOUR:")
    val1.append((criminal_no,criminal_name,location,state,yp,caughtyear,casetype,gender,birthdate,deathpenalty,aod,no_of_cases))
    val2.append((criminal_no,height,eyecolour,im,weight,haircolour))
    sql=('''INSERT INTO CRIMINAL_BASICINFO(CRIMINAL_NO,NAME,JAIL,STATE,YEARSOFPUNISHMENT,CAUGHTYEAR,CASE_TYPE,gender,DOB,DEATH_PENALTY,ALIVE_OR_DEAD,NUMBER_OF_CASES) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)''')
    mycursor.executemany(sql,val1)
    sql2=('''INSERT INTO CN(CRIMINAL_NO,NAME,JAIL,STATE,YEARSOFPUNISHMENT,CAUGHTYEAR,CASE_TYPE,gender,DOB,DEATH_PENALTY,ALIVE_OR_DEAD,NUMBER_OF_CASES) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)''')
    mycursor.executemany(sql2,val1)
    sql1=('''INSERT INTO CRIMINAL_PHYSICALCLASSIFICATION(CRIMINAL_NO,HEIGHT,EYE_COLOUR,IDENTIFICATION_MARK,WEIGHT,HAIR_COLOUR) VALUES(%s,%s,%s,%s,%s,%s)''')
    mycursor.executemany(sql1,val2)
    mydb.commit()
    
#FUNCTION TO SEARCH FOR RECORD
def searchrecord():
    n2=int(input("\n\n1. SEARCH BY CRIMINAL NUMBER\n\n2. SEARCH BY NAME\n\n3. SEARCH BY JAIL\n\n4. SEARCH BY STATE\n\n5. SEARCH BY HEIGHT\n\n6. SEARCH BY IDENTIFICATION MARK\n\n7. SEARCH BY HAIR COLOUR\n\n8. SEARCH BY CAUGHT DATE\n\nENTER YOUR CHOICE:"))
    if n2==1:
        a=int(input("\n\nENTER THE CRIMINAL NUMBER:"))
        b=(a,)
        cn=("SELECT * FROM CRIMINAL_BASICINFO WHERE CRIMINAL_NO=%s")
        mycursor.execute(cn,b)
        y=mycursor.fetchall()
        for i in y:
            print(i)
    if n2==2:
        a=input("\n\nENTER THE NAME:")
        b=(a,)
        na=('''SELECT * FROM CRIMINAL_BASICINFO WHERE NAME=%s''')
        mycursor.execute(na,b)
        z=mycursor.fetchall()
        for k in z:
            print(k)
    if n2==3:
        a=input("\n\nENTER THE NAME OF THE JAIL:")
        b=(a,)
        j=("SELECT * FROM CRIMINAL_BASICINFO WHERE JAIL=%s")
        mycursor.execute(j,b)
        z=mycursor.fetchall()
        for k in z:
            print(k)
    if n2==4:
        i=input("\n\nENTER THE STATE:")
        a=(i,)
        k=("SELECT * FROM CRIMINAL_BASICINFO WHERE STATE=%s")
        mycursor.execute(k,a)
        z=mycursor.fetchall()
        for k in z:
            print(k)
    if n2==5:
        i=input("\n\nENTER THE HEIGHT:")
        a=(i,)
        k=("SELECT * FROM CRIMINAL_BASICINFO,CRIMINAL_PHYSICALCLASSIFICATION WHERE CRIMINAL_PHYSICALCLASSIFICATION.HEIGHT=%s")
        mycursor.execute(k,a)
        z=mycursor.fetchall()
        for k in z:
            print(k)
    if n2==6:
        i=input("\n\nENTER ANY IDENTIFICATION MARK:")
        a=(i,)
        k=("SELECT * FROM CRIMINAL_BASICINFO,CRIMINAL_PHYSICALCLASSIFICATION WHERE CRIMINAL_PHYSICALCLASSIFICATION.IDENTIFICATION_MARK=%s")
        mycursor.execute(k,a)
        z=mycursor.fetchall()
        for k in z:
            print(k)
    if n2==7:
        i=input("\n\nENTER THE HAIR COLOUR:")
        a=(i,)
        k=("SELECT * FROM CRIMINAL_BASICINFO,CRIMINAL_PHYSICALCLASSIFICATION WHERE CRIMINAL_PHYSICALCLASSIFICATION.HAIR_COLOUR=%s")
        mycursor.execute(k,a)
        z=mycursor.fetchall()
        for k in z:
            print(k)
    if n2==8:
        i=int(input("\n\nENTER THE CAUGHT YEAR:"))
        a=(i,)
        k=("SELECT * FROM CRIMINAL_BASICINFO WHERE CAUGHTYEAR=%s")
        mycursor.execute(k,a)
        z=mycursor.fetchall()
        for k in z:
            print(k)
            
#FUNCTION TO ANALYZE THE RECORD
def analysis():
    n=int(input("\n\nENTER 1 TO GET THE INFORMATION ABOUT NUMBER OF CASES IN EACH JAIL\nENTER 2 TO GET THE NUMBER OF CASES IN DIFFERENT YEARS\nENTER 3 TO GET THE NUMBER OF PRISONERS IN A PARTICULAR JAIL\nENTER 4 TO GET THE INFORMATION ABOUT THE NUMBER OF WOMEN AND MEN CRIMINALS\nENTER 5 TO GET THE INFORMATION ABOUT THE NUMBER OF CRIMES IN EACH STATE\nENTER 6 TO GET THE INFORMATION ABOUT NUMBER OF CASES OF EACH TYPE"))
    if n==1:
        x=mycursor.execute("SELECT COUNT(*),jail FROM CN GROUP BY JAIL")
        i=mycursor.fetchall()
        lst=[]
        for k in i:
            print(k)
        for k in i:
            for y in k:
                lst.append(y)
        p=0
        pl=[]
        t=1
        tl=[]
        slices=[]
        labels=[]
        while p<len(lst):
            pl.append(p)
            tl.append(t)
            p+=2
            t+=2
        for i in pl:
            slices.append(lst[int(i)])
        for z in tl:
            labels.append(lst[int(z)])
        plt.pie(slices,labels=labels)
        plt.title("JAIL WISE CRIMINALS PIE")
        plt.show()
        
    if n==2:
        x=mycursor.execute("SELECT COUNT(*),caughtyear FROM CN GROUP BY CAUGHTYEAR")
        i=mycursor.fetchall()
        lst=[]
        for k in i:
            print(k)
        for k in i:
            for y in k:
                lst.append(y)
        p=0
        pl=[]
        t=1
        tl=[]
        slices=[]
        labels=[]
        while p<len(lst):
            pl.append(p)
            tl.append(t)
            p+=2
            t+=2
        for i in pl:
            slices.append(lst[int(i)])
        for z in tl:
            labels.append(lst[int(z)])
        plt.pie(slices,labels=labels)
        plt.title("YEAR WISE CRIMINALS PIE")
        plt.show()
        
    if n==3:
        j=input("\n\nENTER THE NAME OF THE JAIL:")
        k=(j,)
        x=("SELECT COUNT(*) FROM CN WHERE JAIL=%s") 
        m=mycursor.execute(x,k)
        b=mycursor.fetchone()
        for i in b:
            print('NUMBER OF PRISONERS IN',j,'IS:',i)
    if n==4:
        x=mycursor.execute("SELECT COUNT(*) FROM CN WHERE GENDER='MALE'")
        i=mycursor.fetchone()
        for c in i:
            print("\nNUMBER OF MALE PRISONERS:",c)
        a=mycursor.execute("SELECT COUNT(*) FROM CN WHERE GENDER='FEMALE'")
        b=mycursor.fetchone()
        for d in b:
            print("\nNUMBER OF FEMALE PRISONERS:",d)
        m=mycursor.execute("SELECT COUNT(*) FROM CN WHERE GENDER='OTHER'")
        n=mycursor.fetchone()
        for f in n:
            print("\nNUMBER OF OTHER PRISONERS:",f)
        slices=[c,d,f]
        labels=['MALE','FEMALE','OTHER']
        plt.pie(slices,labels=labels)
        plt.title("GENDER WISE CRIMINALS PIE")
        plt.show()
    if n==5:
        x=mycursor.execute("SELECT COUNT(*),STATE FROM CN GROUP BY STATE")
        i=mycursor.fetchall()
        lst=[]
        for k in i:
            print(k)
        for k in i:
            for y in k:
                lst.append(y)
        p=0
        pl=[]
        t=1
        tl=[]
        slices=[]
        labels=[]
        while p<len(lst):
            pl.append(p)
            tl.append(t)
            p+=2
            t+=2
        for i in pl:
            slices.append(lst[int(i)])
        for z in tl:
            labels.append(lst[int(z)])
        plt.pie(slices,labels=labels)
        plt.title("STATE WISE CRIMINALS PIE")
        plt.show()
    if n==6:
        x=mycursor.execute("SELECT COUNT(*),CASE_TYPE FROM CN GROUP BY CASE_TYPE")
        i=mycursor.fetchall()
        lst=[]
        for k in i:
            print(k)
        for k in i:
            for y in k:
                lst.append(y)
        p=0
        pl=[]
        t=1
        tl=[]
        slices=[]
        labels=[]
        while p<len(lst):
            pl.append(p)
            tl.append(t)
            p+=2
            t+=2
        for i in pl:
            slices.append(lst[int(i)])
        for z in tl:
            labels.append(lst[int(z)])
        plt.pie(slices,labels=labels)
        plt.title("CASE TYPE WISE CRIMINALS PIE")
        plt.show()

#TO DELETE A RECORD
def delete():
    cn=int(input("\nENTER THE CRIMINAL NUMBER OF WHOSE RECORD IS TO BE DELETED"))
    c=(cn,)
    mycursor.execute("CREATE table if not exists CN  as select * from CRIMINAL_BASICINFO")
    x=("DELETE FROM CN WHERE CRIMINAL_NO=%s")
    mycursor.execute(x,c)
    mydb.commit()
    print("\n\nRECORD HAS BEEN DELETED SUCCESSFULLY") 

#TO MODIFY THE RECORD   
def modify():
    nm=int(input("\n\n1. TO MODIFY ALIVE OR DEAD:\n2. TO MODIFY NUMBER OF CASES:\n3. TO MODIFY NAME OF THE JAIL:\n4. TO MODIFY GIVEN DEATH PENALTY OR NOT:\n5. TO MODIFY  YEARS OF PUNISHMENT\n6. TO MODIFY CASETYPE\n\nENTER YOUR CHOICE:"))
    if nm==1:
        z=int(input("\nENTER THE CRIMINAL NUMBER WHOSE RECORD IS TO BE EDITED"))
        x=input("\nENTER ALIVE OR DEAD:")
        
        y="UPDATE CN SET ALIVE_OR_DEAD='{}' WHERE CRIMINAL_NO={}".format(x,z)
        mycursor.execute(y)
        a="UPDATE CRIMINAL_BASICINFO SET ALIVE_OR_DEAD='{}' WHERE CRIMINAL_NO={}".format(x,z)
        mycursor.execute(a)
        mydb.commit()
    if nm==2:
        z=int(input("\nENTER THE CRIMINAL NUMBER WHOSE RECORD IS TO BE EDITED"))
        x=input("\nENTER NUMBER OF CASES:")
        
        y="UPDATE CN SET NUMBER_OF_CASES={} WHERE CRIMINAL_NO={}".format(x,z)
        mycursor.execute(y)
        a="UPDATE CRIMINAL_BASICINFO SET NUMBER_OF_CASES={} WHERE CRIMINAL_NO={}".format(x,z)
        mycursor.execute(a)
        mydb.commit()
    if nm==3:
        z=int(input("\nENTER THE CRIMINAL NUMBER WHOSE RECORD IS TO BE EDITED"))
        x=input("\nENTER NAME OF THE JAIL:")
        
        y="UPDATE CN SET JAIL='{}' WHERE CRIMINAL_NO={}".format(x,z)
        mycursor.execute(y)
        a="UPDATE CRIMINAL_BASICINFO SET JAIL='{}' WHERE CRIMINAL_NO={}".format(x,z)
        mycursor.execute(a)
        mydb.commit()
    if nm==4:
        z=int(input("\nENTER THE CRIMINAL NUMBER WHOSE RECORD IS TO BE EDITED"))
        x=input("\nENTER DEATH PENALTY GIEVN OR NOT(YES/NO):")
        
        y="UPDATE CN SET DEATH_PENALTY='{}' WHERE CRIMINAL_NO={}".format(x,z)
        mycursor.execute(y)
        a="UPDATE CRIMINAL_BASICINFO SET DEATH_PENALTY='{}' WHERE CRIMINAL_NO={}".format(x,z)
        mycursor.execute(a)
        mydb.commit()
    if nm==5:
        z=int(input("\nENTER THE CRIMINAL NUMBER WHOSE RECORD IS TO BE EDITED"))
        x=int(input("\nENTER YEARS OF PUNISHMENT:"))
        
        y="UPDATE CN SET YEARSOFPUNISHMENT={} WHERE CRIMINAL_NO={}".format(x,z)
        mycursor.execute(y)
        a="UPDATE CRIMINAL_BASICINFO SET YEARSOFPUNISHMENT={} WHERE CRIMINAL_NO={}".format(x,z)
        mycursor.execute(a)
        mydb.commit()
    if nm==6:
        z=int(input("\nENTER THE CRIMINAL NUMBER WHOSE RECORD IS TO BE EDITED"))
        x=input("\nENTER CASETYPE:")
        
        y="UPDATE CN SET CASE_TYPE='{}' WHERE CRIMINAL_NO={}".format(x,z)
        mycursor.execute(y)
        a="UPDATE CRIMINAL_BASICINFO SET CASE_TYPE='{}' WHERE CRIMINAL_NO={}".format(x,z)
        mycursor.execute(a)
        mydb.commit()
    
        
print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("                *******************************************************CRIMINAL RECORD SYSTEM*****************************************************                 ")
print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------")

while True:
    n=int(input("1. ADD RECORDS\n\n2. SEARCH FOR RECORDS\n\n3. ANALYZE THE DATA\n\n4. DELETE A RECORD\n\n5. MODIFY A RECORD\n\n0. EXIT\n\n\nENTER YOUR CHOICE:"))
    if n==1:
            password=input("\nENTER THE PASSWORD")
            if password=="123456":
                print("\nYOU HAVE ENTERED THE RIGHT PASSWORD")
                addcriminalrecord()
                print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                print("                *******************************************************RECORD ADDED SUCCESSFULLY*****************************************************                 ")
                print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------")
            else:
                print("\nwrong password entered")
                break
                
    if n==2:
        password=input("\nENTER THE PASSWORD")
        if password=="123456":
                print("\nYOU HAVE ENTERED THE RIGHT PASSWORD")
                searchrecord()
        else:
                print("\nwrong password entered")
                break
    if n==3:
        password=input("\nENTER THE PASSWORD")
        if password=="123456":
                print("\nYOU HAVE ENTERED THE RIGHT PASSWORD")
                analysis()
        else:
                print("\nwrong password entered")
                break
    if n==4:
        password=input("\nENTER THE PASSWORD")
        if password=="123456":
                print("\nYOU HAVE ENTERED THE RIGHT PASSWORD")
                delete()
        else:
                print("\nwrong password entered")
                break
    if n==5:
        password=input("\nENTER THE PASSWORD")
        if password=="123456":
                print("\nYOU HAVE ENTERED THE RIGHT PASSWORD")
                modify()
        else:
                print("\nwrong password entered")
                break
        
    if n==0:
        print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        print("                *******************************************************THANK YOU FOR USING THE PROGRAM*****************************************************                 ")
        print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        break
        
        
        
        
            
        
        
        


        
        
