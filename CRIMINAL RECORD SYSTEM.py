import mysql.connector
from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
import matplotlib.pyplot as plt

# Establishing connection to the database
mydb = mysql.connector.connect(host='localhost', user='root', password='TIRTHESH@3234')
mycursor = mydb.cursor()

# Creating database and tables if not exists
mycursor.execute("CREATE DATABASE IF NOT EXISTS CRIMINAL")
mycursor.execute("USE CRIMINAL")
mycursor.execute("""
CREATE TABLE IF NOT EXISTS CRIMINAL_BASICINFO(
    CRIMINAL_NO INTEGER(4),
    NAME VARCHAR(20),
    JAIL VARCHAR(20),
    STATE VARCHAR(20),
    YEARSOFPUNISHMENT INTEGER(4),
    CAUGHTYEAR INTEGER(5),
    CASE_TYPE VARCHAR(15),
    GENDER VARCHAR(8),
    DOB DATE,
    DEATH_PENALTY VARCHAR(3),
    ALIVE_OR_DEAD CHAR(5),
    NUMBER_OF_CASES INTEGER(3)
)""")

mycursor.execute("""
CREATE TABLE IF NOT EXISTS CRIMINAL_PHYSICALCLASSIFICATION(
    CRIMINAL_NO INT(4),
    HEIGHT INT(3),
    EYE_COLOUR VARCHAR(10),
    IDENTIFICATION_MARK VARCHAR(20),
    WEIGHT INT(4),
    HAIR_COLOUR VARCHAR(10)
)""")

# Function to add a criminal record
def addcriminalrecord():
    try:
        n = int(simpledialog.askinteger("Input", "Enter the number of records to store:", minvalue=1))
        for i in range(n):
            criminal_no = simpledialog.askinteger("Input", "Enter the Criminal Number:")
            criminal_name = simpledialog.askstring("Input", "Enter the Criminal's Name:")
            location = simpledialog.askstring("Input", "Enter the Jail Location:")
            state = simpledialog.askstring("Input", "Enter the State:")
            yp = simpledialog.askinteger("Input", "Enter the Years of Punishment:")
            caughtyear = simpledialog.askinteger("Input", "Enter the Year when caught:")
            casetype = simpledialog.askstring("Input", "Enter the Case Type:")
            gender = simpledialog.askstring("Input", "Enter Gender (Male/Female/Other):")
            birthdate = simpledialog.askstring("Input", "Enter Birth Date (YYYY-MM-DD):")
            deathpenalty = simpledialog.askstring("Input", "Given Death Penalty (Yes/No):")
            aod = simpledialog.askstring("Input", "Alive or Dead:")
            no_of_cases = simpledialog.askinteger("Input", "Enter the Number of Cases:")

            height = simpledialog.askinteger("Input", "Enter the Height of the Criminal (in cm):")
            eyecolour = simpledialog.askstring("Input", "Enter the Eye Colour:")
            im = simpledialog.askstring("Input", "Enter the Identification Mark:")
            weight = simpledialog.askinteger("Input", "Enter the Weight in kg:")
            haircolour = simpledialog.askstring("Input", "Enter the Hair Colour:")

            # Inserting records
            val1 = (criminal_no, criminal_name, location, state, yp, caughtyear, casetype, gender, birthdate, deathpenalty, aod, no_of_cases)
            val2 = (criminal_no, height, eyecolour, im, weight, haircolour)
           
            mycursor.execute("""
            INSERT INTO CRIMINAL_BASICINFO(CRIMINAL_NO, NAME, JAIL, STATE, YEARSOFPUNISHMENT, CAUGHTYEAR, CASE_TYPE, GENDER, DOB, DEATH_PENALTY, ALIVE_OR_DEAD, NUMBER_OF_CASES)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, val1)
           
            mycursor.execute("""
            INSERT INTO CRIMINAL_PHYSICALCLASSIFICATION(CRIMINAL_NO, HEIGHT, EYE_COLOUR, IDENTIFICATION_MARK, WEIGHT, HAIR_COLOUR)
            VALUES (%s, %s, %s, %s, %s, %s)
            """, val2)

        mydb.commit()
        messagebox.showinfo("Success", "Criminal record(s) added successfully!")

    except Exception as e:
        messagebox.showerror("Error", str(e))

# Function to search for a criminal record
def searchrecord():
    try:
        choice = simpledialog.askinteger("Input",
            "Search by:\n1. Criminal Number\n2. Name\n3. Jail\n4. State\n5. Height\n6. Identification Mark\n7. Hair Colour\n8. Caught Year",
            minvalue=1, maxvalue=8)

        if choice == 1:
            a = simpledialog.askinteger("Input", "Enter the Criminal Number:")
            mycursor.execute("SELECT * FROM CRIMINAL_BASICINFO WHERE CRIMINAL_NO=%s", (a,))
        elif choice == 2:
            a = simpledialog.askstring("Input", "Enter the Name:")
            mycursor.execute("SELECT * FROM CRIMINAL_BASICINFO WHERE NAME=%s", (a,))
        elif choice == 3:
            a = simpledialog.askstring("Input", "Enter the Jail:")
            mycursor.execute("SELECT * FROM CRIMINAL_BASICINFO WHERE JAIL=%s", (a,))
        elif choice == 4:
            a = simpledialog.askstring("Input", "Enter the State:")
            mycursor.execute("SELECT * FROM CRIMINAL_BASICINFO WHERE STATE=%s", (a,))
        elif choice == 5:
            a = simpledialog.askinteger("Input", "Enter the Height:")
            mycursor.execute("""
            SELECT * FROM CRIMINAL_BASICINFO
            INNER JOIN CRIMINAL_PHYSICALCLASSIFICATION ON CRIMINAL_BASICINFO.CRIMINAL_NO = CRIMINAL_PHYSICALCLASSIFICATION.CRIMINAL_NO
            WHERE CRIMINAL_PHYSICALCLASSIFICATION.HEIGHT = %s
            """, (a,))
        elif choice == 6:
            a = simpledialog.askstring("Input", "Enter the Identification Mark:")
            mycursor.execute("""
            SELECT * FROM CRIMINAL_BASICINFO
            INNER JOIN CRIMINAL_PHYSICALCLASSIFICATION ON CRIMINAL_BASICINFO.CRIMINAL_NO = CRIMINAL_PHYSICALCLASSIFICATION.CRIMINAL_NO
            WHERE CRIMINAL_PHYSICALCLASSIFICATION.IDENTIFICATION_MARK = %s
            """, (a,))
        elif choice == 7:
            a = simpledialog.askstring("Input", "Enter the Hair Colour:")
            mycursor.execute("""
            SELECT * FROM CRIMINAL_BASICINFO
            INNER JOIN CRIMINAL_PHYSICALCLASSIFICATION ON CRIMINAL_BASICINFO.CRIMINAL_NO = CRIMINAL_PHYSICALCLASSIFICATION.CRIMINAL_NO
            WHERE CRIMINAL_PHYSICALCLASSIFICATION.HAIR_COLOUR = %s
            """, (a,))
        elif choice == 8:
            a = simpledialog.askinteger("Input", "Enter the Caught Year:")
            mycursor.execute("SELECT * FROM CRIMINAL_BASICINFO WHERE CAUGHTYEAR=%s", (a,))

        results = mycursor.fetchall()
        result_str = "\n".join([str(record) for record in results])
        messagebox.showinfo("Search Results", result_str if results else "No records found.")

    except Exception as e:
        messagebox.showerror("Error", str(e))

# Main window setup
root = Tk()
root.title("Criminal Record System")

# UI buttons for each feature
btn_add = Button(root, text="Add Record", command=addcriminalrecord)
btn_add.pack(pady=10)

btn_search = Button(root, text="Search Record", command=searchrecord)
btn_search.pack(pady=10)

btn_exit = Button(root, text="Exit", command=root.quit)
btn_exit.pack(pady=10)

root.geometry("300x200")
root.mainloop()
