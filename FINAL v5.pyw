# Admin Login
# Username: admin     Password: admin123
from tkinter import *
from tkinter import messagebox   
import sqlite3
from datetime import date
from datetime import time 
from datetime import datetime
from PIL import ImageTk, Image
import db_operations as db
import Admin_db_operations as adb

from tkinter import Tk, Canvas, YES, BOTH, NW
from PIL import ImageTk, Image

# Initialize the main window
w = Tk()

# Set the window size
window_width, window_height = 1600, 900

# Center the window on the screen
screen_width, screen_height = w.winfo_screenwidth(), w.winfo_screenheight()
position_top = int(screen_height / 2 - window_height / 2)
position_right = int(screen_width / 2 - window_width / 2)
w.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

# Set window icon
icon_path = r"Resources\logo.png"
icon = PhotoImage(file=icon_path)
w.iconphoto(False, icon)

# Make the window non-resizable
w.resizable(False, False)

# Create a full-window canvas
canvas = Canvas(w, bg='black')
canvas.pack(expand=YES, fill=BOTH)

# Load and display an image
image1 = ImageTk.PhotoImage(file=r"Resources\Homepage.png")
canvas.create_image(0, 0, image=image1, anchor=NW)

# Create and place the "Order now!" button
def run_fun():
    fun()

btn_run_fun = Button(w, width=15, text='Order now!', font=('LITHOGRAPH', 30, 'bold'), bg='#8dccd2', fg='white', command=run_fun)
btn_run_fun.place(relx=0.5, rely=0.5, anchor=CENTER)

# Prepare variables
count1 = count2 = count3 = count4 = count5 = count6 = count7 = count8 = count9 = count10 = count11 = count12 = count13 = count14 = count15 = 1
count16 = count17 = count18 = count19 = count20 = count21 = count22 = count23 = count24 = count25 = count26 = count27 = 1
bc1 = bc2 = bc3 = bc4 = bc5 = bc6 = bc7 = bc8 = bc9 = bc10 = 0
total1 = total2 = total3 = total4 = total5 = total6 = total7 = total8 = total9 = total10 = total11 = total12 = total13 = total14 = total15 = 1
total16 = total17 = total18 = total19 = total20 = total21 = total22 = total23 = total24 = total25 = total26 = total27 = 1
USERNAME, PASSWORD, date1, date2 = StringVar(), StringVar(), StringVar(), StringVar()
now = datetime.now()

# Database function
def Database():
    global conn, cursor
    conn = sqlite3.connect("usernpass.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `member` (mem_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, username TEXT, password TEXT)")
    cursor.execute("SELECT * FROM `member` WHERE `username` = 'admin' AND `password` = 'admin123'")
    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO `member` (username, password) VALUES('admin', 'admin123')")
        conn.commit()

# Table functions
def table1():
    global bc1
    bc1 = 1
    menu()

def table2():
    global bc2
    bc2 = 1
    menu()

def table3():
    global bc3
    bc3 = 1
    menu()

def table4():
    global bc4
    bc4 = 1
    menu()

def table5():
    global bc5
    bc5 = 1
    menu()

def table6():
    global bc6
    bc6 = 1
    menu()

def table7():
    global bc7
    bc7 = 1
    menu()

def table8():
    global bc8
    bc8 = 1
    menu()

def table9():
    global bc9
    bc9 = 1
    menu()

def table10():
    global bc10
    bc10 = 1
    menu()

def bac1():
    global bc1, bc2, bc3, bc4, bc5, bc6, bc7, bc8, bc9, bc10
    bc1 = bc2 = bc3 = bc4 = bc5 = bc6 = bc7 = bc8 = bc9 = bc10 = 0
    t.withdraw()

# Bakewell Tart window
def Bakewell():
    global z1
    z1 = Toplevel(w)
    z1.update_idletasks()
    
    window_width, window_height = 475, 550
    screen_width, screen_height = z1.winfo_screenwidth(), z1.winfo_screenheight()
    position_x = int((screen_width / 2) - (window_width / 2))
    position_y = int((screen_height / 2) - (window_height / 2))
    z1.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")
    z1.iconphoto(False, icon)
    z1.resizable(0, 0)
    z1.focus_set()
    
    canvas = Canvas(z1, width=550, height=550, bg='#f8939c')
    canvas.pack(expand=YES, fill=BOTH)

    photox = PhotoImage(file=r"Resources\backbutton.png")
    back = Button(z1, image=photox, compound=TOP, command=z1.withdraw)
    back.image = photox
    back.place(x=410, y=10)

    photo1 = PhotoImage(file=r"Resources\SHORTCRUST PASTRY\BAKEWELL.png")
    b1 = Button(z1, text='Bakewell Tart', image=photo1, compound=TOP, font=('LITHOGRAPH', 15, 'bold'), fg="white", bg="#f8939c", bd=0)
    b1.image = photo1
    b1.place(x=70, y=100)
    
    # Functions to manage counts
    def add():
        global count1
        count1 = min(count1 + 1, 10)
        txtbox.delete("1.0", END)
        txtbox.insert(END, count1)

    def sub():
        global count1
        count1 = max(count1 - 1, 1)
        txtbox.delete("1.0", END)
        txtbox.insert(END, count1)

    def cnf():
        global total1, count1
        total1 = price1 * count1
        if bc1 == 1: db.insert1('Bakewell Tart', count1, price1, total1)
        elif bc2 == 1: db.insert2('Bakewell Tart', count1, price1, total1)
        elif bc3 == 1: db.insert3('Bakewell Tart', count1, price1, total1)
        elif bc4 == 1: db.insert4('Bakewell Tart', count1, price1, total1)
        elif bc5 == 1: db.insert5('Bakewell Tart', count1, price1, total1)
        elif bc6 == 1: db.insert6('Bakewell Tart', count1, price1, total1)
        elif bc7 == 1: db.insert7('Bakewell Tart', count1, price1, total1)
        elif bc8 == 1: db.insert8('Bakewell Tart', count1, price1, total1)
        elif bc9 == 1: db.insert9('Bakewell Tart', count1, price1, total1)
        elif bc10 == 1: db.insert10('Bakewell Tart', count1, price1, total1)
        count1 = 1
        total1 = 0
        z1.destroy()

    # Create and place widgets in the Bakewell Tart window
    txtbox = Text(z1, height=0.5, width=5, bd=0, font=('LITHOGRAPH', 15, 'bold'), fg="white", bg="#f8939c")
    txtbox.place(x=368, y=165)
    txtbox.insert('1.0', count1)
    
    plus = Button(z1, text='+', font=('arial', 16, 'bold'), width=5, fg="#f8939c", bg="white", command=add)
    plus.place(x=340, y=100)

    minus = Button(z1, text='-', font=('arial', 16, 'bold'), width=5, fg="#f8939c", bg="white", command=sub)
    minus.place(x=340, y=220)

    b2 = Button(z1, text='Confirm Order', compound=TOP, font=('LITHOGRAPH', 12, 'bold'), bd=0, fg="#f8939c", bg="white", command=cnf)
    b2.place(x=325, y=300)

    var = StringVar()
    label1 = Label(z1, textvariable=var, relief=RAISED, justify=LEFT, font=('LITHOGRAPH', 12, 'bold'), bg='#f8939c', bd=0, fg='white')
    var.set("A British tart with layers of jam, \nfrangipane, and icing.")
    label1.place(x=70, y=350)

    var1 = StringVar()
    label2 = Label(z1, textvariable=var1, relief=RAISED, justify=LEFT, font=('LITHOGRAPH', 25, 'bold'), bg='#f8939c', bd=0, fg='white')
    var1.set("₱5 each")
    price1 = 5
    
    label2.place(x=70, y=420)
    z1.title("Bakewell Tart")

def Lemon():
    global z2
    z2 = Toplevel(w)

    # Update idle tasks to ensure the window size is calculated
    z2.update_idletasks()
    
    window_width = 475
    window_height = 550
    
    # Get screen width and height
    screen_width = z2.winfo_screenwidth()
    screen_height = z2.winfo_screenheight()
    
    # Calculate position x, y
    position_x = int((screen_width / 2) - (window_width / 2))
    position_y = int((screen_height / 2) - (window_height / 2))
    
    # Set the geometry of the window
    z2.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")
    
    z2.iconphoto(False, icon)

    z2.resizable(0, 0)
    z2.focus_set()
    
    canvas = Canvas(z2, width=550, height=550, bg='#f8939c')  # Update canvas size
    canvas.pack(expand=YES, fill=BOTH)
    
    # Load and create the back button
    photox = PhotoImage(file=r"Resources\backbutton.png")
    back = Button(z2, image=photox, compound=TOP, command=z2.withdraw)
    back.image = photox
    back.place(x=410, y=10)

    # Load and create the Bakewell Tart button
    photo1 = PhotoImage(file=r"Resources\SHORTCRUST PASTRY\LEMON.png")
    b1 = Button(z2, text='Lemon Meringue Pie', image=photo1, compound=TOP, font=('LITHOGRAPH',15,'bold'), fg="white", bg="#f8939c",bd=0)
    b1.image = photo1
    b1.place(x=70, y=100)

    def add():
        global count2 
        count2=count2+1
        if count2>=10 :
            count2=10
            txtbox.delete("1.0",END)
            txtbox.insert(END,count2)
        else :
            txtbox.delete("1.0",END)
            txtbox.insert(END,count2)
    def sub():
        global count2
        count2 = max(count2 - 1, 1)  # Limit count to 1
        txtbox.delete("1.0", END)
        txtbox.insert(END, count2)
    def cnf():
        global total2
        global count2
        global bc1
        global bc2
        global bc3
        global bc4
        global bc5
        global bc6
        global bc7
        global bc8
        global bc9
        global bc10
        total2=price2*count2
        if(bc1==1):
            db.insert1('Lemon Meringue',count2,price2,total2)
        elif(bc2==1):
            db.insert2('Lemon Meringue',count2,price2,total2)
        elif(bc3==1):
            db.insert3('Lemon Meringue',count2,price2,total2)
        elif(bc4==1):
            db.insert4('Lemon Meringue',count2,price2,total2)
        elif(bc5==1):           
            db.insert5('Lemon Meringue',count2,price2,total2)
        elif(bc7==1):           
            db.insert7('Lemon Meringue',count2,price2,total2)
        elif(bc8==1):            
            db.insert8('Lemon Meringue',count2,price2,total2)
        elif(bc9==1):            
            db.insert9('Lemon Meringue',count2,price2,total2)
        elif(bc10==1):
            db.insert10('Lemon Meringue',count2,price2,total2)
        count2=1
        total2=0
        z2.destroy()

    # Create and place the text box to display count
    txtbox = Text(z2, height=0.5, width=5, bd=0, font=('LITHOGRAPH',15,'bold'), fg="white", bg="#f8939c")
    txtbox.place(x=368, y=165)
    txtbox.insert('1.0', count2)
    
    # Create and place the plus button
    plus = Button(z2, text='+', font=('arial', 16, 'bold'), width=5, fg="#f8939c", bg="white", command=add)
    plus.place(x=340, y=100)

    # Create and place the minus button
    minus = Button(z2, text='-', font=('arial', 16, 'bold'), width=5, fg="#f8939c", bg="white", command=sub)
    minus.place(x=340, y=220)

    # Create and place the confirm button
    b2 = Button(z2, text='Confirm Order', compound=TOP, font=('LITHOGRAPH',12,'bold'), bd=0, fg="#f8939c", bg="white", command=cnf)
    b2.place(x=325, y=300)

    # Create and place a label with a description
    var = StringVar()
    label1 = Label(z2, textvariable=var, relief=RAISED, justify=LEFT, font=('LITHOGRAPH', 12,'bold'), bg='#f8939c', bd=0, fg='white')
    var.set("A tart filled with lemon curd and topped \nwith fluffy meringue.")
    label1.place(x=70, y=350)

    # Create and place a label with the price
    var1 = StringVar()
    label2 = Label(z2, textvariable=var1, relief=RAISED, justify=LEFT, font=('LITHOGRAPH', 25, 'bold'), bg='#f8939c', bd=0, fg='white')
    var1.set("₱4 each")
    price2 = 4
    
    label2.place(x=70, y=420)
    z2.title("Lemon Meringue")

def Choco():
    global z3
    z3 = Toplevel(w)

    # Update idle tasks to ensure the window size is calculated
    z3.update_idletasks()
    
    window_width = 475
    window_height = 550
    
    # Get screen width and height
    screen_width = z3.winfo_screenwidth()
    screen_height = z3.winfo_screenheight()
    
    # Calculate position x, y
    position_x = int((screen_width / 2) - (window_width / 2))
    position_y = int((screen_height / 2) - (window_height / 2))
    
    # Set the geometry of the window
    z3.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")
    
    z3.iconphoto(False, icon)

    z3.resizable(0, 0)
    z3.focus_set()
    
    canvas = Canvas(z3, width=550, height=550, bg='#f8939c')  # Update canvas size
    canvas.pack(expand=YES, fill=BOTH)
    
    # Load and create the back button
    photox = PhotoImage(file=r"Resources\backbutton.png")
    back = Button(z3, image=photox, compound=TOP, command=z3.withdraw)
    back.image = photox
    back.place(x=410, y=10)

    # Load and create the Bakewell Tart button
    photo1 = PhotoImage(file=r"Resources\SHORTCRUST PASTRY\CHOCO.png")
    b3 = Button(z3, text='Chocolate Pecan', image=photo1, compound=TOP, font=('LITHOGRAPH',15,'bold'), fg="white", bg="#f8939c",bd=0)
    b3.image = photo1
    b3.place(x=70, y=100)

    def add():
        global count3
        count3=count3+1
        if count3>=10 :
            count3=10
            txtbox.delete("1.0",END)
            txtbox.insert(END,count3)
        else :
            txtbox.delete("1.0",END)
            txtbox.insert(END,count3)
    def sub():
        global count3
        count3 = max(count3 - 1, 1)  # Limit count to 1
        txtbox.delete("1.0", END)
        txtbox.insert(END, count3)
    def cnf():
        global total3
        global count3
        global bc1
        global bc2
        global bc3
        global bc4
        global bc5
        global bc6
        global bc7
        global bc8
        global bc9
        global bc10
        total3=price3*count3
        if(bc1==1):
            db.insert1('Chocolate Pecan',count3,price3,total3)
        elif(bc2==1):
            db.insert2('Chocolate Pecan',count3,price3,total3)
        elif(bc3==1):
            db.insert3('Chocolate Pecan',count3,price3,total3)
        elif(bc4==1):
            db.insert4('Chocolate Pecan',count3,price3,total3)
        elif(bc5==1):           
            db.insert5('Chocolate Pecan',count3,price3,total3)
        elif(bc6==1):            
            db.insert6('Chocolate Pecan',count3,price3,total3)
        elif(bc7==1):           
            db.insert7('Chocolate Pecan',count3,price3,total3)
        elif(bc8==1):            
            db.insert8('Chocolate Pecan',count3,price3,total3)
        elif(bc9==1):            
            db.insert9('Chocolate Pecan',count3,price3,total3)
        elif(bc10==1):
            db.insert10('Chocolate Pecan',count3,price3,total3)
        count3=1
        total3=0
        z3.destroy()
# Create and place the text box to display count
    txtbox = Text(z3, height=0.5, width=5, bd=0, font=('LITHOGRAPH',15,'bold'), fg="white", bg="#f8939c")
    txtbox.place(x=368, y=165)
    txtbox.insert('1.0', count3)
    
    # Create and place the plus button
    plus = Button(z3, text='+', font=('arial', 16, 'bold'), width=5, fg="#f8939c", bg="white", command=add)
    plus.place(x=340, y=100)

    # Create and place the minus button
    minus = Button(z3, text='-', font=('arial', 16, 'bold'), width=5, fg="#f8939c", bg="white", command=sub)
    minus.place(x=340, y=220)

    # Create and place the confirm button
    b2 = Button(z3, text='Confirm Order', compound=TOP, font=('LITHOGRAPH',12,'bold'), bd=0, fg="#f8939c", bg="white", command=cnf)
    b2.place(x=325, y=300)

    # Create and place a label with a description
    var = StringVar()
    label1 = Label(z3, textvariable=var, relief=RAISED, justify=LEFT, font=('LITHOGRAPH', 12,'bold'), bg='#f8939c', bd=0, fg='white')
    var.set("A rich, sweet pie with a filling of pecans,\nsyrup, and butter.")
    label1.place(x=70, y=350)

    # Create and place a label with the price
    var1 = StringVar()
    label2 = Label(z3, textvariable=var1, relief=RAISED, justify=LEFT, font=('LITHOGRAPH', 25, 'bold'), bg='#f8939c', bd=0, fg='white')
    var1.set("₱15 each")
    price3 = 15
    
    label2.place(x=70, y=420)
    z3.title("Chocolate Pecan")
    
def Fruit():
    
    global z4
    z4 = Toplevel(w)

    # Update idle tasks to ensure the window size is calculated
    z4.update_idletasks()
    
    window_width = 475
    window_height = 550
    
    # Get screen width and height
    screen_width = z4.winfo_screenwidth()
    screen_height = z4.winfo_screenheight()
    
    # Calculate position x, y
    position_x = int((screen_width / 2) - (window_width / 2))
    position_y = int((screen_height / 2) - (window_height / 2))
    
    # Set the geometry of the window
    z4.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")
    
    z4.iconphoto(False, icon)

    z4.resizable(0, 0)
    z4.focus_set()
    
    canvas = Canvas(z4, width=550, height=550, bg='#f8939c')  # Update canvas size
    canvas.pack(expand=YES, fill=BOTH)
    
    # Load and create the back button
    photox = PhotoImage(file=r"Resources\backbutton.png")
    back = Button(z4, image=photox, compound=TOP, command=z4.withdraw)
    back.image = photox
    back.place(x=410, y=10)

    # Load and create the Fruit Tart button
    photo1 = PhotoImage(file=r"Resources\SHORTCRUST PASTRY\FRUIT.png")
    b4 = Button(z4, text='Fruit Tart', image=photo1, compound=TOP, font=('LITHOGRAPH',15,'bold'), fg="white", bg="#f8939c",bd=0)
    b4.image = photo1
    b4.place(x=70, y=100)

    def add():
        global count4
        count4 = count4 + 1
        if count4 >= 10:
            count4 = 10
            txtbox.delete("1.0", END)
            txtbox.insert(END, count4)
        else:
            txtbox.delete("1.0", END)
            txtbox.insert(END, count4)

    def sub():
        global count4
        count4 = max(count4 - 1, 1)  # Limit count to 1
        txtbox.delete("1.0", END)
        txtbox.insert(END, count4)

    
    def cnf():
        global total4
        global count4
        global bc1
        global bc2
        global bc3
        global bc4
        global bc5
        global bc6
        global bc7
        global bc8
        global bc9
        global bc10
        total4 = price4 * count4
        if bc1 == 1:
            db.insert1('Fruit Tart', count4, price4, total4)
        elif bc2 == 1:
            db.insert2('Fruit Tart', count4, price4, total4)
        elif bc3 == 1:
            db.insert3('Fruit Tart', count4, price4, total4)
        elif bc4 == 1:
            db.insert4('Fruit Tart', count4, price4, total4)
        elif bc5 == 1:           
            db.insert5('Fruit Tart', count4, price4, total4)
        elif bc6 == 1:            
            db.insert6('Fruit Tart', count4, price4, total4)
        elif bc7 == 1:           
            db.insert7('Fruit Tart', count4, price4, total4)
        elif bc8 == 1:            
            db.insert8('Fruit Tart', count4, price4, total4)
        elif bc9 == 1:            
            db.insert9('Fruit Tart', count4, price4, total4)
        elif bc10 == 1:
            db.insert10('Fruit Tart', count4, price4, total4)
        count4 = 1
        total4 = 0
        z4.destroy()
    
    # Create and place the text box to display count
    txtbox = Text(z4, height=0.5, width=5, bd=0, font=('LITHOGRAPH',15,'bold'), fg="white", bg="#f8939c")
    txtbox.place(x=368, y=165)
    txtbox.insert('1.0', count4)
    
    # Create and place the plus button
    plus = Button(z4, text='+', font=('arial', 16, 'bold'), width=5, fg="#f8939c", bg="white", command=add)
    plus.place(x=340, y=100)

    # Create and place the minus button
    minus = Button(z4, text='-', font=('arial', 16, 'bold'), width=5, fg="#f8939c", bg="white", command=sub)
    minus.place(x=340, y=220)

    # Create and place the confirm button
    b2 = Button(z4, text='Confirm Order', compound=TOP, font=('LITHOGRAPH',12,'bold'), bd=0, fg="#f8939c", bg="white", command=cnf)
    b2.place(x=325, y=300)

    # Create and place a label with a description
    var = StringVar()
    label1 = Label(z4, textvariable=var, relief=RAISED, justify=LEFT, font=('LITHOGRAPH', 12,'bold'), bg='#f8939c', bd=0, fg='white')
    var.set("A crisp pastry shell filled with pastry\ncream and topped with fresh fruits.")
    label1.place(x=70, y=350)

    # Create and place a label with the price
    var1 = StringVar()
    label2 = Label(z4, textvariable=var1, relief=RAISED, justify=LEFT, font=('LITHOGRAPH', 25, 'bold'), bg='#f8939c', bd=0, fg='white')
    var1.set("₱20 each")
    price4 = 20
    
    label2.place(x=70, y=420)
    z4.title("Fruit Tart")
    
def Tarte():
    global z5
    z5 = Toplevel(w)

    # Update idle tasks to ensure the window size is calculated
    z5.update_idletasks()
    
    window_width = 475
    window_height = 550
    
    # Get screen width and height
    screen_width = z5.winfo_screenwidth()
    screen_height = z5.winfo_screenheight()
    
    # Calculate position x, y
    position_x = int((screen_width / 2) - (window_width / 2))
    position_y = int((screen_height / 2) - (window_height / 2))
    
    # Set the geometry of the window
    z5.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")
    
    z5.iconphoto(False, icon)

    z5.resizable(0, 0)
    z5.focus_set()
    
    canvas = Canvas(z5, width=550, height=550, bg='#f8939c')  # Update canvas size
    canvas.pack(expand=YES, fill=BOTH)
    
    # Load and create the back button
    photox = PhotoImage(file=r"Resources\backbutton.png")
    back = Button(z5, image=photox, compound=TOP, command=z5.withdraw)
    back.image = photox
    back.place(x=410, y=10)

    # Load and create the Fruit Tart button
    photo1 = PhotoImage(file=r"Resources\SHORTCRUST PASTRY\TARTE.png")
    b5 = Button(z5, text='Tarte Tatin', image=photo1, compound=TOP, font=('LITHOGRAPH',15,'bold'), fg="white", bg="#f8939c",bd=0)
    b5.image = photo1
    b5.place(x=70, y=100)

    def add():
        global count5
        count5 = count5 + 1
        if count5 >= 10:
            count5 = 10
            txtbox.delete("1.0", END)
            txtbox.insert(END, count5)
        else:
            txtbox.delete("1.0", END)
            txtbox.insert(END, count5)
    
    def sub():
        global count5
        count5 = max(count5 - 1, 1)  # Limit count to 0
        txtbox.delete("1.0", END)
        txtbox.insert(END, count5)
    
    def cnf():
        global total5
        global count5
        global bc1
        global bc2
        global bc3
        global bc4
        global bc5
        global bc6
        global bc7
        global bc8
        global bc9
        global bc10
        total5 = price5 * count5
        if bc1 == 1:
            db.insert1('Tarte Tatin', count5, price5, total5)
        elif bc2 == 1:
            db.insert2('Tarte Tatin', count5, price5, total5)
        elif bc3 == 1:
            db.insert3('Tarte Tatin', count5, price5, total5)
        elif bc4 == 1:
            db.insert4('Tarte Tatin', count5, price5, total5)
        elif bc5 == 1:
            db.insert5('Tarte Tatin', count5, price5, total5)
        elif bc6 == 1:
            db.insert6('Tarte Tatin', count5, price5, total5)
        elif bc7 == 1:
            db.insert7('Tarte Tatin', count5, price5, total5)
        elif bc8 == 1:
            db.insert8('Tarte Tatin', count5, price5, total5)
        elif bc9 == 1:
            db.insert9('Tarte Tatin', count5, price5, total5)
        elif bc10 == 1:
            db.insert10('Tarte Tatin', count5, price5, total5)
        count5 = 1
        total5 = 0
        z5.destroy()

    # Create and place the text box to display count
    txtbox = Text(z5, height=0.5, width=5, bd=0, font=('LITHOGRAPH',15,'bold'), fg="white", bg="#f8939c")
    txtbox.place(x=368, y=165)
    txtbox.insert('1.0', count5)
    
    # Create and place the plus button
    plus = Button(z5, text='+', font=('arial', 16, 'bold'), width=5, fg="#f8939c", bg="white", command=add)
    plus.place(x=340, y=100)

    # Create and place the minus button
    minus = Button(z5, text='-', font=('arial', 16, 'bold'), width=5, fg="#f8939c", bg="white", command=sub)
    minus.place(x=340, y=220)

    # Create and place the confirm button
    b2 = Button(z5, text='Confirm Order', compound=TOP, font=('LITHOGRAPH',12,'bold'), bd=0, fg="#f8939c", bg="white", command=cnf)
    b2.place(x=325, y=300)

    # Create and place a label with a description
    var = StringVar()
    label1 = Label(z5, textvariable=var, relief=RAISED, justify=LEFT, font=('LITHOGRAPH', 12,'bold'), bg='#f8939c', bd=0, fg='white')
    var.set("An upside-down caramelized apple tart.")
    label1.place(x=70, y=350)

    # Create and place a label with the price
    var1 = StringVar()
    label2 = Label(z5, textvariable=var1, relief=RAISED, justify=LEFT, font=('LITHOGRAPH', 25, 'bold'), bg='#f8939c', bd=0, fg='white')
    var1.set("₱15 each")
    price5 = 15
    
    label2.place(x=70, y=420)
    z5.title("Tarte Tatin")
    
def AppleStr():
    global z6
    z6 = Toplevel(w)

    # Update idle tasks to ensure the window size is calculated
    z6.update_idletasks()
    
    window_width = 475
    window_height = 550
    
    # Get screen width and height
    screen_width = z6.winfo_screenwidth()
    screen_height = z6.winfo_screenheight()
    
    # Calculate position x, y
    position_x = int((screen_width / 2) - (window_width / 2))
    position_y = int((screen_height / 2) - (window_height / 2))
    
    # Set the geometry of the window
    z6.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")
    
    z6.iconphoto(False, icon)

    z6.resizable(0, 0)
    z6.focus_set()
    
    canvas = Canvas(z6, width=550, height=550, bg='#f8939c')  # Update canvas size
    canvas.pack(expand=YES, fill=BOTH)
    
    # Load and create the back button
    photox = PhotoImage(file=r"Resources\backbutton.png")
    back = Button(z6, image=photox, compound=TOP, command=z6.withdraw)
    back.image = photox
    back.place(x=410, y=10)

    # Load and create the Fruit Tart button
    photo1 = PhotoImage(file=r"Resources\FILO PASTRY\APPLE STRUDEL.png")
    b6 = Button(z6, text='Apple Strudel', image=photo1, compound=TOP, font=('LITHOGRAPH',15,'bold'), fg="white", bg="#f8939c",bd=0)
    b6.image = photo1
    b6.place(x=70, y=100)

    def add():
        global count6
        count6 = count6 + 1
        if count6 >= 10:
            count6 = 10
            txtbox.delete("1.0", END)
            txtbox.insert(END, count6)
        else:
            txtbox.delete("1.0", END)
            txtbox.insert(END, count6)
    
    def sub():
        global count6
        count6 = max(count6 - 1, 1)  # Limit count to 1
        txtbox.delete("1.0", END)
        txtbox.insert(END, count6)
    
    def cnf():
        global total6
        global count6
        global bc1
        global bc2
        global bc3
        global bc4
        global bc5
        global bc6
        global bc7
        global bc8
        global bc9
        global bc10
        total6 = price6 * count6
        if bc1 == 1:
            db.insert1('Apple Strudel', count6, price6, total6)
        elif bc2 == 1:
            db.insert2('Apple Strudel', count6, price6, total6)
        elif bc3 == 1:
            db.insert3('Apple Strudel', count6, price6, total6)
        elif bc4 == 1:
            db.insert4('Apple Strudel', count6, price6, total6)
        elif bc5 == 1:
            db.insert5('Apple Strudel', count6, price6, total6)
        elif bc6 == 1:
            db.insert6('Apple Strudel', count6, price6, total6)
        elif bc7 == 1:
            db.insert7('Apple Strudel', count6, price6, total6)
        elif bc8 == 1:
            db.insert8('Apple Strudel', count6, price6, total6)
        elif bc9 == 1:
            db.insert9('Apple Strudel', count6, price6, total6)
        elif bc10 == 1:
            db.insert10('Apple Strudel', count6, price6, total6)
        count6 = 1
        total6 = 0
        z6.destroy()

    # Create and place the text box to display count
    txtbox = Text(z6, height=0.5, width=5, bd=0, font=('LITHOGRAPH',15,'bold'), fg="white", bg="#f8939c")
    txtbox.place(x=368, y=165)
    txtbox.insert('1.0', count6)
    
    # Create and place the plus button
    plus = Button(z6, text='+', font=('arial', 16, 'bold'), width=5, fg="#f8939c", bg="white", command=add)
    plus.place(x=340, y=100)

    # Create and place the minus button
    minus = Button(z6, text='-', font=('arial', 16, 'bold'), width=5, fg="#f8939c", bg="white", command=sub)
    minus.place(x=340, y=220)

    # Create and place the confirm button
    b2 = Button(z6, text='Confirm Order', compound=TOP, font=('LITHOGRAPH',12,'bold'), bd=0, fg="#f8939c", bg="white", command=cnf)
    b2.place(x=325, y=300)

    # Create and place a label with a description
    var = StringVar()
    label1 = Label(z6, textvariable=var, relief=RAISED, justify=LEFT, font=('LITHOGRAPH', 12,'bold'), bg='#f8939c', bd=0, fg='white')
    var.set("A classic Viennese dessert with apple \nfilling wrapped in filo.")
    label1.place(x=70, y=350)

    # Create and place a label with the price
    var1 = StringVar()
    label2 = Label(z6, textvariable=var1, relief=RAISED, justify=LEFT, font=('LITHOGRAPH', 25, 'bold'), bg='#f8939c', bd=0, fg='white')
    var1.set("₱20 each")
    price6 = 20
    
    label2.place(x=70, y=420)
    z6.title("Apple Strudel")

def Baklava():
    global z7
    z7 = Toplevel(w)

    # Update idle tasks to ensure the window size is calculated
    z7.update_idletasks()
    
    window_width = 475
    window_height = 550
    
    # Get screen width and height
    screen_width = z7.winfo_screenwidth()
    screen_height = z7.winfo_screenheight()
    
    # Calculate position x, y
    position_x = int((screen_width / 2) - (window_width / 2))
    position_y = int((screen_height / 2) - (window_height / 2))
    
    # Set the geometry of the window
    z7.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")
    
    z7.iconphoto(False, icon)

    z7.resizable(0, 0)
    z7.focus_set()
    
    canvas = Canvas(z7, width=550, height=550, bg='#f8939c')  # Update canvas size
    canvas.pack(expand=YES, fill=BOTH)
    
    # Load and create the back button
    photox = PhotoImage(file=r"Resources\backbutton.png")
    back = Button(z7, image=photox, compound=TOP, command=z7.withdraw)
    back.image = photox
    back.place(x=410, y=10)

    photo1 = PhotoImage(file=r"Resources\FILO PASTRY\BAKLAVA.png")
    b7 = Button(z7, text='Baklava', image=photo1, compound=TOP, font=('LITHOGRAPH',15,'bold'), fg="white", bg="#f8939c",bd=0)
    b7.image = photo1
    b7.place(x=70, y=100)

    def add():
        global count7
        count7 = count7 + 1
        if count7 >= 10:
            count7 = 10
            txtbox.delete("1.0", END)
            txtbox.insert(END, count7)
        else:
            txtbox.delete("1.0", END)
            txtbox.insert(END, count7)
    
    def sub():
        global count7
        count7 = max(count7 - 1, 1)  # Limit count to 0
        txtbox.delete("1.0", END)
        txtbox.insert(END, count7)
    
    def cnf():
        global total7
        global count7
        global bc1
        global bc2
        global bc3
        global bc4
        global bc5
        global bc6
        global bc7
        global bc8
        global bc9
        global bc10
        total7 = price7 * count7
        if bc1 == 1:
            db.insert1('Baklava', count7, price7, total7)
        elif bc2 == 1:
            db.insert2('Baklava', count7, price7, total7)
        elif bc3 == 1:
            db.insert3('Baklava', count7, price7, total7)
        elif bc4 == 1:
            db.insert4('Baklava', count7, price7, total7)
        elif bc5 == 1:
            db.insert5('Baklava', count7, price7, total7)
        elif bc6 == 1:
            db.insert6('Baklava', count7, price7, total7)
        elif bc7 == 1:
            db.insert7('Baklava', count7, price7, total7)
        elif bc8 == 1:
            db.insert8('Baklava', count7, price7, total7)
        elif bc9 == 1:
            db.insert9('Baklava', count7, price7, total7)
        elif bc10 == 1:
            db.insert10('Baklava', count7, price7, total7)
        count7 = 1
        total7 = 0
        z7.destroy()

    # Create and place the text box to display count
    txtbox = Text(z7, height=0.5, width=5, bd=0, font=('LITHOGRAPH',15,'bold'), fg="white", bg="#f8939c")
    txtbox.place(x=368, y=165)
    txtbox.insert('1.0', count7)
    
    # Create and place the plus button
    plus = Button(z7, text='+', font=('arial', 16, 'bold'), width=5, fg="#f8939c", bg="white", command=add)
    plus.place(x=340, y=100)

    # Create and place the minus button
    minus = Button(z7, text='-', font=('arial', 16, 'bold'), width=5, fg="#f8939c", bg="white", command=sub)
    minus.place(x=340, y=220)

    # Create and place the confirm button
    b2 = Button(z7, text='Confirm Order', compound=TOP, font=('LITHOGRAPH',12,'bold'), bd=0, fg="#f8939c", bg="white", command=cnf)
    b2.place(x=325, y=300)

    # Create and place a label with a description
    var = StringVar()
    label1 = Label(z7, textvariable=var, relief=RAISED, justify=LEFT, font=('LITHOGRAPH', 12,'bold'), bg='#f8939c', bd=0, fg='white')
    var.set("A sweet, rich pastry made with layers of\nfilo, nuts, and honey syrup.")
    label1.place(x=70, y=350)

    # Create and place a label with the price
    var1 = StringVar()
    label2 = Label(z7, textvariable=var1, relief=RAISED, justify=LEFT, font=('LITHOGRAPH', 25, 'bold'), bg='#f8939c', bd=0, fg='white')
    var1.set("₱25 each")
    price7 = 25
    
    label2.place(x=70, y=420)
    z7.title("Baklava")

def Borek():
    global z8
    z8 = Toplevel(w)

    # Update idle tasks to ensure the window size is calculated
    z8.update_idletasks()
    
    window_width = 475
    window_height = 550
    
    # Get screen width and height
    screen_width = z8.winfo_screenwidth()
    screen_height = z8.winfo_screenheight()
    
    # Calculate position x, y
    position_x = int((screen_width / 2) - (window_width / 2))
    position_y = int((screen_height / 2) - (window_height / 2))
    
    # Set the geometry of the window
    z8.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")
    
    z8.iconphoto(False, icon)

    z8.resizable(0, 0)
    z8.focus_set()
    
    canvas = Canvas(z8, width=550, height=550, bg='#f8939c')  # Update canvas size
    canvas.pack(expand=YES, fill=BOTH)
    
    # Load and create the back button
    photox = PhotoImage(file=r"Resources\backbutton.png")
    back = Button(z8, image=photox, compound=TOP, command=z8.withdraw)
    back.image = photox
    back.place(x=410, y=10)

    # Load and create the Fruit Tart button
    photo1 = PhotoImage(file=r"Resources\FILO PASTRY\BOREK.png")
    b8 = Button(z8, text='Borek', image=photo1, compound=TOP, font=('LITHOGRAPH',15,'bold'), fg="white", bg="#f8939c",bd=0)
    b8.image = photo1
    b8.place(x=70, y=100)

    def add():
        global count8
        count8 = count8 + 1
        if count8 >= 10:
            count8 = 10
            txtbox.delete("1.0", END)
            txtbox.insert(END, count8)
        else:
            txtbox.delete("1.0", END)
            txtbox.insert(END, count8)
    
    def sub():
        global count8
        count8 = max(count8 - 1, 1)  # Limit count to 0
        txtbox.delete("1.0", END)
        txtbox.insert(END, count8)
    
    def cnf():
        global total8
        global count8
        global bc1
        global bc2
        global bc3
        global bc4
        global bc5
        global bc6
        global bc7
        global bc8
        global bc9
        global bc10
        total8 = price8 * count8
        if bc1 == 1:
            db.insert1('Borek', count8, price8, total8)
        elif bc2 == 1:
            db.insert2('Borek', count8, price8, total8)
        elif bc3 == 1:
            db.insert3('Borek', count8, price8, total8)
        elif bc4 == 1:
            db.insert4('Borek', count8, price8, total8)
        elif bc5 == 1:
            db.insert5('Borek', count8, price8, total8)
        elif bc6 == 1:
            db.insert6('Borek', count8, price8, total8)
        elif bc7 == 1:
            db.insert7('Borek', count8, price8, total8)
        elif bc8 == 1:
            db.insert8('Borek', count8, price8, total8)
        elif bc9 == 1:
            db.insert9('Borek', count8, price8, total8)
        elif bc10 == 1:
            db.insert10('Borek', count8, price8, total8)
        count8 = 1
        total8 = 0
        z8.destroy()

    # Create and place the text box to display count
    txtbox = Text(z8, height=0.5, width=5, bd=0, font=('LITHOGRAPH',15,'bold'), fg="white", bg="#f8939c")
    txtbox.place(x=368, y=165)
    txtbox.insert('1.0', count8)
    
    # Create and place the plus button
    plus = Button(z8, text='+', font=('arial', 16, 'bold'), width=5, fg="#f8939c", bg="white", command=add)
    plus.place(x=340, y=100)

    # Create and place the minus button
    minus = Button(z8, text='-', font=('arial', 16, 'bold'), width=5, fg="#f8939c", bg="white", command=sub)
    minus.place(x=340, y=220)

    # Create and place the confirm button
    b2 = Button(z8, text='Confirm Order', compound=TOP, font=('LITHOGRAPH',12,'bold'), bd=0, fg="#f8939c", bg="white", command=cnf)
    b2.place(x=325, y=300)

    # Create and place a label with a description
    var = StringVar()
    label1 = Label(z8, textvariable=var, relief=RAISED, justify=LEFT, font=('LITHOGRAPH', 12,'bold'), bg='#f8939c', bd=0, fg='white')
    var.set("A Turkish pastry filled with\nmeats, cheeses, or vegetables.")
    label1.place(x=70, y=350)

    # Create and place a label with the price
    var1 = StringVar()
    label2 = Label(z8, textvariable=var1, relief=RAISED, justify=LEFT, font=('LITHOGRAPH', 25, 'bold'), bg='#f8939c', bd=0, fg='white')
    var1.set("₱15 each")
    price8 = 15
    
    label2.place(x=70, y=420)
    z8.title("Borek")

def Kataifi():
    global z9
    z9 = Toplevel(w)

    # Update idle tasks to ensure the window size is calculated
    z9.update_idletasks()
    
    window_width = 475
    window_height = 550
    
    # Get screen width and height
    screen_width = z9.winfo_screenwidth()
    screen_height = z9.winfo_screenheight()
    
    # Calculate position x, y
    position_x = int((screen_width / 2) - (window_width / 2))
    position_y = int((screen_height / 2) - (window_height / 2))
    
    # Set the geometry of the window
    z9.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")
    
    z9.iconphoto(False, icon)

    z9.resizable(0, 0)
    z9.focus_set()
    
    canvas = Canvas(z9, width=550, height=550, bg='#f8939c')  # Update canvas size
    canvas.pack(expand=YES, fill=BOTH)
    
    # Load and create the back button
    photox = PhotoImage(file=r"Resources\backbutton.png")
    back = Button(z9, image=photox, compound=TOP, command=z9.withdraw)
    back.image = photox
    back.place(x=410, y=10)

    # Load and create the Fruit Tart button
    photo1 = PhotoImage(file=r"Resources\FILO PASTRY\KATAIFI.png")
    b9 = Button(z9, text='Kataifi', image=photo1, compound=TOP, font=('LITHOGRAPH',15,'bold'), fg="white", bg="#f8939c",bd=0)
    b9.image = photo1
    b9.place(x=70, y=100)

    def add():
        global count9
        count9 = count9 + 1
        if count9 >= 10:
            count9 = 10
            txtbox.delete("1.0", END)
            txtbox.insert(END, count9)
        else:
            txtbox.delete("1.0", END)
            txtbox.insert(END, count9)
    
    def sub():
        global count9
        count9 = max(count9 - 1, 1)  # Limit count to 0
        txtbox.delete("1.0", END)
        txtbox.insert(END, count9)
    
    def cnf():
        global total9
        global count9
        global bc1
        global bc2
        global bc3
        global bc4
        global bc5
        global bc6
        global bc7
        global bc8
        global bc9
        global bc10
        total9 = price9 * count9
        if bc1 == 1:
            db.insert1('Kataifi', count9, price9, total9)
        elif bc2 == 1:
            db.insert2('Kataifi', count9, price9, total9)
        elif bc3 == 1:
            db.insert3('Kataifi', count9, price9, total9)
        elif bc4 == 1:
            db.insert4('Kataifi', count9, price9, total9)
        elif bc5 == 1:
            db.insert5('Kataifi', count9, price9, total9)
        elif bc6 == 1:
            db.insert6('Kataifi', count9, price9, total9)
        elif bc7 == 1:
            db.insert7('Kataifi', count9, price9, total9)
        elif bc8 == 1:
            db.insert8('Kataifi', count9, price9, total9)
        elif bc9 == 1:
            db.insert9('Kataifi', count9, price9, total9)
        elif bc10 == 1:
            db.insert10('Kataifi', count9, price9, total9)
        count9 = 1
        total9 = 0
        z9.destroy()

    # Create and place the text box to display count
    txtbox = Text(z9, height=0.5, width=5, bd=0, font=('LITHOGRAPH',15,'bold'), fg="white", bg="#f8939c")
    txtbox.place(x=368, y=165)
    txtbox.insert('1.0', count9)
    
    # Create and place the plus button
    plus = Button(z9, text='+', font=('arial', 16, 'bold'), width=5, fg="#f8939c", bg="white", command=add)
    plus.place(x=340, y=100)

    # Create and place the minus button
    minus = Button(z9, text='-', font=('arial', 16, 'bold'), width=5, fg="#f8939c", bg="white", command=sub)
    minus.place(x=340, y=220)

    # Create and place the confirm button
    b2 = Button(z9, text='Confirm Order', compound=TOP, font=('LITHOGRAPH',12,'bold'), bd=0, fg="#f8939c", bg="white", command=cnf)
    b2.place(x=325, y=300)

    # Create and place a label with a description
    var = StringVar()
    label1 = Label(z9, textvariable=var, relief=RAISED, justify=LEFT, font=('LITHOGRAPH', 12,'bold'), bg='#f8939c', bd=0, fg='white')
    var.set("A Greek dessert made with shredded filo dough,\nfilled with nuts, and soaked in syrup.")
    label1.place(x=70, y=350)

    # Create and place a label with the price
    var1 = StringVar()
    label2 = Label(z9, textvariable=var1, relief=RAISED, justify=LEFT, font=('LITHOGRAPH', 25, 'bold'), bg='#f8939c', bd=0, fg='white')
    var1.set("₱15 each")
    price9 = 15
    
    label2.place(x=70, y=420)
    z9.title("Kataifi")

def Tiropita():
    global z10
    z10 = Toplevel(w)

    # Update idle tasks to ensure the window size is calculated
    z10.update_idletasks()
    
    window_width = 475
    window_height = 550
    
    # Get screen width and height
    screen_width = z10.winfo_screenwidth()
    screen_height = z10.winfo_screenheight()
    
    # Calculate position x, y
    position_x = int((screen_width / 2) - (window_width / 2))
    position_y = int((screen_height / 2) - (window_height / 2))
    
    # Set the geometry of the window
    z10.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")
    
    z10.iconphoto(False, icon)

    z10.resizable(0, 0)
    z10.focus_set()
    
    canvas = Canvas(z10, width=550, height=550, bg='#f8939c')  # Update canvas size
    canvas.pack(expand=YES, fill=BOTH)
    
    # Load and create the back button
    photox = PhotoImage(file=r"Resources\backbutton.png")
    back = Button(z10, image=photox, compound=TOP, command=z10.withdraw)
    back.image = photox
    back.place(x=410, y=10)

    # Load and create the Fruit Tart button
    photo1 = PhotoImage(file=r"Resources\FILO PASTRY\TIROPITA.png")
    b10 = Button(z10, text='Tiropita', image=photo1, compound=TOP, font=('LITHOGRAPH',15,'bold'), fg="white", bg="#f8939c",bd=0)
    b10.image = photo1
    b10.place(x=70, y=100)

    def add():
        global count10
        count10 = count10 + 1
        if count10 >= 10:
            count10 = 10
            txtbox.delete("1.0", END)
            txtbox.insert(END, count10)
        else:
            txtbox.delete("1.0", END)
            txtbox.insert(END, count10)
    
    def sub():
        global count10
        count10 = max(count10 - 1, 1)  # Limit count to 0
        txtbox.delete("1.0", END)
        txtbox.insert(END, count10)
    
    def cnf():
        global total10
        global count10
        global bc1
        global bc2
        global bc3
        global bc4
        global bc5
        global bc6
        global bc7
        global bc8
        global bc9
        global bc10
        total10 = price10 * count10
        if bc1 == 1:
            db.insert1('Tiropita', count10, price10, total10)
        elif bc2 == 1:
            db.insert2('Tiropita', count10, price10, total10)
        elif bc3 == 1:
            db.insert3('Tiropita', count10, price10, total10)
        elif bc4 == 1:
            db.insert4('Tiropita', count10, price10, total10)
        elif bc5 == 1:
            db.insert5('Tiropita', count10, price10, total10)
        elif bc6 == 1:
            db.insert6('Tiropita', count10, price10, total10)
        elif bc7 == 1:
            db.insert7('Tiropita', count10, price10, total10)
        elif bc8 == 1:
            db.insert8('Tiropita', count10, price10, total10)
        elif bc9 == 1:
            db.insert9('Tiropita', count10, price10, total10)
        elif bc10 == 1:
            db.insert10('Tiropita', count10, price10, total10)
        count10 = 1
        total10 = 0
        z10.destroy()

    # Create and place the text box to display count
    txtbox = Text(z10, height=0.5, width=5, bd=0, font=('LITHOGRAPH',15,'bold'), fg="white", bg="#f8939c")
    txtbox.place(x=368, y=165)
    txtbox.insert('1.0', count10)
    
    # Create and place the plus button
    plus = Button(z10, text='+', font=('arial', 16, 'bold'), width=5, fg="#f8939c", bg="white", command=add)
    plus.place(x=340, y=100)

    # Create and place the minus button
    minus = Button(z10, text='-', font=('arial', 16, 'bold'), width=5, fg="#f8939c", bg="white", command=sub)
    minus.place(x=340, y=220)

    # Create and place the confirm button
    b2 = Button(z10, text='Confirm Order', compound=TOP, font=('LITHOGRAPH',12,'bold'), bd=0, fg="#f8939c", bg="white", command=cnf)
    b2.place(x=325, y=300)

    # Create and place a label with a description
    var = StringVar()
    label1 = Label(z10, textvariable=var, relief=RAISED, justify=LEFT, font=('LITHOGRAPH', 12,'bold'), bg='#f8939c', bd=0, fg='white')
    var.set("Greek cheese pies with a mix of feta and ricotta.")
    label1.place(x=70, y=350)

    # Create and place a label with the price
    var1 = StringVar()
    label2 = Label(z10, textvariable=var1, relief=RAISED, justify=LEFT, font=('LITHOGRAPH', 25, 'bold'), bg='#f8939c', bd=0, fg='white')
    var1.set("₱25 each")
    price10 = 25
    
    label2.place(x=70, y=420)
    z10.title("Tiropita")

def Napoleon():
    global z11
    z11 = Toplevel(w)

    # Update idle tasks to ensure the window size is calculated
    z11.update_idletasks()
    
    window_width = 475
    window_height = 550
    
    # Get screen width and height
    screen_width = z11.winfo_screenwidth()
    screen_height = z11.winfo_screenheight()
    
    # Calculate position x, y
    position_x = int((screen_width / 2) - (window_width / 2))
    position_y = int((screen_height / 2) - (window_height / 2))
    
    # Set the geometry of the window
    z11.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")
    
    z11.iconphoto(False, icon)

    z11.resizable(0, 0)
    z11.focus_set()
    
    canvas = Canvas(z11, width=550, height=550, bg='#f8939c')  # Update canvas size
    canvas.pack(expand=YES, fill=BOTH)
    
    # Load and create the back button
    photox = PhotoImage(file=r"Resources\backbutton.png")
    back = Button(z11, image=photox, compound=TOP, command=z11.withdraw)
    back.image = photox
    back.place(x=410, y=10)

    # Load and create the Fruit Tart button
    photo1 = PhotoImage(file=r"Resources\PUFF PASTRY\NAPOLEON.png")
    b11 = Button(z11, text='Napoleon', image=photo1, compound=TOP, font=('LITHOGRAPH',15,'bold'), fg="white", bg="#f8939c",bd=0)
    b11.image = photo1
    b11.place(x=70, y=100)

    def add():
        global count11
        count11 = count11 + 1
        if count11 >= 10:
            count11 = 10
            txtbox.delete("1.0", END)
            txtbox.insert(END, count11)
        else:
            txtbox.delete("1.0", END)
            txtbox.insert(END, count11)
    
    def sub():
        global count11
        count11 = max(count11 - 1, 1)  # Limit count to 0
        txtbox.delete("1.0", END)
        txtbox.insert(END, count11)
    
    def cnf():
        global total11
        global count11
        global bc1
        global bc2
        global bc3
        global bc4
        global bc5
        global bc6
        global bc7
        global bc8
        global bc9
        global bc10
        total11 = price11 * count11
        if bc1 == 1:
            db.insert1('Napoleon', count11, price11, total11)
        elif bc2 == 1:
            db.insert2('Napoleon', count11, price11, total11)
        elif bc3 == 1:
            db.insert3('Napoleon', count11, price11, total11)
        elif bc4 == 1:
            db.insert4('Napoleon', count11, price11, total11)
        elif bc5 == 1:
            db.insert5('Napoleon', count11, price11, total11)
        elif bc6 == 1:
            db.insert6('Napoleon', count11, price11, total11)
        elif bc7 == 1:
            db.insert7('Napoleon', count11, price11, total11)
        elif bc8 == 1:
            db.insert8('Napoleon', count11, price11, total11)
        elif bc9 == 1:
            db.insert9('Napoleon', count11, price11, total11)
        elif bc10 == 1:
            db.insert10('Napoleon', count11, price11, total11)
        count11 = 1
        total11 = 0
        z11.destroy()

    # Create and place the text box to display count
    txtbox = Text(z11, height=0.5, width=5, bd=0, font=('LITHOGRAPH',15,'bold'), fg="white", bg="#f8939c")
    txtbox.place(x=368, y=165)
    txtbox.insert('1.0', count11)
    
    # Create and place the plus button
    plus = Button(z11, text='+', font=('arial', 16, 'bold'), width=5, fg="#f8939c", bg="white", command=add)
    plus.place(x=340, y=100)

    # Create and place the minus button
    minus = Button(z11, text='-', font=('arial', 16, 'bold'), width=5, fg="#f8939c", bg="white", command=sub)
    minus.place(x=340, y=220)

    # Create and place the confirm button
    b2 = Button(z11, text='Confirm Order', compound=TOP, font=('LITHOGRAPH',12,'bold'), bd=0, fg="#f8939c", bg="white", command=cnf)
    b2.place(x=325, y=300)

    # Create and place a label with a description
    var = StringVar()
    label1 = Label(z11, textvariable=var, relief=RAISED, justify=LEFT, font=('LITHOGRAPH', 12,'bold'), bg='#f8939c', bd=0, fg='white')
    var.set("Layers of puff pastry filled with pastry\ncream and topped with icing.")
    label1.place(x=70, y=350)

    # Create and place a label with the price
    var1 = StringVar()
    label2 = Label(z11, textvariable=var1, relief=RAISED, justify=LEFT, font=('LITHOGRAPH', 25, 'bold'), bg='#f8939c', bd=0, fg='white')
    var1.set("₱30 each")
    price11 = 30
    
    label2.place(x=70, y=420)
    z11.title("Napoleon")
    

def Beef():
    global z12
    z12 = Toplevel(w)

    # Update idle tasks to ensure the window size is calculated
    z12.update_idletasks()
    
    window_width = 475
    window_height = 550
    
    # Get screen width and height
    screen_width = z12.winfo_screenwidth()
    screen_height = z12.winfo_screenheight()
    
    # Calculate position x, y
    position_x = int((screen_width / 2) - (window_width / 2))
    position_y = int((screen_height / 2) - (window_height / 2))
    
    # Set the geometry of the window
    z12.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")
    
    z12.iconphoto(False, icon)

    z12.resizable(0, 0)
    z12.focus_set()
    
    canvas = Canvas(z12, width=550, height=550, bg='#f8939c')  # Update canvas size
    canvas.pack(expand=YES, fill=BOTH)
    
    # Load and create the back button
    photox = PhotoImage(file=r"Resources\backbutton.png")
    back = Button(z12, image=photox, compound=TOP, command=z12.withdraw)
    back.image = photox
    back.place(x=410, y=10)

    # Load and create the Fruit Tart button
    photo1 = PhotoImage(file=r"Resources\PUFF PASTRY\BEEF WELLINGTON.png")
    b12 = Button(z12, text='Beef Wellington', image=photo1, compound=TOP, font=('LITHOGRAPH',15,'bold'), fg="white", bg="#f8939c",bd=0)
    b12.image = photo1
    b12.place(x=70, y=100)

    def add():
        global count12
        count12 = count12 + 1
        if count12 >= 10:
            count12 = 10
            txtbox.delete("1.0", END)
            txtbox.insert(END, count12)
        else:
            txtbox.delete("1.0", END)
            txtbox.insert(END, count12)
    
    def sub():
        global count12
        count12 = max(count12 - 1, 1)  # Limit count to 0
        txtbox.delete("1.0", END)
        txtbox.insert(END, count12)
    
    def cnf():
        global total12
        global count12
        global bc1
        global bc2
        global bc3
        global bc4
        global bc5
        global bc6
        global bc7
        global bc8
        global bc9
        global bc10
        total12 = price12 * count12
        if(bc1==1):
            db.insert1('Beef Wellington',count12,price12,total12)
        elif(bc2==1):
            db.insert2('Beef Wellington',count12,price12,total12)
        elif(bc3==1):
            db.insert3('Beef Wellington',count12,price12,total12)
        elif(bc4==1):
            db.insert4('Beef Wellington',count12,price12,total12)
        elif(bc5==1):           
            db.insert5('Beef Wellington',count12,price12,total12)
        elif(bc6==1):            
            db.insert6('Beef Wellington',count12,price12,total12)
        elif(bc7==1):           
            db.insert7('Beef Wellington',count12,price12,total12)
        elif(bc8==1):            
            db.insert8('Beef Wellington',count12,price12,total12)
        elif(bc9==1):            
            db.insert9('Beef Wellington',count12,price12,total12)
        elif(bc10==1):
            db.insert10('Beef Wellington',count12,price12,total12)
        count12=1
        total12=0
        z12.destroy()

    # Create and place the text box to display count
    txtbox = Text(z12, height=0.5, width=5, bd=0, font=('LITHOGRAPH',15,'bold'), fg="white", bg="#f8939c")
    txtbox.place(x=368, y=165)
    txtbox.insert('1.0', count12)
    
    # Create and place the plus button
    plus = Button(z12, text='+', font=('arial', 16, 'bold'), width=5, fg="#f8939c", bg="white", command=add)
    plus.place(x=340, y=100)

    # Create and place the minus button
    minus = Button(z12, text='-', font=('arial', 16, 'bold'), width=5, fg="#f8939c", bg="white", command=sub)
    minus.place(x=340, y=220)

    # Create and place the confirm button
    b2 = Button(z12, text='Confirm Order', compound=TOP, font=('LITHOGRAPH',12,'bold'), bd=0, fg="#f8939c", bg="white", command=cnf)
    b2.place(x=325, y=300)

    # Create and place a label with a description
    var = StringVar()
    label1 = Label(z12, textvariable=var, relief=RAISED, justify=LEFT, font=('LITHOGRAPH', 12,'bold'), bg='#f8939c', bd=0, fg='white')
    var.set("A filet of beef wrapped in\npuff pastry and baked.")
    label1.place(x=70, y=350)

    # Create and place a label with the price
    var1 = StringVar()
    label2 = Label(z12, textvariable=var1, relief=RAISED, justify=LEFT, font=('LITHOGRAPH', 25, 'bold'), bg='#f8939c', bd=0, fg='white')
    var1.set("₱70 each")
    price12 = 70
    
    label2.place(x=70, y=420)
    z12.title("Beef Wellington")


def Croissant():
    global z13
    z13 = Toplevel(w)

    # Update idle tasks to ensure the window size is calculated
    z13.update_idletasks()
    
    window_width = 475
    window_height = 550
    
    # Get screen width and height
    screen_width = z13.winfo_screenwidth()
    screen_height = z13.winfo_screenheight()
    
    # Calculate position x, y
    position_x = int((screen_width / 2) - (window_width / 2))
    position_y = int((screen_height / 2) - (window_height / 2))
    
    # Set the geometry of the window
    z13.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")
    
    z13.iconphoto(False, icon)

    z13.resizable(0, 0)
    z13.focus_set()
    
    canvas = Canvas(z13, width=550, height=550, bg='#f8939c')  # Update canvas size
    canvas.pack(expand=YES, fill=BOTH)
    
    # Load and create the back button
    photox = PhotoImage(file=r"Resources\backbutton.png")
    back = Button(z13, image=photox, compound=TOP, command=z13.withdraw)
    back.image = photox
    back.place(x=410, y=10)

    # Load and create the Fruit Tart button
    photo1 = PhotoImage(file=r"Resources\PUFF PASTRY\CROISSANT.png")
    b13 = Button(z13, text='Croissant', image=photo1, compound=TOP, font=('LITHOGRAPH',15,'bold'), fg="white", bg="#f8939c",bd=0)
    b13.image = photo1
    b13.place(x=70, y=100)

    def add():
        global count13
        count13 = count13 + 1
        if count13 >= 10:
            count13 = 10
            txtbox.delete("1.0", END)
            txtbox.insert(END, count13)
        else:
            txtbox.delete("1.0", END)
            txtbox.insert(END, count13)
    
    def sub():
        global count13
        count13 = max(count13 - 1, 1)  # Limit count to 0
        txtbox.delete("1.0", END)
        txtbox.insert(END, count13)
    
    def cnf():
        global total13
        global count13
        global bc1
        global bc2
        global bc3
        global bc4
        global bc5
        global bc6
        global bc7
        global bc8
        global bc9
        global bc10
        total13 = price13 * count13
        if(bc1==1):
            db.insert1('Croissant',count13,price13,total13)
        elif(bc2==1):
            db.insert2('Croissant',count13,price13,total13)
        elif(bc3==1):
            db.insert3('Croissant',count13,price13,total13)
        elif(bc4==1):
            db.insert4('Croissant',count13,price13,total13)
        elif(bc5==1):           
            db.insert5('Croissant',count13,price13,total13)
        elif(bc6==1):            
            db.insert6('Croissant',count13,price13,total13)
        elif(bc7==1):           
            db.insert7('Croissant',count13,price13,total13)
        elif(bc8==1):            
            db.insert8('Croissant',count13,price13,total13)
        elif(bc9==1):            
            db.insert9('Croissant',count13,price13,total13)
        elif(bc10==1):
            db.insert10('Croissant',count13,price13,total13)
        count13=1
        total13=0
        z13.destroy()

    # Create and place the text box to display count
    txtbox = Text(z13, height=0.5, width=5, bd=0, font=('LITHOGRAPH',15,'bold'), fg="white", bg="#f8939c")
    txtbox.place(x=368, y=165)
    txtbox.insert('1.0', count13)
    
    # Create and place the plus button
    plus = Button(z13, text='+', font=('arial', 16, 'bold'), width=5, fg="#f8939c", bg="white", command=add)
    plus.place(x=340, y=100)

    # Create and place the minus button
    minus = Button(z13, text='-', font=('arial', 16, 'bold'), width=5, fg="#f8939c", bg="white", command=sub)
    minus.place(x=340, y=220)

    # Create and place the confirm button
    b13 = Button(z13, text='Confirm Order', compound=TOP, font=('LITHOGRAPH',12,'bold'), bd=0, fg="#f8939c", bg="white", command=cnf)
    b13.place(x=325, y=300)

    # Create and place a label with a description
    var = StringVar()
    label1 = Label(z13, textvariable=var, relief=RAISED, justify=LEFT, font=('LITHOGRAPH', 12,'bold'), bg='#f8939c', bd=0, fg='white')
    var.set("A buttery, flaky, and crescent-shaped pastry.")
    label1.place(x=70, y=350)

    # Create and place a label with the price
    var1 = StringVar()
    label2 = Label(z13, textvariable=var1, relief=RAISED, justify=LEFT, font=('LITHOGRAPH', 25, 'bold'), bg='#f8939c', bd=0, fg='white')
    var1.set("₱30 each")
    price13 = 30
    
    label2.place(x=70, y=420)
    z13.title("Croissant")


def Pain():
    global z14
    z14 = Toplevel(w)

    # Update idle tasks to ensure the window size is calculated
    z14.update_idletasks()
    
    window_width = 475
    window_height = 550
    
    # Get screen width and height
    screen_width = z14.winfo_screenwidth()
    screen_height = z14.winfo_screenheight()
    
    # Calculate position x, y
    position_x = int((screen_width / 2) - (window_width / 2))
    position_y = int((screen_height / 2) - (window_height / 2))
    
    # Set the geometry of the window
    z14.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")
    
    z14.iconphoto(False, icon)

    z14.resizable(0, 0)
    z14.focus_set()
    
    canvas = Canvas(z14, width=550, height=550, bg='#f8939c')  # Update canvas size
    canvas.pack(expand=YES, fill=BOTH)
    
    # Load and create the back button
    photox = PhotoImage(file=r"Resources\backbutton.png")
    back = Button(z14, image=photox, compound=TOP, command=z14.withdraw)
    back.image = photox
    back.place(x=410, y=10)

    # Load and create the Fruit Tart button
    photo1 = PhotoImage(file=r"Resources\PUFF PASTRY\PAIN AU CHOCOLAT.png")
    b14 = Button(z14, text='Pain au Chocolat', image=photo1, compound=TOP, font=('LITHOGRAPH',15,'bold'), fg="white", bg="#f8939c",bd=0)
    b14.image = photo1
    b14.place(x=70, y=100)

    def add():
        global count14
        count14 = count14 + 1
        if count14 >= 10:
            count14 = 10
            txtbox.delete("1.0", END)
            txtbox.insert(END, count14)
        else:
            txtbox.delete("1.0", END)
            txtbox.insert(END, count14)
    
    def sub():
        global count14
        count14 = max(count14 - 1, 1)  # Limit count to 0
        txtbox.delete("1.0", END)
        txtbox.insert(END, count14)
    
    def cnf():
        global total14
        global count14
        global bc1
        global bc2
        global bc3
        global bc4
        global bc5
        global bc6
        global bc7
        global bc8
        global bc9
        global bc10
        total14 = price14 * count14
        if(bc1==1):
            db.insert1('Pain au Chocolat',count14,price14,total14)
        elif(bc2==1):
            db.insert2('Pain au Chocolat',count14,price14,total14)
        elif(bc3==1):
            db.insert3('Pain au Chocolat',count14,price14,total14)
        elif(bc4==1):
            db.insert4('Pain au Chocolat',count14,price14,total14)
        elif(bc5==1):           
            db.insert5('Pain au Chocolat',count14,price14,total14)
        elif(bc6==1):            
            db.insert6('Pain au Chocolat',count14,price14,total14)
        elif(bc7==1):           
            db.insert7('Pain au Chocolat',count14,price14,total14)
        elif(bc8==1):            
            db.insert8('Pain au Chocolat',count14,price14,total14)
        elif(bc9==1):            
            db.insert9('Pain au Chocolat',count14,price14,total14)
        elif(bc10==1):
            db.insert10('Pain au Chocolat',count14,price14,total14)
        count14=1
        total14=0
        z14.destroy()

    # Create and place the text box to display count
    txtbox = Text(z14, height=0.5, width=5, bd=0, font=('LITHOGRAPH',15,'bold'), fg="white", bg="#f8939c")
    txtbox.place(x=368, y=165)
    txtbox.insert('1.0', count14)
    
    # Create and place the plus button
    plus = Button(z14, text='+', font=('arial', 16, 'bold'), width=5, fg="#f8939c", bg="white", command=add)
    plus.place(x=340, y=100)

    # Create and place the minus button
    minus = Button(z14, text='-', font=('arial', 16, 'bold'), width=5, fg="#f8939c", bg="white", command=sub)
    minus.place(x=340, y=220)

    # Create and place the confirm button
    b2 = Button(z14, text='Confirm Order', compound=TOP, font=('LITHOGRAPH',12,'bold'), bd=0, fg="#f8939c", bg="white", command=cnf)
    b2.place(x=325, y=300)

    # Create and place a label with a description
    var = StringVar()
    label1 = Label(z14, textvariable=var, relief=RAISED, justify=LEFT, font=('LITHOGRAPH', 12,'bold'), bg='#f8939c', bd=0, fg='white')
    var.set("A puff pastry filled with dark chocolate.")
    label1.place(x=70, y=350)

    # Create and place a label with the price
    var1 = StringVar()
    label2 = Label(z14, textvariable=var1, relief=RAISED, justify=LEFT, font=('LITHOGRAPH', 25, 'bold'), bg='#f8939c', bd=0, fg='white')
    var1.set("₱30 each")
    price14 = 30
    
    label2.place(x=70, y=420)
    z14.title("Pain au Chocolat")

def Volauvent():
    global z15
    z15 = Toplevel(w)

    # Update idle tasks to ensure the window size is calculated
    z15.update_idletasks()
    
    window_width = 475
    window_height = 550
    
    # Get screen width and height
    screen_width = z15.winfo_screenwidth()
    screen_height = z15.winfo_screenheight()
    
    # Calculate position x, y
    position_x = int((screen_width / 2) - (window_width / 2))
    position_y = int((screen_height / 2) - (window_height / 2))
    
    # Set the geometry of the window
    z15.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")
    
    z15.iconphoto(False, icon)

    z15.resizable(0, 0)
    z15.focus_set()
    
    canvas = Canvas(z15, width=550, height=550, bg='#f8939c')  # Update canvas size
    canvas.pack(expand=YES, fill=BOTH)
    
    # Load and create the back button
    photox = PhotoImage(file=r"Resources\backbutton.png")
    back = Button(z15, image=photox, compound=TOP, command=z15.withdraw)
    back.image = photox
    back.place(x=410, y=10)

    # Load and create the Fruit Tart button
    photo1 = PhotoImage(file=r"Resources\FLAKY PASTRY\VOL-AU-VENT.png")
    b15 = Button(z15, text='Vol-au-vent', image=photo1, compound=TOP, font=('LITHOGRAPH',15,'bold'), fg="white", bg="#f8939c",bd=0)
    b15.image = photo1
    b15.place(x=70, y=100)

    def add():
        global count15
        count15 = count15 + 1
        if count15 >= 10:
            count15 = 10
            txtbox.delete("1.0", END)
            txtbox.insert(END, count15)
        else:
            txtbox.delete("1.0", END)
            txtbox.insert(END, count15)
    
    def sub():
        global count15
        count15 = max(count15 - 1, 1)  # Limit count to 0
        txtbox.delete("1.0", END)
        txtbox.insert(END, count15)
    
    def cnf():
        global total15
        global count15
        global bc1
        global bc2
        global bc3
        global bc4
        global bc5
        global bc6
        global bc7
        global bc8
        global bc9
        global bc10
        total15 = price15 * count15

        if(bc1==1):
            db.insert1('Vol-au-vent',count15,price15,total15)
        elif(bc2==1):
            db.insert2('Vol-au-vent',count15,price15,total15)
        elif(bc3==1):
            db.insert3('Vol-au-vent',count15,price15,total15)
        elif(bc4==1):
            db.insert4('Vol-au-vent',count15,price15,total15)
        elif(bc5==1):           
            db.insert5('Vol-au-vent',count15,price15,total15)
        elif(bc6==1):            
            db.insert6('Vol-au-vent',count15,price15,total15)
        elif(bc7==1):           
            db.insert7('Vol-au-vent',count15,price15,total15)
        elif(bc8==1):
            db.insert8('Vol-au-vent',count15,price15,total15)
        elif(bc9==1):            
            db.insert9('Vol-au-vent',count15,price15,total15)
        elif(bc10==1):
            db.insert10('Vol-au-vent',count15,price15,total15)
        count15=1
        total15=0
        z15.destroy()

    # Create and place the text box to display count
    txtbox = Text(z15, height=0.5, width=5, bd=0, font=('LITHOGRAPH',15,'bold'), fg="white", bg="#f8939c")
    txtbox.place(x=368, y=165)
    txtbox.insert('1.0', count15)
    
    # Create and place the plus button
    plus = Button(z15, text='+', font=('arial', 16, 'bold'), width=5, fg="#f8939c", bg="white", command=add)
    plus.place(x=340, y=100)

    # Create and place the minus button
    minus = Button(z15, text='-', font=('arial', 16, 'bold'), width=5, fg="#f8939c", bg="white", command=sub)
    minus.place(x=340, y=220)

    # Create and place the confirm button
    b2 = Button(z15, text='Confirm Order', compound=TOP, font=('LITHOGRAPH',12,'bold'), bd=0, fg="#f8939c", bg="white", command=cnf)
    b2.place(x=325, y=300)

    # Create and place a label with a description
    var = StringVar()
    label1 = Label(z15, textvariable=var, relief=RAISED, justify=LEFT, font=('LITHOGRAPH', 12,'bold'), bg='#f8939c', bd=0, fg='white')
    var.set("Puff pastry shells filled with savory\ningredients like seafood or mushrooms.")
    label1.place(x=70, y=350)

    # Create and place a label with the price
    var1 = StringVar()
    label2 = Label(z15, textvariable=var1, relief=RAISED, justify=LEFT, font=('LITHOGRAPH', 25, 'bold'), bg='#f8939c', bd=0, fg='white')
    var1.set("₱30 each")
    price15 = 30
    
    label2.place(x=70, y=420)
    z15.title("Vol-au-vent")

def Palmiers():
    global z16
    z16 = Toplevel(w)

    # Update idle tasks to ensure the window size is calculated
    z16.update_idletasks()
    
    window_width = 475
    window_height = 550
    
    # Get screen width and height
    screen_width = z16.winfo_screenwidth()
    screen_height = z16.winfo_screenheight()
    
    # Calculate position x, y
    position_x = int((screen_width / 2) - (window_width / 2))
    position_y = int((screen_height / 2) - (window_height / 2))
    
    # Set the geometry of the window
    z16.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")
    
    z16.iconphoto(False, icon)

    z16.resizable(0, 0)
    z16.focus_set()
    
    canvas = Canvas(z16, width=550, height=550, bg='#f8939c')  # Update canvas size
    canvas.pack(expand=YES, fill=BOTH)
    
    # Load and create the back button
    photox = PhotoImage(file=r"Resources\backbutton.png")
    back = Button(z16, image=photox, compound=TOP, command=z16.withdraw)
    back.image = photox
    back.place(x=410, y=10)

    # Load and create the Fruit Tart button
    photo1 = PhotoImage(file=r"Resources\FLAKY PASTRY\PALMIERS.png")
    b16 = Button(z16, text='Palmiers', image=photo1, compound=TOP, font=('LITHOGRAPH', 15, 'bold'), fg="white", bg="#f8939c", bd=0)
    b16.image = photo1
    b16.place(x=70, y=100)

    def add():
        global count16
        count16 = count16 + 1
        if count16 >= 10:
            count16 = 10
            txtbox.delete("1.0", END)
            txtbox.insert(END, count16)
        else:
            txtbox.delete("1.0", END)
            txtbox.insert(END, count16)
    
    def sub():
        global count16
        count16 = max(count16 - 1, 1)  # Limit count to 0
        txtbox.delete("1.0", END)
        txtbox.insert(END, count16)
    
    def cnf():
        global total16
        global count16
        global bc1
        global bc2
        global bc3
        global bc4
        global bc5
        global bc6
        global bc7
        global bc8
        global bc9
        global bc10
        total16 = price16 * count16
        if(bc1==1):
            db.insert1('Palmiers',count16,price16,total16)
        elif(bc2==1):
            db.insert2('Palmiers',count16,price16,total16)
        elif(bc3==1):
            db.insert3('Palmiers',count16,price16,total16)
        elif(bc4==1):
            db.insert4('Palmiers',count16,price16,total16)
        elif(bc5==1):           
            db.insert5('Palmiers',count16,price16,total16)
        elif(bc6==1):            
            db.insert6('Palmiers',count16,price16,total16)
        elif(bc7==1):           
            db.insert7('Palmiers',count16,price16,total16)
        elif(bc8==1):            
            db.insert8('Palmiers',count16,price16,total16)
        elif(bc9==1):            
            db.insert9('Palmiers',count16,price16,total16)
        elif(bc10==1):
            db.insert10('Palmiers',count16,price16,total16)
        count16=1
        total16=0
        z16.destroy()

    # Create and place the text box to display count
    txtbox = Text(z16, height=0.5, width=5, bd=0, font=('LITHOGRAPH', 15, 'bold'), fg="white", bg="#f8939c")
    txtbox.place(x=368, y=165)
    txtbox.insert('1.0', count16)
    
    # Create and place the plus button
    plus = Button(z16, text='+', font=('arial', 16, 'bold'), width=5, fg="#f8939c", bg="white", command=add)
    plus.place(x=340, y=100)

    # Create and place the minus button
    minus = Button(z16, text='-', font=('arial', 16, 'bold'), width=5, fg="#f8939c", bg="white", command=sub)
    minus.place(x=340, y=220)

    # Create and place the confirm button
    b2 = Button(z16, text='Confirm Order', compound=TOP, font=('LITHOGRAPH', 12, 'bold'), bd=0, fg="#f8939c", bg="white", command=cnf)
    b2.place(x=325, y=300)

    # Create and place a label with a description
    var = StringVar()
    label1 = Label(z16, textvariable=var, relief=RAISED, justify=LEFT, font=('LITHOGRAPH', 12, 'bold'), bg='#f8939c', bd=0, fg='white')
    var.set("Sweet, crisp, and caramelized pastries\nalso known as elephant ears.")
    label1.place(x=70, y=350)

    # Create and place a label with the price
    var1 = StringVar()
    label2 = Label(z16, textvariable=var1, relief=RAISED, justify=LEFT, font=('LITHOGRAPH', 25, 'bold'), bg='#f8939c', bd=0, fg='white')
    var1.set("₱30 each")
    price16 = 30
    
    label2.place(x=70, y=420)
    z16.title("Palmiers")

def Eccles():
    global z17
    z17 = Toplevel(w)

    # Update idle tasks to ensure the window size is calculated
    z17.update_idletasks()
    
    window_width = 475
    window_height = 550
    
    # Get screen width and height
    screen_width = z17.winfo_screenwidth()
    screen_height = z17.winfo_screenheight()
    
    # Calculate position x, y
    position_x = int((screen_width / 2) - (window_width / 2))
    position_y = int((screen_height / 2) - (window_height / 2))
    
    # Set the geometry of the window
    z17.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")
    
    z17.iconphoto(False, icon)

    z17.resizable(0, 0)
    z17.focus_set()
    
    canvas = Canvas(z17, width=550, height=550, bg='#f8939c')  # Update canvas size
    canvas.pack(expand=YES, fill=BOTH)
    
    # Load and create the back button
    photox = PhotoImage(file=r"Resources\backbutton.png")
    back = Button(z17, image=photox, compound=TOP, command=z17.withdraw)
    back.image = photox
    back.place(x=410, y=10)

    # Load and create the Fruit Tart button
    photo1 = PhotoImage(file=r"Resources\FLAKY PASTRY\ECCLES CAKES.png")
    b17 = Button(z17, text='Eccles Cakes', image=photo1, compound=TOP, font=('LITHOGRAPH',15,'bold'), fg="white", bg="#f8939c",bd=0)
    b17.image = photo1
    b17.place(x=70, y=100)

    def add():
        global count17
        count17 = count17 + 1
        if count17 >= 10:
            count17 = 10
            txtbox.delete("1.0", END)
            txtbox.insert(END, count17)
        else:
            txtbox.delete("1.0", END)
            txtbox.insert(END, count17)
    
    def sub():
        global count17
        count17 = max(count17 - 1, 1)  # Limit count to 0
        txtbox.delete("1.0", END)
        txtbox.insert(END, count17)
    
    def cnf():
        global total17
        global count17
        global bc1
        global bc2
        global bc3
        global bc4
        global bc5
        global bc6
        global bc7
        global bc8
        global bc9
        global bc10
        total17 = price17 * count17
        if(bc1==1):
            db.insert1('Eccles Cakes',count17,price17,total17)
        elif(bc2==1):
            db.insert2('Eccles Cakes',count17,price17,total17)
        elif(bc3==1):
            db.insert3('Eccles Cakes',count17,price17,total17)
        elif(bc4==1):
            db.insert4('Eccles Cakes',count17,price17,total17)
        elif(bc5==1):           
            db.insert5('Eccles Cakes',count17,price17,total17)
        elif(bc6==1):            
            db.insert6('Eccles Cakes',count17,price17,total17)
        elif(bc7==1):           
            db.insert7('Eccles Cakes',count17,price17,total17)
        elif(bc8==1):            
            db.insert8('Eccles Cakes',count17,price17,total17)
        elif(bc9==1):            
            db.insert9('Eccles Cakes',count17,price17,total17)
        elif(bc10==1):
            db.insert10('Eccles Cakes',count17,price17,total17)
        count17=1
        total17=0
        z17.destroy()

    # Create and place the text box to display count
    txtbox = Text(z17, height=0.5, width=5, bd=0, font=('LITHOGRAPH',15,'bold'), fg="white", bg="#f8939c")
    txtbox.place(x=368, y=165)
    txtbox.insert('1.0', count17)

    # Create and place the plus button
    plus = Button(z17, text='+', font=('arial', 16, 'bold'), width=5, fg="#f8939c", bg="white", command=add)
    plus.place(x=340, y=100)

    # Create and place the minus button
    minus = Button(z17, text='-', font=('arial', 16, 'bold'), width=5, fg="#f8939c", bg="white", command=sub)
    minus.place(x=340, y=220)

    # Create and place the confirm button
    b2 = Button(z17, text='Confirm Order', compound=TOP, font=('LITHOGRAPH',12,'bold'), bd=0, fg="#f8939c", bg="white", command=cnf)
    b2.place(x=325, y=300)

    # Create and place a label with a description
    var = StringVar()
    label1 = Label(z17, textvariable=var, relief=RAISED, justify=LEFT, font=('LITHOGRAPH', 12,'bold'), bg='#f8939c', bd=0, fg='white')
    var.set("Small, round pastries filled with currants\nand topped with sugar.")
    label1.place(x=70, y=350)

    # Create and place a label with the price
    var1 = StringVar()
    label2 = Label(z17, textvariable=var1, relief=RAISED, justify=LEFT, font=('LITHOGRAPH', 25, 'bold'), bg='#f8939c', bd=0, fg='white')
    var1.set("₱50 each")
    price17 = 50

    label2.place(x=70, y=420)
    z17.title("Eccles Cakes")

def Pasties():
    global z18
    z18 = Toplevel(w)

    # Update idle tasks to ensure the window size is calculated
    z18.update_idletasks()
    
    window_width = 475
    window_height = 550
    
    # Get screen width and height
    screen_width = z18.winfo_screenwidth()
    screen_height = z18.winfo_screenheight()
    
    # Calculate position x, y
    position_x = int((screen_width / 2) - (window_width / 2))
    position_y = int((screen_height / 2) - (window_height / 2))
    
    # Set the geometry of the window
    z18.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")
    
    z18.iconphoto(False, icon)

    z18.resizable(0, 0)
    z18.focus_set()
    
    canvas = Canvas(z18, width=550, height=550, bg='#f8939c')  # Update canvas size
    canvas.pack(expand=YES, fill=BOTH)
    
    # Load and create the back button
    photox = PhotoImage(file=r"Resources\backbutton.png")
    back = Button(z18, image=photox, compound=TOP, command=z18.withdraw)
    back.image = photox
    back.place(x=410, y=10)

    # Load and create the Fruit Tart button
    photo1 = PhotoImage(file=r"Resources\FLAKY PASTRY\PASTIES.png")
    b18 = Button(z18, text='Pasties', image=photo1, compound=TOP, font=('LITHOGRAPH',15,'bold'), fg="white", bg="#f8939c",bd=0)
    b18.image = photo1
    b18.place(x=70, y=100)

    def add():
        global count18
        count18 = count18 + 1
        if count18 >= 10:
            count18 = 10
            txtbox.delete("1.0", END)
            txtbox.insert(END, count18)
        else:
            txtbox.delete("1.0", END)
            txtbox.insert(END, count18)
    
    def sub():
        global count18
        count18 = max(count18 - 1, 1)  # Limit count to 1
        txtbox.delete("1.0", END)
        txtbox.insert(END, count18)
    
    def cnf():
        global total18
        global count18
        global bc1
        global bc2
        global bc3
        global bc4
        global bc5
        global bc6
        global bc7
        global bc8
        global bc9
        global bc10
        total18 = price18 * count18
        if(bc1==1):
            db.insert1('Pasties',count18,price18,total18)
        elif(bc2==1):
            db.insert2('Pasties',count18,price18,total18)
        elif(bc3==1):
            db.insert3('Pasties',count18,price18,total18)
        elif(bc4==1):
            db.insert4('Pasties',count18,price18,total18)
        elif(bc5==1):           
            db.insert5('Pasties',count18,price18,total18)
        elif(bc6==1):            
            db.insert6('Pasties',count18,price18,total18)
        elif(bc7==1):           
            db.insert7('Pasties',count18,price18,total18)
        elif(bc8==1):            
            db.insert8('Pasties',count18,price18,total18)
        elif(bc9==1):            
            db.insert9('Pasties',count18,price18,total18)
        elif(bc10==1):
            db.insert10('Pasties',count18,price18,total18)
        count18=1
        total18=0
        z18.destroy()

    # Create and place the text box to display count
    txtbox = Text(z18, height=0.5, width=5, bd=0, font=('LITHOGRAPH',15,'bold'), fg="white", bg="#f8939c")
    txtbox.place(x=368, y=165)
    txtbox.insert('1.0', count18)
    
    # Create and place the plus button
    plus = Button(z18, text='+', font=('arial', 16, 'bold'), width=5, fg="#f8939c", bg="white", command=add)
    plus.place(x=340, y=100)

    # Create and place the minus button
    minus = Button(z18, text='-', font=('arial', 16, 'bold'), width=5, fg="#f8939c", bg="white", command=sub)
    minus.place(x=340, y=220)

    # Create and place the confirm button
    b2 = Button(z18, text='Confirm Order', compound=TOP, font=('LITHOGRAPH',12,'bold'), bd=0, fg="#f8939c", bg="white", command=cnf)
    b2.place(x=325, y=300)

    # Create and place a label with a description
    var = StringVar()
    label1 = Label(z18, textvariable=var, relief=RAISED, justify=LEFT, font=('LITHOGRAPH', 12,'bold'), bg='#f8939c', bd=0, fg='white')
    var.set("Hand-held savory pies, often\nfilled with meat and vegetables.")
    label1.place(x=70, y=350)

    # Create and place a label with the price
    var1 = StringVar()
    label2 = Label(z18, textvariable=var1, relief=RAISED, justify=LEFT, font=('LITHOGRAPH', 25, 'bold'), bg='#f8939c', bd=0, fg='white')
    var1.set("₱40 each")
    price18 = 40
    
    label2.place(x=70, y=420)
    z18.title("Pasties")

def Chicken():
    global z19
    z19 = Toplevel(w)

    # Update idle tasks to ensure the window size is calculated
    z19.update_idletasks()
    
    window_width = 475
    window_height = 550
    
    # Get screen width and height
    screen_width = z19.winfo_screenwidth()
    screen_height = z19.winfo_screenheight()
    
    # Calculate position x, y
    position_x = int((screen_width / 2) - (window_width / 2))
    position_y = int((screen_height / 2) - (window_height / 2))
    
    # Set the geometry of the window
    z19.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")
    
    z19.iconphoto(False, icon)

    z19.resizable(0, 0)
    z19.focus_set()
    
    canvas = Canvas(z19, width=550, height=550, bg='#f8939c')  # Update canvas size
    canvas.pack(expand=YES, fill=BOTH)
    
    # Load and create the back button
    photox = PhotoImage(file=r"Resources\backbutton.png")
    back = Button(z19, image=photox, compound=TOP, command=z19.withdraw)
    back.image = photox
    back.place(x=410, y=10)

    photo1 = PhotoImage(file=r"Resources/FLAKY PASTRY/CHICKEN POT PIE.png")
    b19 = Button(z19, text='Chicken Pot Pie', image=photo1, compound=TOP, font=('LITHOGRAPH',15,'bold'), fg="white", bg="#f8939c",bd=0)
    b19.image = photo1
    b19.place(x=70, y=100)

    def add():
        global count19
        count19 = count19 + 1
        if count19 >= 10:
            count19 = 10
            txtbox.delete("1.0", END)
            txtbox.insert(END, count19)
        else:
            txtbox.delete("1.0", END)
            txtbox.insert(END, count19)
    
    def sub():
        global count19
        count19 = max(count19 - 1, 1)  # Limit count to 0
        txtbox.delete("1.0", END)
        txtbox.insert(END, count19)
    
    def cnf():
        global total19
        global count19
        global bc1
        global bc2
        global bc3
        global bc4
        global bc5
        global bc6
        global bc7
        global bc8
        global bc9
        global bc10
        total19 = price19 * count19

        if(bc1==1):
            db.insert1('Chicken Pot Pie',count19,price19,total19)
        elif(bc2==1):
            db.insert2('Chicken Pot Pie',count19,price19,total19)
        elif(bc3==1):
            db.insert3('Chicken Pot Pie',count19,price19,total19)
        elif(bc4==1):
            db.insert4('Chicken Pot Pie',count19,price19,total19)
        elif(bc5==1):           
            db.insert5('Chicken Pot Pie',count19,price19,total19)
        elif(bc6==1):            
            db.insert6('Chicken Pot Pie',count19,price19,total19)
        elif(bc7==1):           
            db.insert7('Chicken Pot Pie',count19,price19,total19)
        elif(bc8==1):            
            db.insert8('Chicken Pot Pie',count19,price19,total19)
        elif(bc9==1):            
            db.insert9('Chicken Pot Pie',count19,price19,total19)
        elif(bc10==1):
            db.insert10('Chicken Pot Pie',count19,price19,total19)
        count19=1
        total19=0
        z19.destroy()

    # Create and place the text box to display count
    txtbox = Text(z19, height=0.5, width=5, bd=0, font=('LITHOGRAPH',15,'bold'), fg="white", bg="#f8939c")
    txtbox.place(x=368, y=165)
    txtbox.insert('1.0', count19)
    
    # Create and place the plus button
    plus = Button(z19, text='+', font=('arial', 16, 'bold'), width=5, fg="#f8939c", bg="white", command=add)
    plus.place(x=340, y=100)

    # Create and place the minus button
    minus = Button(z19, text='-', font=('arial', 16, 'bold'), width=5, fg="#f8939c", bg="white", command=sub)
    minus.place(x=340, y=220)

    # Create and place the confirm button
    b2 = Button(z19, text='Confirm Order', compound=TOP, font=('LITHOGRAPH',12,'bold'), bd=0, fg="#f8939c", bg="white", command=cnf)
    b2.place(x=325, y=300)

    # Create and place a label with a description
    var = StringVar()
    label1 = Label(z19, textvariable=var, relief=RAISED, justify=LEFT, font=('LITHOGRAPH', 12,'bold'), bg='#f8939c', bd=0, fg='white')
    var.set("A savory pie with a flaky pastry top.")
    label1.place(x=70, y=350)

    # Create and place a label with the price
    var1 = StringVar()
    label2 = Label(z19, textvariable=var1, relief=RAISED, justify=LEFT, font=('LITHOGRAPH', 25, 'bold'), bg='#f8939c', bd=0, fg='white')
    var1.set("₱100 each")
    price19 = 100
    
    label2.place(x=70, y=420)
    z19.title("Chicken Pot Pie")

def Eclair():
    global z20
    z20 = Toplevel(w)

    # Update idle tasks to ensure the window size is calculated
    z20.update_idletasks()
    
    window_width = 475
    window_height = 550
    
    # Get screen width and height
    screen_width = z20.winfo_screenwidth()
    screen_height = z20.winfo_screenheight()
    
    # Calculate position x, y
    position_x = int((screen_width / 2) - (window_width / 2))
    position_y = int((screen_height / 2) - (window_height / 2))
    
    # Set the geometry of the window
    z20.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")
    
    z20.iconphoto(False, icon)

    z20.resizable(0, 0)
    z20.focus_set()
    
    canvas = Canvas(z20, width=550, height=550, bg='#f8939c')  # Update canvas size
    canvas.pack(expand=YES, fill=BOTH)
    
    # Load and create the back button
    photox = PhotoImage(file=r"Resources\backbutton.png")
    back = Button(z20, image=photox, compound=TOP, command=z20.withdraw)
    back.image = photox
    back.place(x=410, y=10)

    # Load and create the Fruit Tart button
    photo1 = PhotoImage(file=r"Resources\CHOUX PASTRY\ECLAIR.png")
    b20 = Button(z20, text='Eclair', image=photo1, compound=TOP, font=('LITHOGRAPH',15,'bold'), fg="white", bg="#f8939c",bd=0)
    b20.image = photo1
    b20.place(x=70, y=100)

    def add():
        global count20
        count20 = count20 + 1
        if count20 >= 10:
            count20 = 10
            txtbox.delete("1.0", END)
            txtbox.insert(END, count20)
        else:
            txtbox.delete("1.0", END)
            txtbox.insert(END, count20)
    
    def sub():
        global count20
        count20 = max(count20 - 1, 1)  # Limit count to 0
        txtbox.delete("1.0", END)
        txtbox.insert(END, count20)
    
    def cnf():
        global total20
        global count20
        global bc1
        global bc2
        global bc3
        global bc4
        global bc5
        global bc6
        global bc7
        global bc8
        global bc9
        global bc10
        total20 = price20 * count20
        if(bc1==1):
            db.insert1('Eclair',count20,price20,total20)
        elif(bc2==1):
            db.insert2('Eclair',count20,price20,total20)
        elif(bc3==1):
            db.insert3('Eclair',count20,price20,total20)
        elif(bc4==1):
            db.insert4('Eclair',count20,price20,total20)
        elif(bc5==1):           
            db.insert5('Eclair',count20,price20,total20)
        elif(bc6==1):            
            db.insert6('Eclair',count20,price20,total20)
        elif(bc7==1):       
            db.insert7('Eclair',count20,price20,total20)
        elif(bc8==1):            
            db.insert8('Eclair',count20,price20,total20)
        elif(bc9==1):            
            db.insert9('Eclair',count20,price20,total20)
        elif(bc10==1):
            db.insert10('Eclair',count20,price20,total20)
        count20=1
        total20=0
        z20.destroy()

    # Create and place the text box to display count
    txtbox = Text(z20, height=0.5, width=5, bd=0, font=('LITHOGRAPH',15,'bold'), fg="white", bg="#f8939c")
    txtbox.place(x=368, y=165)
    txtbox.insert('1.0', count20)
    
    # Create and place the plus button
    plus = Button(z20, text='+', font=('arial', 16, 'bold'), width=5, fg="#f8939c", bg="white", command=add)
    plus.place(x=340, y=100)

    # Create and place the minus button
    minus = Button(z20, text='-', font=('arial', 16, 'bold'), width=5, fg="#f8939c", bg="white", command=sub)
    minus.place(x=340, y=220)

    # Create and place the confirm button
    b2 = Button(z20, text='Confirm Order', compound=TOP, font=('LITHOGRAPH',12,'bold'), bd=0, fg="#f8939c", bg="white", command=cnf)
    b2.place(x=325, y=300)

    # Create and place a label with a description
    var = StringVar()
    label1 = Label(z20, textvariable=var, relief=RAISED, justify=LEFT, font=('LITHOGRAPH', 12,'bold'), bg='#f8939c', bd=0, fg='white')
    var.set("A pastry filled with cream and\ntopped with chocolate glaze.")
    label1.place(x=70, y=350)

    # Create and place a label with the price
    var1 = StringVar()
    label2 = Label(z20, textvariable=var1, relief=RAISED, justify=LEFT, font=('LITHOGRAPH', 25, 'bold'), bg='#f8939c', bd=0, fg='white')
    var1.set("₱60 each")
    price20 = 60
    
    label2.place(x=70, y=420)
    z20.title("Eclair")

def Profiteroles():
    global z21
    z21 = Toplevel(w)

    # Update idle tasks to ensure the window size is calculated
    z21.update_idletasks()
    
    window_width = 475
    window_height = 550
    
    # Get screen width and height
    screen_width = z21.winfo_screenwidth()
    screen_height = z21.winfo_screenheight()
    
    # Calculate position x, y
    position_x = int((screen_width / 2) - (window_width / 2))
    position_y = int((screen_height / 2) - (window_height / 2))
    
    # Set the geometry of the window
    z21.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")
    
    z21.iconphoto(False, icon)

    z21.resizable(0, 0)
    z21.focus_set()
    
    canvas = Canvas(z21, width=550, height=550, bg='#f8939c')  # Update canvas size
    canvas.pack(expand=YES, fill=BOTH)
    
    # Load and create the back button
    photox = PhotoImage(file=r"Resources\backbutton.png")
    back = Button(z21, image=photox, compound=TOP, command=z21.withdraw)
    back.image = photox
    back.place(x=410, y=10)

    # Load and create the Fruit Tart button
    photo1 = PhotoImage(file=r"Resources/CHOUX PASTRY/PROFITEROLES.png")
    b21 = Button(z21, text='Profiteroles', image=photo1, compound=TOP, font=('LITHOGRAPH',15,'bold'), fg="white", bg="#f8939c",bd=0)
    b21.image = photo1
    b21.place(x=70, y=100)

    def add():
        global count21
        count21 = count21 + 1
        if count21 >= 10:
            count21 = 10
            txtbox.delete("1.0", END)
            txtbox.insert(END, count21)
        else:
            txtbox.delete("1.0", END)
            txtbox.insert(END, count21)
    
    def sub():
        global count21
        count21 = max(count21 - 1, 1)  # Limit count to 0
        txtbox.delete("1.0", END)
        txtbox.insert(END, count21)
    
    def cnf():
        global total21
        global count21
        global bc1
        global bc2
        global bc3
        global bc4
        global bc5
        global bc6
        global bc7
        global bc8
        global bc9
        global bc10
        total21 = price21 * count21
        if(bc1==1):
            db.insert1('Profiteroles',count21,price21,total21)
        elif(bc2==1):
            db.insert2('Profiteroles',count21,price21,total21)
        elif(bc3==1):
            db.insert3('Profiteroles',count21,price21,total21)
        elif(bc4==1):
            db.insert4('Profiteroles',count21,price21,total21)
        elif(bc5==1):           
            db.insert5('Profiteroles',count21,price21,total21)
        elif(bc6==1):            
            db.insert6('Profiteroles',count21,price21,total21)
        elif(bc7==1):           
            db.insert7('Profiteroles',count21,price21,total21)
        elif(bc8==1):            
            db.insert8('Profiteroles',count21,price21,total21)
        elif(bc9==1):            
            db.insert9('Profiteroles',count21,price21,total21)
        elif(bc10==1):
            db.insert10('Profiteroles',count21,price21,total21)
        count21=1
        total21=0
        z21.destroy()

    # Create and place the text box to display count
    txtbox = Text(z21, height=0.5, width=5, bd=0, font=('LITHOGRAPH',15,'bold'), fg="white", bg="#f8939c")
    txtbox.place(x=368, y=165)
    txtbox.insert('1.0', count21)
    
    # Create and place the plus button
    plus = Button(z21, text='+', font=('arial', 16, 'bold'), width=5, fg="#f8939c", bg="white", command=add)
    plus.place(x=340, y=100)

    # Create and place the minus button
    minus = Button(z21, text='-', font=('arial', 16, 'bold'), width=5, fg="#f8939c", bg="white", command=sub)
    minus.place(x=340, y=220)

    # Create and place the confirm button
    b2 = Button(z21, text='Confirm Order', compound=TOP, font=('LITHOGRAPH',12,'bold'), bd=0, fg="#f8939c", bg="white", command=cnf)
    b2.place(x=325, y=300)

    # Create and place a label with a description
    var = StringVar()
    label1 = Label(z21, textvariable=var, relief=RAISED, justify=LEFT, font=('LITHOGRAPH', 12,'bold'), bg='#f8939c', bd=0, fg='white')
    var.set("Cream-filled choux balls\noften served with chocolate sauce.")
    label1.place(x=70, y=350)

    # Create and place a label with the price
    var1 = StringVar()
    label2 = Label(z21, textvariable=var1, relief=RAISED, justify=LEFT, font=('LITHOGRAPH', 25, 'bold'), bg='#f8939c', bd=0, fg='white')
    var1.set("₱60 each")
    price21 = 60
    
    label2.place(x=70, y=420)
    z21.title("Profiteroles")

def Paris():
    global z22
    z22 = Toplevel(w)

    # Update idle tasks to ensure the window size is calculated
    z22.update_idletasks()
    
    window_width = 475
    window_height = 550
    
    # Get screen width and height
    screen_width = z22.winfo_screenwidth()
    screen_height = z22.winfo_screenheight()
    
    # Calculate position x, y
    position_x = int((screen_width / 2) - (window_width / 2))
    position_y = int((screen_height / 2) - (window_height / 2))
    
    # Set the geometry of the window
    z22.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")
    
    z22.iconphoto(False, icon)

    z22.resizable(0, 0)
    z22.focus_set()
    
    canvas = Canvas(z22, width=550, height=550, bg='#f8939c')  # Update canvas size
    canvas.pack(expand=YES, fill=BOTH)
    
    # Load and create the back button
    photox = PhotoImage(file=r"Resources\backbutton.png")
    back = Button(z22, image=photox, compound=TOP, command=z22.withdraw)
    back.image = photox
    back.place(x=410, y=10)

    # Load and create the Fruit Tart button
    photo1 = PhotoImage(file=r"Resources\CHOUX PASTRY\PARIS-BREST.png")
    b22 = Button(z22, text='Paris-Brest', image=photo1, compound=TOP, font=('LITHOGRAPH',15,'bold'), fg="white", bg="#f8939c",bd=0)
    b22.image = photo1
    b22.place(x=70, y=100)

    def add():
        global count22
        count22 = count22 + 1
        if count22 >= 10:
            count22 = 10
            txtbox.delete("1.0", END)
            txtbox.insert(END, count22)
        else:
            txtbox.delete("1.0", END)
            txtbox.insert(END, count22)
    
    def sub():
        global count22
        count22 = max(count22 - 1, 1)  # Limit count to 0
        txtbox.delete("1.0", END)
        txtbox.insert(END, count22)
    
    def cnf():
        global total22
        global count22
        global bc1
        global bc2
        global bc3
        global bc4
        global bc5
        global bc6
        global bc7
        global bc8
        global bc9
        global bc10
        total22 = price22 * count22
        if(bc1==1):
            db.insert1('Paris-Brest',count22,price22,total22)
        elif(bc2==1):
            db.insert2('Paris-Brest',count22,price22,total22)
        elif(bc3==1):
            db.insert3('Paris-Brest',count22,price22,total22)
        elif(bc4==1):
            db.insert4('Paris-Brest',count22,price22,total22)
        elif(bc5==1):           
            db.insert5('Paris-Brest',count22,price22,total22)
        elif(bc6==1):            
            db.insert6('Paris-Brest',count22,price22,total22)
        elif(bc7==1):           
            db.insert7('Paris-Brest',count22,price22,total22)
        elif(bc8==1):            
            db.insert8('Paris-Brest',count22,price22,total22)
        elif(bc9==1):            
            db.insert9('Paris-Brest',count22,price22,total22)
        elif(bc10==1):
            db.insert10('Paris-Brest',count22,price22,total22)
        count22=1
        total22=0
        z22.destroy()

    # Create and place the text box to display count
    txtbox = Text(z22, height=0.5, width=5, bd=0, font=('LITHOGRAPH',15,'bold'), fg="white", bg="#f8939c")
    txtbox.place(x=368, y=165)
    txtbox.insert('1.0', count22)
    
    # Create and place the plus button
    plus = Button(z22, text='+', font=('arial', 16, 'bold'), width=5, fg="#f8939c", bg="white", command=add)
    plus.place(x=340, y=100)

    # Create and place the minus button
    minus = Button(z22, text='-', font=('arial', 16, 'bold'), width=5, fg="#f8939c", bg="white", command=sub)
    minus.place(x=340, y=220)

    # Create and place the confirm button
    b22 = Button(z22, text='Confirm Order', compound=TOP, font=('LITHOGRAPH',12,'bold'), bd=0, fg="#f8939c", bg="white", command=cnf)
    b22.place(x=325, y=300)

    # Create and place a label with a description
    var = StringVar()
    label1 = Label(z22, textvariable=var, relief=RAISED, justify=LEFT, font=('LITHOGRAPH', 12,'bold'), bg='#f8939c', bd=0, fg='white')
    var.set("A ring-shaped choux pastry\nfilled with praline-flavored cream")
    label1.place(x=70, y=350)

    # Create and place a label with the price
    var1 = StringVar()
    label2 = Label(z22, textvariable=var1, relief=RAISED, justify=LEFT, font=('LITHOGRAPH', 25, 'bold'), bg='#f8939c', bd=0, fg='white')
    var1.set("₱100 each")
    price22 = 100
    
    label2.place(x=70, y=420)
    z22.title("Paris-Brest")

def Croquembouche():
    global z23
    z23 = Toplevel(w)

    # Update idle tasks to ensure the window size is calculated
    z23.update_idletasks()
    
    window_width = 475
    window_height = 550
    
    # Get screen width and height
    screen_width = z23.winfo_screenwidth()
    screen_height = z23.winfo_screenheight()
    
    # Calculate position x, y
    position_x = int((screen_width / 2) - (window_width / 2))
    position_y = int((screen_height / 2) - (window_height / 2))
    
    # Set the geometry of the window
    z23.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")
    
    z23.iconphoto(False, icon)

    z23.resizable(0, 0)
    z23.focus_set()
    
    canvas = Canvas(z23, width=550, height=550, bg='#f8939c')  # Update canvas size
    canvas.pack(expand=YES, fill=BOTH)
    
    # Load and create the back button
    photox = PhotoImage(file=r"Resources\backbutton.png")
    back = Button(z23, image=photox, compound=TOP, command=z23.withdraw)
    back.image = photox
    back.place(x=410, y=10)

    # Load and create the Fruit Tart button
    photo1 = PhotoImage(file=r"Resources/CHOUX PASTRY/CROQUEMBOUCHE.png")
    b23 = Button(z23, text='Croquembouche', image=photo1, compound=TOP, font=('LITHOGRAPH',15,'bold'), fg="white", bg="#f8939c",bd=0)
    b23.image = photo1
    b23.place(x=70, y=100)

    def add():
        global count23
        count23 = count23 + 1
        if count23 >= 10:
            count23 = 10
            txtbox.delete("1.0", END)
            txtbox.insert(END, count23)
        else:
            txtbox.delete("1.0", END)
            txtbox.insert(END, count23)
    
    def sub():
        global count23
        count23 = max(count23 - 1, 1)  # Limit count to 0
        txtbox.delete("1.0", END)
        txtbox.insert(END, count23)
    
    def cnf():
        global total23
        global count23
        global bc1
        global bc2
        global bc3
        global bc4
        global bc5
        global bc6
        global bc7
        global bc8
        global bc9
        global bc10
        total23 = price23 * count23
        if(bc1==1):
            db.insert1('Croquembouche',count23,price23,total23)
        elif(bc2==1):
            db.insert2('Croquembouche',count23,price23,total23)
        elif(bc3==1):
            db.insert3('Croquembouche',count23,price23,total23)
        elif(bc4==1):
            db.insert4('Croquembouche',count23,price23,total23)
        elif(bc5==1):           
            db.insert5('Croquembouche',count23,price23,total23)
        elif(bc6==1):            
            db.insert6('Croquembouche',count23,price23,total23)
        elif(bc7==1):           
            db.insert7('Croquembouche',count23,price23,total23)
        elif(bc8==1):            
            db.insert8('Croquembouche',count23,price23,total23)
        elif(bc9==1):            
            db.insert9('Croquembouche',count23,price23,total23)
        elif(bc10==1):
            db.insert10('Croquembouche',count23,price23,total23)
        count23=1
        total23=0
        z23.destroy()
    # Create and place the text box to display count
    txtbox = Text(z23, height=0.5, width=5, bd=0, font=('LITHOGRAPH',15,'bold'), fg="white", bg="#f8939c")
    txtbox.place(x=368, y=165)
    txtbox.insert('1.0', count23)
    
    # Create and place the plus button
    plus = Button(z23, text='+', font=('arial', 16, 'bold'), width=5, fg="#f8939c", bg="white", command=add)
    plus.place(x=340, y=100)

    # Create and place the minus button
    minus = Button(z23, text='-', font=('arial', 16, 'bold'), width=5, fg="#f8939c", bg="white", command=sub)
    minus.place(x=340, y=220)

    # Create and place the confirm button
    b2 = Button(z23, text='Confirm Order', compound=TOP, font=('LITHOGRAPH',12,'bold'), bd=0, fg="#f8939c", bg="white", command=cnf)
    b2.place(x=325, y=300)

    # Create and place a label with a description
    var = StringVar()
    label1 = Label(z23, textvariable=var, relief=RAISED, justify=LEFT, font=('LITHOGRAPH', 12,'bold'), bg='#f8939c', bd=0, fg='white')
    var.set("A tower of cream-filled choux\n balls bound with caramel.")
    label1.place(x=70, y=350)

    # Create and place a label with the price
    var1 = StringVar()
    label2 = Label(z23, textvariable=var1, relief=RAISED, justify=LEFT, font=('LITHOGRAPH', 25, 'bold'), bg='#f8939c', bd=0, fg='white')
    var1.set("₱120 each")
    price23 = 120
    
    label2.place(x=70, y=420)
    z23.title("Croquembouche")

def Gougeres():
    global z24
    z24 = Toplevel(w)

    # Update idle tasks to ensure the window size is calculated
    z24.update_idletasks()
    
    window_width = 475
    window_height = 550
    
    # Get screen width and height
    screen_width = z24.winfo_screenwidth()
    screen_height = z24.winfo_screenheight()
    
    # Calculate position x, y
    position_x = int((screen_width / 2) - (window_width / 2))
    position_y = int((screen_height / 2) - (window_height / 2))
    
    # Set the geometry of the window
    z24.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")
    
    z24.iconphoto(False, icon)

    z24.resizable(0, 0)
    z24.focus_set()
    
    canvas = Canvas(z24, width=550, height=550, bg='#f8939c')  # Update canvas size
    canvas.pack(expand=YES, fill=BOTH)
    
    # Load and create the back button
    photox = PhotoImage(file=r"Resources\backbutton.png")
    back = Button(z24, image=photox, compound=TOP, command=z24.withdraw)
    back.image = photox
    back.place(x=410, y=10)

    # Load and create the Fruit Tart button
    photo1 = PhotoImage(file=r"Resources/CHOUX PASTRY/GOURGERES.png")
    b24 = Button(z24, text='Gougeres', image=photo1, compound=TOP, font=('LITHOGRAPH',15,'bold'), fg="white", bg="#f8939c",bd=0)
    b24.image = photo1
    b24.place(x=70, y=100)

    def add():
        global count24
        count24 = count24 + 1
        if count24 >= 10:
            count24 = 10
            txtbox.delete("1.0", END)
            txtbox.insert(END, count24)
        else:
            txtbox.delete("1.0", END)
            txtbox.insert(END, count24)
    
    def sub():
        global count24
        count24 = max(count24 - 1, 1)  # Limit count to 0
        txtbox.delete("1.0", END)
        txtbox.insert(END, count24)
    
    def cnf():
        global total24
        global count24
        global bc1
        global bc2
        global bc3
        global bc4
        global bc5
        global bc6
        global bc7
        global bc8
        global bc9
        global bc10
        total24 = price24 * count24
        if(bc1==1):
            db.insert1('Gougeres',count24,price24,total24)
        elif(bc2==1):
            db.insert2('Gougeres',count24,price24,total24)
        elif(bc3==1):
            db.insert3('Gougeres',count24,price24,total24)
        elif(bc4==1):
            db.insert4('Gougeres',count24,price24,total24)
        elif(bc5==1):           
            db.insert5('Gougeres',count24,price24,total24)
        elif(bc6==1):            
            db.insert6('Gougeres',count24,price24,total24)
        elif(bc7==1):           
            db.insert7('Gougeres',count24,price24,total24)
        elif(bc8==1):            
            db.insert8('Gougeres',count24,price24,total24)
        elif(bc9==1):            
            db.insert9('Gougeres',count24,price24,total24)
        elif(bc10==1):
            db.insert10('Gougeres',count24,price24,total24)
        count24=1
        total24=0
        z24.destroy()
    # Create and place the text box to display count
    txtbox = Text(z24, height=0.5, width=5, bd=0, font=('LITHOGRAPH',15,'bold'), fg="white", bg="#f8939c")
    txtbox.place(x=368, y=165)
    txtbox.insert('1.0', count24)
    
    # Create and place the plus button
    plus = Button(z24, text='+', font=('arial', 16, 'bold'), width=5, fg="#f8939c", bg="white", command=add)
    plus.place(x=340, y=100)

    # Create and place the minus button
    minus = Button(z24, text='-', font=('arial', 16, 'bold'), width=5, fg="#f8939c", bg="white", command=sub)
    minus.place(x=340, y=220)

    # Create and place the confirm button
    b2 = Button(z24, text='Confirm Order', compound=TOP, font=('LITHOGRAPH',12,'bold'), bd=0, fg="#f8939c", bg="white", command=cnf)
    b2.place(x=325, y=300)

    # Create and place a label with a description
    var = StringVar()
    label1 = Label(z24, textvariable=var, relief=RAISED, justify=LEFT, font=('LITHOGRAPH', 12,'bold'), bg='#f8939c', bd=0, fg='white')
    var.set("Savory choux puffs made with\ncheese, often Gruyère.")
    label1.place(x=70, y=350)

    # Create and place a label with the price
    var1 = StringVar()
    label2 = Label(z24, textvariable=var1, relief=RAISED, justify=LEFT, font=('LITHOGRAPH', 25, 'bold'), bg='#f8939c', bd=0, fg='white')
    var1.set("₱140 each")
    price24 = 140
    
    label2.place(x=70, y=420)
    z24.title("Gougeres")

# PASTRY TYPES

def Filo():
    global c
    c = Toplevel(w)
    
    window_width = 1410
    window_height = 780
    
    # Get screen width and height
    screen_width = c.winfo_screenwidth()
    screen_height = c.winfo_screenheight()
    
    # Calculate position x, y
    position_x = int((screen_width / 2) - (window_width / 2))
    position_y = int((screen_height / 2) - (window_height / 2))
    
    # Set the geometry of the window
    c.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")
    
    c.iconphoto(False, icon)

    c.resizable(0, 0)
    c.focus_set()

    canvas = tk.Canvas(c, width=1410, height=780)
    canvas.pack()
    
    create_gradient(canvas, 1410, 780, '#f8939c', '#fbc2c4')
    canvas.pack(expand = YES, fill = BOTH)

    #GUI
    photox=PhotoImage(file = r"Resources\backbutton.png")
    back=Button(c, image=photox, compound = TOP, command=c.withdraw)
    back.image=photox
    back.place(x=1300,y=15)

    menu_label =Label(c,width=15,text = 'Filo Pastries:', font=('LITHOGRAPH',20,'bold'),bg='#f8939c',fg='white')
    menu_label.place(relx=0.50, rely=0.10, anchor=CENTER)
    
    #MENU
    photo1 = PhotoImage(file = r"Resources\FILO PASTRY\APPLE STRUDEL.png")
    b1=Button(c, text = 'Apple Strudle', image = photo1, font='LITHOGRAPH', compound = TOP, command=AppleStr)
    b1.image=photo1
    b1.place(x=27,y=120)
    photo2 = PhotoImage(file = r"Resources\FILO PASTRY\BAKLAVA.png")
    b2=Button(c, text = 'Baklava', image = photo2, font='LITHOGRAPH', compound = TOP, command=Baklava)
    b2.image=photo2
    b2.place(x=307,y=120)
    photo3 = PhotoImage(file = r"Resources\FILO PASTRY\BOREK.png")
    b3=Button(c, text = 'Borek', image = photo3, font='LITHOGRAPH', compound = TOP, command=Borek)
    b3.image=photo3
    b3.place(x=587,y=120)
    photo4 = PhotoImage(file = r"Resources\FILO PASTRY\KATAIFI.png")
    b4=Button(c, text = 'Kataifi', image = photo4, font='LITHOGRAPH', compound = TOP, command=Kataifi)
    b4.image=photo4
    b4.place(x=867,y=120)
    photo5 = PhotoImage(file = r"Resources\FILO PASTRY\TIROPITA.png")
    b5=Button(c, text = 'Tiropita', image = photo5, font='LITHOGRAPH', compound = TOP, command=Tiropita)
    b5.image=photo5
    b5.place(x=1147,y=120)
    
    c.title("Filo Pastries")

def Puff():
    global d
    d = Toplevel(w)

    # Update idle tasks to ensure the window size is calculated
    d.update_idletasks()
    
    window_width = 1410
    window_height = 780
    
    # Get screen width and height
    screen_width = d.winfo_screenwidth()
    screen_height = d.winfo_screenheight()
    
    # Calculate position x, y
    position_x = int((screen_width / 2) - (window_width / 2))
    position_y = int((screen_height / 2) - (window_height / 2))
    
    # Set the geometry of the window
    d.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")
    
    d.iconphoto(False, icon)

    d.resizable(0, 0)
    d.focus_set()

    
    canvas = tk.Canvas(d, width=1410, height=780)
    canvas.pack()
    
    create_gradient(canvas, 1410, 780, '#f8939c', '#fbc2c4')
    canvas.pack(expand = YES, fill = BOTH)
    
    menu_label =Label(d,width=15,text = 'Puff Pastries:', font=('LITHOGRAPH',20,'bold'),bg='#f8939c',fg='white')
    menu_label.place(relx=0.50, rely=0.10, anchor=CENTER)

    photox=PhotoImage(file = r"Resources\backbutton.png")
    back=Button(d, image=photox, compound = TOP, command=d.withdraw)
    back.image=photox
    back.place(x=1300,y=15)
   
    photo1 = PhotoImage(file = r"Resources\PUFF PASTRY\NAPOLEON.png")
    b1=Button(d, text = 'Napoleon', image = photo1, font='LITHOGRAPH', compound = TOP, command=Napoleon)
    b1.image=photo1
    b1.place(x=125,y=120)
    
    photo2 = PhotoImage(file = r"Resources\PUFF PASTRY\BEEF WELLINGTON.png")
    b2=Button(d, text = 'Beef Wellington', image = photo2, font='LITHOGRAPH', compound = TOP, command=Beef)
    b2.image=photo2
    b2.place(x=425,y=120)

    photo3 = PhotoImage(file = r"Resources\PUFF PASTRY\CROISSANT.png")
    b3=Button(d, text = 'Croissant', image = photo3, font='LITHOGRAPH', compound = TOP, command=Croissant)
    b3.image=photo3
    b3.place(x=725,y=120)

    photo4 = PhotoImage(file = r"Resources\PUFF PASTRY\PAIN AU CHOCOLAT.png")
    b4=Button(d, text = 'Pain au Chocolat', image = photo4, font='LITHOGRAPH', compound = TOP, command=Pain)
    b4.image=photo4
    b4.place(x=1025,y=120)

    d.title("Puff Pastries")
    
def Flaky():
    global e
    e = Toplevel(w)

    # Update idle tasks to ensure the window size is calculated
    e.update_idletasks()
    
    window_width = 1410
    window_height = 780
    
    # Get screen width and height
    screen_width = e.winfo_screenwidth()
    screen_height = e.winfo_screenheight()
    
    # Calculate position x, y
    position_x = int((screen_width / 2) - (window_width / 2))
    position_y = int((screen_height / 2) - (window_height / 2))
    
    # Set the geometry of the window
    e.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")
    
    e.iconphoto(False, icon)

    e.resizable(0, 0)
    e.focus_set()
    
    canvas = tk.Canvas(e, width=1410, height=780)
    canvas.pack()
    
    menu_label =Label(e,width=15,text = 'Flaky Pastries:', font=('LITHOGRAPH',20,'bold'),bg='#f8939c',fg='white')
    menu_label.place(relx=0.50, rely=0.10, anchor=CENTER)
    
    create_gradient(canvas, 1410, 780, '#f8939c', '#fbc2c4')
    canvas.pack(expand = YES, fill = BOTH)
    
    photox=PhotoImage(file = r"Resources\backbutton.png")
    back=Button(e, image=photox, compound = TOP, command=e.withdraw)
    back.image=photox
    back.place(x=1300,y=15)

    photo1 = PhotoImage(file = r"Resources\FLAKY PASTRY\VOL-AU-VENT.png")
    b1=Button(e, text = 'Vol-au-vent', image = photo1, font='LITHOGRAPH', compound = TOP, command=Volauvent)
    b1.image=photo1
    b1.place(x=27,y=120)
    
    photo2 = PhotoImage(file = r"Resources\FLAKY PASTRY\PALMIERS.png")
    b2=Button(e, text = 'Palmiers', image = photo2, font='LITHOGRAPH', compound = TOP, command=Palmiers)
    b2.image=photo2
    b2.place(x=307,y=120)
    
    photo3 = PhotoImage(file = r"Resources\FLAKY PASTRY\ECCLES CAKES.png")
    b3=Button(e, text = 'Eccles Cakes', image = photo3, font='LITHOGRAPH', compound = TOP, command=Eccles)
    b3.image=photo3
    b3.place(x=587,y=120)
    
    photo4 = PhotoImage(file = r"Resources\FLAKY PASTRY\PASTIES.png")
    b4=Button(e, text = 'Pasties', image = photo4, font='LITHOGRAPH', compound = TOP, command=Pasties)
    b4.image=photo4
    b4.place(x=867,y=120)
    
    photo5 = PhotoImage(file = r"Resources/FLAKY PASTRY/CHICKEN POT PIE.png")
    b5=Button(e, text = 'Chicken Pot Pie', image = photo5, font='LITHOGRAPH', compound = TOP, command=Chicken)
    b5.image=photo5
    b5.place(x=1147,y=120)
    
    e.title("Flaky Pastries")

def Choux():
    global g
    g = Toplevel(w)

    # Update idle tasks to ensure the window size is calculated
    g.update_idletasks()
    
    window_width = 1410
    window_height = 780
    
    # Get screen width and height
    screen_width = g.winfo_screenwidth()
    screen_height = g.winfo_screenheight()
    
    # Calculate position x, y
    position_x = int((screen_width / 2) - (window_width / 2))
    position_y = int((screen_height / 2) - (window_height / 2))
    
    # Set the geometry of the window
    g.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")
    
    g.iconphoto(False, icon)

    g.resizable(0, 0)
    g.focus_set()
    
    canvas = tk.Canvas(g, width=1410, height=780)
    canvas.pack()
    
    create_gradient(canvas, 1410, 780, '#f8939c', '#fbc2c4')
    canvas.pack(expand = YES, fill = BOTH)
    
    menu_label =Label(g,width=15,text = 'Choux Pastries:', font=('LITHOGRAPH',20,'bold'),bg='#f8939c',fg='white')
    menu_label.place(relx=0.50, rely=0.10, anchor=CENTER)
    
    create_gradient(canvas, 1410, 780, '#f8939c', '#fbc2c4')
    canvas.pack(expand = YES, fill = BOTH)
    
    photox=PhotoImage(file = r"Resources\backbutton.png")
    back=Button(g, image=photox, compound = TOP, command=g.withdraw)
    back.image=photox
    back.place(x=1300,y=15)

    photo1 = PhotoImage(file = r"Resources\CHOUX PASTRY\ECLAIR.png")
    b1=Button(g, text = 'Eclair', image = photo1, font='LITHOGRAPH', compound = TOP, command=Eclair)
    b1.image=photo1
    b1.place(x=27,y=120)
    
    photo2 = PhotoImage(file = r"Resources\CHOUX PASTRY\PROFITEROLES.png")
    b2=Button(g, text = 'Profiteroles', image = photo2, font='LITHOGRAPH', compound = TOP, command=Profiteroles)
    b2.image=photo2
    b2.place(x=307,y=120)
    
    photo3 = PhotoImage(file = r"Resources\CHOUX PASTRY\PARIS-BREST.png")
    b3=Button(g, text = 'Paris-Brest', image = photo3, font='LITHOGRAPH', compound = TOP, command=Paris)
    b3.image=photo3
    b3.place(x=587,y=120)
    
    photo4 = PhotoImage(file = r"Resources\CHOUX PASTRY\CROQUEMBOUCHE.png")
    b4=Button(g, text = 'Croquembouche', image = photo4, font='LITHOGRAPH', compound = TOP, command=Croquembouche )
    b4.image=photo4
    b4.place(x=867,y=120)
    
    photo5 = PhotoImage(file = r"Resources\CHOUX PASTRY\GOURGERES.png")
    b5=Button(g, text = 'Gougeres', image = photo5, font='LITHOGRAPH', compound = TOP, command=Gougeres)
    b5.image=photo5
    b5.place(x=1147,y=120)
    
    g.title("Choux Pastries")

#SHORTCRUST PASTRIES
def menu():
    global t
    t = Toplevel(w)

    # Update idle tasks to ensure the window size is calculated
    t.update_idletasks()
    
    window_width = 1410
    window_height = 780
    
    # Get screen width and height
    screen_width = t.winfo_screenwidth()
    screen_height = t.winfo_screenheight()
    
    # Calculate position x, y
    position_x = int((screen_width / 2) - (window_width / 2))
    position_y = int((screen_height / 2) - (window_height / 2))
    
    # Set the geometry of the window
    t.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")
    
    t.iconphoto(False, icon)

    t.resizable(0, 0)
    t.focus_set()

    
    canvas = tk.Canvas(t, width=1410, height=780)
    canvas.pack()
    
    create_gradient(canvas, 1410, 780, '#f8939c', '#fbc2c4')
    canvas.pack(expand = YES, fill = BOTH)
    
    #GUI
    photox=PhotoImage(file = r"Resources\backbutton.png")
    back=Button(t, image=photox, compound = TOP, command=bac1)
    back.image=photox
    back.place(x=1300,y=15)
    photoy=PhotoImage(file = r"Resources\printbill.png")
    back=Button(t, image=photoy, compound = TOP, command=bill)
    back.image=photoy
    back.place(x=15,y=15)

    btn_pastry =Button(t,width=15,text = 'Filo Pastries', font=('LITHOGRAPH',20,'bold'),bg='#8dccd2',fg='white', command=Filo)
    btn_pastry.place(relx=0.20, rely=0.08, anchor=CENTER)
    
    menu_label =Label(t,width=15,text = 'Shortcrust Pastries:', font=('LITHOGRAPH',20,'bold'),bg='#f8939c',fg='white')
    menu_label.place(relx=0.50, rely=0.10, anchor=CENTER)

    btn_pastry =Button(t,width=15,text = 'Puff Pastries', font=('LITHOGRAPH',20,'bold'),bg='#8dccd2',fg='white', command=Puff)
    btn_pastry.place(relx=0.80, rely=0.08, anchor=CENTER)
    
    btn_pastry =Button(t,width=15,text = 'Flaky Pastries', font=('LITHOGRAPH',20,'bold'),bg='#8dccd2',fg='white', command=Flaky)
    btn_pastry.place(relx=0.30, rely=0.93, anchor=CENTER)
    
    btn_pastry =Button(t,width=15,text = 'Choux Pastries', font=('LITHOGRAPH',20,'bold'),bg='#8dccd2',fg='white', command=Choux)
    btn_pastry.place(relx=0.60, rely=0.93, anchor=CENTER)
    


    #MENU

    photo1 = PhotoImage(file = r"Resources\SHORTCRUST PASTRY\BAKEWELL.png")
    b1=Button(t, text = 'Bakewell Tart', image = photo1, font='LITHOGRAPH', compound = TOP, command=Bakewell
)
    b1.image=photo1
    b1.place(x=27,y=120)
    photo2 = PhotoImage(file = r"Resources\SHORTCRUST PASTRY\LEMON.png")
    b2=Button(t, text = 'Lemon Meringue', image = photo2, font='LITHOGRAPH', compound = TOP, command=Lemon)
    b2.image=photo2
    b2.place(x=307,y=120)
    photo3 = PhotoImage(file = r"Resources\SHORTCRUST PASTRY\CHOCO.png")
    b3=Button(t, text = 'Chocolate Pecan', image = photo3, font='LITHOGRAPH', compound = TOP,command=Choco)
    b3.image=photo3
    b3.place(x=587,y=120)
    photo4 = PhotoImage(file = r"Resources\SHORTCRUST PASTRY\FRUIT.png")
    b4=Button(t, text = 'Fruit Tart', image = photo4, font='LITHOGRAPH', compound = TOP,command=Fruit)
    b4.image=photo4
    b4.place(x=867,y=120)
    photo5 = PhotoImage(file = r"Resources\SHORTCRUST PASTRY\TARTE.png")
    b5=Button(t, text = 'Tarte Tatin', image = photo5, font='LITHOGRAPH', compound = TOP, command=Tarte)
    b5.image=photo5
    b5.place(x=1147,y=120)
    
    
    if(bc1==1):
        t.title("Table 1")
    elif(bc2==1):
        t.title("Table 2")
    elif(bc3==1):
        t.title("Table 3")
    elif(bc4==1):
        t.title("Table 4")
    elif(bc5==1):           
        t.title("Table 5")
    elif(bc6==1):            
        t.title("Table 6")
    elif(bc7==1):           
        t.title("Table 7")
    elif(bc8==1):            
        t.title("Table 8")
    elif(bc9==1):            
        t.title("Table 9")
    else:
        t.title("Table 10")

#CLEAR DB FUNCTION
def clear():
    adb.del1()
    messagebox.showinfo("Information","Database Cleared Successfully")
    
def close_bdata_window():
    if 'r1' in globals():
        r1.destroy()

def bdata():

    global r1
    close_bdata_window()  # Close the previous bdata window, if exists

    def brow():
        a=date1.get()
        b=date2.get()
        lb1.delete(0,'end')
        lb2.delete(0,'end')
        receipt.delete("1.0",END)
        conn = sqlite3.connect('ADMIN.sqlite')
        cursor = conn.cursor()
        if a == "" or b == "":
            messagebox.showerror("Error","Please Enter the Date")
            bdata()
        else:
            try:
                for row in cursor.execute("SELECT * from `ADMIN` where `DATE` = ?", (a,)):
                    id1=row[0]
                    break
                for row in cursor.execute("SELECT * FROM `ADMIN` WHERE `DATE` = ?", (b,)):
                    id2=row[0]
                if(id1>id2):
                    messagebox.showerror("Error","Date Entered Incorrectly")
                    bdata()
                else:
                    ##CORRECT DATE
                    receipt.delete("1.0",END)
                    receipt.insert(END,"ID\tBILL\tTABLE\t\tITEM\t\tQTY\tPRICE\tDATE\t   TIME\n")
                    receipt.insert(END,"==================================================================================\n\n")
                    for row in cursor.execute("SELECT * FROM `ADMIN` WHERE ID >= ? AND ID <= ?", (id1,id2,)):
                        a=row[0]
                        a=str(a)
                        b=row[1]
                        b=str(b)
                        c=row[2]
                        c=str(c)
                        d=row[3]
                        d=str(d)
                        e=row[4]
                        e=str(e)
                        f=row[5]
                        f=str(f)
                        g=row[6]
                        g=str(g)
                        h=row[7]
                        h=str(h)
                        receipt.insert(END,a+"\t"+b+"\t"+c+"\t\t"+d+"\t\t"+e+"\t"+f+"\t"+g+"\t   "+h+"\n")
            except UnboundLocalError:
                try:
                      try:
                          #LAST DATE OUT OF DB
                        for row in cursor.execute("SELECT * FROM 'ADMIN' "):
                            idx=row[0]
                        receipt.delete("1.0",END)
                        receipt.insert(END,"ID\tBILL\tTABLE\t\tITEM\t\tQTY\tPRICE\tDATE\t   TIME\n")
                        receipt.insert(END,"==================================================================================\n\n")
                        for row in cursor.execute("SELECT * FROM `ADMIN` WHERE ID >= ? AND ID <= ?", (id1,idx,)):
                            a=row[0]
                            a=str(a)
                            b=row[1]
                            b=str(b)
                            c=row[2]
                            c=str(c)
                            d=row[3]
                            d=str(d)
                            e=row[4]
                            e=str(e)
                            f=row[5]
                            f=str(f)
                            g=row[6]
                            g=str(g)
                            h=row[7]
                            h=str(h)
                            receipt.insert(END,a+"\t"+b+"\t"+c+"\t\t"+d+"\t\t"+e+"\t"+f+"\t"+g+"\t   "+h+"\n")
                      except UnboundLocalError:
                          #FIRST DATE OUT OF DB
                            for row in cursor.execute("SELECT * FROM 'ADMIN' "):
                                idy=row[0]
                                break
                            receipt.delete("1.0",END)
                            receipt.insert(END,"ID\tBILL\tTABLE\t\tITEM\t\tQTY\tPRICE\tDATE\t   TIME\n")
                            receipt.insert(END,"==================================================================================\n\n")
                            for row in cursor.execute("SELECT * FROM `ADMIN` WHERE ID >= ? AND ID <= ?", (idy,id2,)):
                                a=row[0]
                                a=str(a)
                                b=row[1]
                                b=str(b)
                                c=row[2]
                                c=str(c)
                                d=row[3]
                                d=str(d)
                                e=row[4]
                                e=str(e)
                                f=row[5]
                                f=str(f)
                                g=row[6]
                                g=str(g)
                                h=row[7]
                                h=str(h)
                                receipt.insert(END,a+"\t"+b+"\t"+c+"\t\t"+d+"\t\t"+e+"\t"+f+"\t"+g+"\t   "+h+"\n")
                except:
                    messagebox.showerror("Error","Date Format Entered Incorrectly")
                    bdata()
        conn.commit()
        conn.close()


    r1 = Toplevel(w)

    # Update idle tasks to ensure the window size is calculated
    r1.update_idletasks()
    
    window_width = 1100
    window_height = 768
    
    # Get screen width and height
    screen_width = r1.winfo_screenwidth()
    screen_height = r1.winfo_screenheight()
    
    # Calculate position x, y
    position_x = int((screen_width / 2) - (window_width / 2))
    position_y = int((screen_height / 2) - (window_height / 2))
    
    # Set the geometry of the window
    r1.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")
    
    r1.resizable(0, 0)

    r1.iconphoto(False, icon)
    r1.focus_set()

    
    canvas = Canvas(r1, width=window_width, height=window_height, bg='#f8939c')  # Update canvas size
    canvas.pack(expand=YES, fill=BOTH)
    receipt=Text(r1,height=19,width=88,bd=1,font=('LITHOGRAPH',16,'italic'),fg="black",bg="white")
    receipt.place(x=20,y=100)
    lab1 = Label(r1, text = "From:", font=('LITHOGRAPH', 14),bg='#f8939c',fg='white')
    lab1.place(x=380,y=10)
    lb1=Entry(r1, textvariable=date1, font=(14))
    lb1.place(x=460,y=10)
    lab2 = Label(r1, text = "To:", font=('LITHOGRAPH', 14),bg='#f8939c',fg='white')
    lab2.place(x=380,y=45)
    lb2=Entry(r1, textvariable=date2, font=(14))
    lb2.place(x=460,y=45)
    b1=Button(r1, width=10, text = 'Search', font=('LITHOGRAPH',14,'bold'),bg='#8dccd2',fg='white', command=brow)
    b1.place(x=700,y=25)
    menubar = Menu(r1)
    filemenu = Menu(menubar, tearoff=0)
    helpmenu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Go", menu=filemenu)
    filemenu.add_command(label="Exit", command=r1.withdraw)
    r1.config(menu=menubar)
    r1.title("Database")
    conn = sqlite3.connect('ADMIN.sqlite')
    cursor = conn.cursor()
    receipt.insert(END,"ID\tBILL\tTABLE\t\tITEM\t\tQTY\tPRICE\tDATE\t   TIME\n")
    receipt.insert(END,"==================================================================================\n\n")
    for row in cursor.execute("SELECT * from ADMIN"):       
        a=row[0]
        a=str(a)
        b=row[1]
        b=str(b)
        c=row[2]
        c=str(c)
        d=row[3]
        d=str(d)
        e=row[4]
        e=str(e)
        f=row[5]
        f=str(f)
        g=row[6]
        g=str(g)
        h=row[7]
        h=str(h)
        receipt.insert(END,a+"\t"+b+"\t"+c+"\t\t"+d+"\t\t"+e+"\t"+f+"\t"+g+"\t   "+h+"\n")                   
    conn.commit()
    conn.close()

import tkinter as tk

def create_gradient(canvas, width, height, color1, color2):
    r1, g1, b1 = canvas.winfo_rgb(color1)
    r2, g2, b2 = canvas.winfo_rgb(color2)
    
    r_ratio = float(r2 - r1) / height
    g_ratio = float(g2 - g1) / height
    b_ratio = float(b2 - b1) / height
    
    for i in range(height):
        nr = int(r1 + (r_ratio * i))
        ng = int(g1 + (g_ratio * i))
        nb = int(b1 + (b_ratio * i))
        
        color = f'#{nr:04x}{ng:04x}{nb:04x}'
        canvas.create_line(0, i, width, i, fill=color)

def browse():

    r = Toplevel(w)

    
    window_width = 400
    window_height = 400
    
    # Get screen width and height
    screen_width = r.winfo_screenwidth()
    screen_height = r.winfo_screenheight()
    
    # Calculate position x, y
    position_x = int((screen_width / 2) - (window_width / 2))
    position_y = int((screen_height / 2) - (window_height / 2))
    
    # Set the geometry of the window
    r.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")
    
    r.resizable(0, 0)
    r.iconphoto(False, icon)

    r.focus_set()

    canvas = tk.Canvas(r, width=400, height=400)
    canvas.pack()
    
    create_gradient(canvas, 400, 400, '#f8939c', '#fbc2c4')

    canvas.pack(expand = YES, fill = BOTH)#8dccd2
    b1=Button(r,width=15,text = 'Browse Data', font=('LITHOGRAPH',20,'bold'),bg='#8dccd2',fg='white',command=bdata)
    b1.place(x=70,y=100)

    b2=Button(r,width=15, text = 'Clear Data', font=('LITHOGRAPH',20,'bold'),bg='#8dccd2',fg='white',command=clear)
    b2.place(x=70,y=225)
    
    menu = Menu(r) 
    r.config(menu=menu) 
    filemenu = Menu(menu, tearoff=0) 
    menu.add_cascade(label='Go', menu=filemenu) 
    filemenu.add_command(label='Exit', command=r.withdraw) 
    helpmenu = Menu(menu, tearoff=0) 
    r.title("Browse")   


def Login(event=None):
    Database()
    if USERNAME.get() == "" or PASSWORD.get() == "":
        USERNAME.set("")
        PASSWORD.set("")
        messagebox.showerror("Error","Please Enter Username and Password")  
    else:
        cursor.execute("SELECT * FROM `member` WHERE `username` = ? AND `password` = ?", (USERNAME.get(), PASSWORD.get()))
        if cursor.fetchone() is not None:
            USERNAME.set("")
            PASSWORD.set("")
            l1.withdraw()
            browse()
        else:
            USERNAME.set("")
            PASSWORD.set("")
            messagebox.showerror("Error","Invalid Username or Password")
            l1.withdraw()
    cursor.close()
    conn.close()
def admin():
  
    global l1
    l1 = Toplevel(w)

    
    window_width = 375
    window_height = 160
    
    # Get screen width and height
    screen_width = l1.winfo_screenwidth()
    screen_height = l1.winfo_screenheight()
    
    # Calculate position x, y
    position_x = int((screen_width / 2) - (window_width / 2))
    position_y = int((screen_height / 2) - (window_height / 2))
    
    # Set the geometry of the window
    l1.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")
    
    l1.resizable(0, 0)
    l1.iconphoto(False, icon)

    l1.focus_set()
    lbl_username = Label(l1, text = "Username:", font=('LITHOGRAPH', 14), bd=15)
    lbl_username.grid(row=0, sticky="e")
    lbl_password = Label(l1, text = "Password:", font=('LITHOGRAPH', 14), bd=15)
    lbl_password.grid(row=1, sticky="e")
    lbl_text = Label(l1)
    lbl_text.grid(row=2, columnspan=2)
    lbl_text = Label(l1)
    lbl_text.grid(row=2, columnspan=2)
    username = Entry(l1, textvariable=USERNAME, font=(14))
    username.grid(row=0, column=1)
    password = Entry(l1, textvariable=PASSWORD, show="*", font=(14))
    password.grid(row=1, column=1)
    btn_login = Button(l1, text="Login", width=20, command=Login)
    btn_login.place(x=110,y=120)
    btn_login.bind('<Return>', Login)
    l1.title("Login")


#choose table
def fun():
    global f
    f = Toplevel(w)

    # Update idle tasks to ensure the window size is calculated
    f.update_idletasks()
    
    window_width = 1380
    window_height = 780
    
    # Get screen width and height
    screen_width = f.winfo_screenwidth()
    screen_height = f.winfo_screenheight()
    
    # Calculate position x, y
    position_x = int((screen_width / 2) - (window_width / 2))
    position_y = int((screen_height / 2) - (window_height / 2))
    
    # Set the geometry of the window
    f.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")
    
    f.iconphoto(False, icon)

    f.resizable(0, 0)
    f.focus_set()

    canvas = tk.Canvas(f, width=1380, height=780)
    canvas.pack()
    
    create_gradient(canvas, 1380, 780, '#f8939c', '#fbc2c4')
    canvas.pack(expand = YES, fill = BOTH)
    
    menubar = Menu(f)
    filemenu = Menu(menubar, tearoff=0)
    helpmenu = Menu(menubar, tearoff=0)
    
    filemenu.add_command(label="Admin", command=admin)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=f.withdraw)
    menubar.add_cascade(label="Go", menu=filemenu)
    
    
    f.config(menu=menubar)
    f.iconphoto(False, icon)
    
    # Define button placements in a loop to avoid redundancy
    button_info = [
        (r"Resources\1.png", "TABLE 1", table1, 27, 80),
        (r"Resources\4.png", "TABLE 2", table2, 307, 80),
        (r"Resources\2.png", "TABLE 3", table3, 587, 80),
        (r"Resources\4.png", "TABLE 4", table4, 867, 80),
        (r"Resources\2.png", "TABLE 5", table5, 1147, 80),
        (r"Resources\1.png", "TABLE 6", table6, 27, 450),
        (r"Resources\2.png", "TABLE 7", table7, 307, 450),
        (r"Resources\4.png", "TABLE 8", table8, 587, 450),
        (r"Resources\1.png", "TABLE 9", table9, 867, 450),
        (r"Resources\4.png", "TABLE 10", table10, 1147, 450),
    ]

    for img_file, label, cmd, x, y in button_info:
        photo = PhotoImage(file=img_file)
        btn = Button(f, text=label, image=photo, font=('LITHOGRAPH', 20, 'bold'), compound=TOP, command=cmd)
        btn.image = photo
        btn.place(x=x, y=y)
    
    f.title("Choose a table!")



def bill():
    global bil
    bil = Toplevel(w)

    # Update idle tasks to ensure the window size is calculated
    bil.update_idletasks()
    
    window_width = 1365
    window_height = 780
    
    # Get screen width and height
    screen_width = bil.winfo_screenwidth()
    screen_height = bil.winfo_screenheight()
    
    # Calculate position x, y
    position_x = int((screen_width / 2) - (window_width / 2))
    position_y = int((screen_height / 2) - (window_height / 2))
    
    # Set the geometry of the window
    bil.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")
    
    bil.iconphoto(False, icon)

    bil.resizable(0, 0)
    bil.focus_set()
    
    canvas = tk.Canvas(bil, width=1370, height=780)
    canvas.pack()
    
    create_gradient(canvas, 1370, 780, '#f8939c', '#fbc2c4')
    canvas.pack(expand = YES, fill = BOTH)

    tot=Text(bil,height=1,width=14,bd=0,font=('LITHOGRAPH',20,'bold'),fg="#9f5c5f",bg="white")
    tot.place(x=1358,y=800)

    receipt=Text(bil,height=20,width=88,bd=0,font=('LITHOGRAPH',20,'bold'),fg="#9f5c5f",bg="white")
    receipt.place(x=20,y=70)

    tot.config(state=DISABLED)
    receipt.config(state=DISABLED)

    receipt.config(state=NORMAL)
    receipt.delete("1.0",END)
    tot.delete("1.0",END)
    TimeOfOrder=StringVar()
    DateOfOrder=StringVar()
    TimeOfOrder.set(now.strftime("%I:%M:%S %p"))
    DateOfOrder.set(now.strftime("%x"))

    receipt.insert(END,"\t\t\t\t    PASTRY PALETTE,\n")
    receipt.insert(END,"\t\t\t  Catalina Building, New York Ave, Cubao,\n")
    receipt.insert(END,"\t\t\t        Quezon City, 1109 Metro Manila\n")
    receipt.insert(END,"\t\t\t                   TEL: 0135-353-533\n\n")
    receipt.insert(END," Date :\t\t"+DateOfOrder.get()+"\n")
    receipt.insert(END," Time :\t\t"+TimeOfOrder.get()+"\n\n")
    receipt.insert(END,"==================================================================================\n")
    receipt.insert(END,"\t\t\t\tORDER SUMMARY\n")
    receipt.insert(END,"==================================================================================\n\n")
    receipt.insert(END,"      ITEM			                     QUANTITY			                                                 PRICE\n")
    
    if(bc1==1):
        adbill=adb.peekbil()
        adbill=adbill + 1
        adbill=str(adbill)
        conn = sqlite3.connect('TABLE_1.sqlite')
        cursor = conn.cursor()
        for row in cursor.execute("SELECT ITEM,QUANTITY,PRICE,TOTAL from TABLE1"):
            c1=row[1]
            c1=str(c1)
            d1=row[3]
            d1=str(d1)
            item=row[0]
            quantity=row[1]
            total=row[3]
            adb.insert(adbill,"TABLE 1",item,quantity,total)
            receipt.insert(END," "+row[0]+"			                             "+c1+"			                                                     "+d1+"\n")
        conn.commit()
        conn.close()
        to=str(db.peek1())
        receipt.insert(END,"\n==================================================================================\n")
        receipt.insert(END," Bill no.:"+adbill+"                                                                                                             TOTAL:    ₱"+to+"\n")
        receipt.insert(END,"==================================================================================\n")
    elif(bc2==1):
        adbill=adb.peekbil()
        adbill=adbill + 1
        adbill=str(adbill)
        conn = sqlite3.connect('TABLE_1.sqlite')
        cursor = conn.cursor()
        for row in cursor.execute("SELECT ITEM,QUANTITY,PRICE,TOTAL from TABLE2"):
            c1=row[1]
            c1=str(c1)
            d1=row[3]
            d1=str(d1)
            item=row[0]
            quantity=row[1]
            total=row[3]
            adb.insert(adbill,"TABLE 2",item,quantity,total)
            receipt.insert(END," "+row[0]+"			                             "+c1+"			                                                     "+d1+"\n")
        conn.commit()
        conn.close()
        to=str(db.peek2())
        receipt.insert(END,"\n==================================================================================\n")
        receipt.insert(END," Bill no.:"+adbill+"                                                                                                             TOTAL:    ₱"+to+"\n")
        receipt.insert(END,"==================================================================================\n")
    elif(bc3==1):
        adbill=adb.peekbil()
        adbill=adbill + 1
        adbill=str(adbill)
        conn = sqlite3.connect('TABLE_1.sqlite')
        cursor = conn.cursor()
        for row in cursor.execute("SELECT ITEM,QUANTITY,PRICE,TOTAL from TABLE3"):
            c1=row[1]
            c1=str(c1)
            d1=row[3]
            d1=str(d1)
            item=row[0]
            quantity=row[1]
            total=row[3]
            adb.insert(adbill,"TABLE 3",item,quantity,total)
            receipt.insert(END," "+row[0]+"			                             "+c1+"			                                                     "+d1+"\n")
        conn.commit()
        conn.close()
        to=str(db.peek3())
        receipt.insert(END,"\n==================================================================================\n")
        receipt.insert(END," Bill no.:"+adbill+"                                                                                                             TOTAL:    ₱"+to+"\n")
        receipt.insert(END,"==================================================================================\n")
    elif(bc4==1):
        adbill=adb.peekbil()
        adbill=adbill + 1
        adbill=str(adbill)
        conn = sqlite3.connect('TABLE_1.sqlite')
        cursor = conn.cursor()
        for row in cursor.execute("SELECT ITEM,QUANTITY,PRICE,TOTAL from TABLE4"):
            c1=row[1]
            c1=str(c1)
            d1=row[3]
            d1=str(d1)
            item=row[0]
            quantity=row[1]
            total=row[3]
            adb.insert(adbill,"TABLE 4",item,quantity,total)
            receipt.insert(END," "+row[0]+"			                             "+c1+"			                                                     "+d1+"\n")
        conn.commit()
        conn.close()
        to=str(db.peek4())
        receipt.insert(END,"\n==================================================================================\n")
        receipt.insert(END," Bill no.:"+adbill+"                                                                                                             TOTAL:    ₱"+to+"\n")
        receipt.insert(END,"==================================================================================\n")
    elif(bc5==1):
        adbill=adb.peekbil()
        adbill=adbill + 1
        adbill=str(adbill)
        conn = sqlite3.connect('TABLE_1.sqlite')
        cursor = conn.cursor()
        for row in cursor.execute("SELECT ITEM,QUANTITY,PRICE,TOTAL from TABLE5"):
            c1=row[1]
            c1=str(c1)
            d1=row[3]
            d1=str(d1)
            item=row[0]
            quantity=row[1]
            total=row[3]
            adb.insert(adbill,"TABLE 5",item,quantity,total)
            receipt.insert(END," "+row[0]+"			                             "+c1+"			                                                     "+d1+"\n")
        conn.commit()
        conn.close()
        to=str(db.peek5())
        receipt.insert(END,"\n==================================================================================\n")
        receipt.insert(END," Bill no.:"+adbill+"                                                                                                             TOTAL:    ₱"+to+"\n")
        receipt.insert(END,"==================================================================================\n")
    elif(bc6==1):
        adbill=adb.peekbil()
        adbill=adbill + 1
        adbill=str(adbill)
        conn = sqlite3.connect('TABLE_1.sqlite')
        cursor = conn.cursor()
        for row in cursor.execute("SELECT ITEM,QUANTITY,PRICE,TOTAL from TABLE6"):
            c1=row[1]
            c1=str(c1)
            d1=row[3]
            d1=str(d1)
            item=row[0]
            quantity=row[1]
            total=row[3]
            adb.insert(adbill,"TABLE 6",item,quantity,total)
            receipt.insert(END," "+row[0]+"			                             "+c1+"			                                                     "+d1+"\n")
        conn.commit()
        conn.close()
        to=str(db.peek6())
        receipt.insert(END,"\n==================================================================================\n")
        receipt.insert(END," Bill no.:"+adbill+"                                                                                                             TOTAL:    ₱"+to+"\n")
        receipt.insert(END,"==================================================================================\n")
    elif(bc7==1):
        adbill=adb.peekbil()
        adbill=adbill + 1
        adbill=str(adbill)
        conn = sqlite3.connect('TABLE_1.sqlite')
        cursor = conn.cursor()
        for row in cursor.execute("SELECT ITEM,QUANTITY,PRICE,TOTAL from TABLE7"):
            c1=row[1]
            c1=str(c1)
            d1=row[3]
            d1=str(d1)
            item=row[0]
            quantity=row[1]
            total=row[3]
            adb.insert(adbill,"TABLE 7",item,quantity,total)
            receipt.insert(END," "+row[0]+"			                             "+c1+"			                                                     "+d1+"\n")
        conn.commit()
        conn.close()
        to=str(db.peek7())
        receipt.insert(END,"\n==================================================================================\n")
        receipt.insert(END," Bill no.:"+adbill+"                                                                                                             TOTAL:    ₱"+to+"\n")
        receipt.insert(END,"==================================================================================\n")
    elif(bc8==1):
        adbill=adb.peekbil()
        adbill=adbill + 1
        adbill=str(adbill)
        conn = sqlite3.connect('TABLE_1.sqlite')
        cursor = conn.cursor()
        for row in cursor.execute("SELECT ITEM,QUANTITY,PRICE,TOTAL from TABLE8"):
            c1=row[1]
            c1=str(c1)
            d1=row[3]
            d1=str(d1)
            item=row[0]
            quantity=row[1]
            total=row[3]
            adb.insert(adbill,"TABLE 8",item,quantity,total)
            receipt.insert(END," "+row[0]+"			                             "+c1+"			                                                     "+d1+"\n")
        conn.commit()
        conn.close()
        to=str(db.peek8())
        receipt.insert(END,"\n==================================================================================\n")
        receipt.insert(END," Bill no.:"+adbill+"                                                                                                             TOTAL:    ₱"+to+"\n")
        receipt.insert(END,"==================================================================================\n")
    elif(bc9==1):
        adbill=adb.peekbil()
        adbill=adbill + 1
        adbill=str(adbill)
        conn = sqlite3.connect('TABLE_1.sqlite')
        cursor = conn.cursor()
        for row in cursor.execute("SELECT ITEM,QUANTITY,PRICE,TOTAL from TABLE9"):
            c1=row[1]
            c1=str(c1)
            d1=row[3]
            d1=str(d1)
            item=row[0]
            quantity=row[1]
            total=row[3]
            adb.insert(adbill,"TABLE 9",item,quantity,total)
            receipt.insert(END," "+row[0]+"			                             "+c1+"			                                                     "+d1+"\n")
        conn.commit()
        conn.close()
        to=str(db.peek9())
        receipt.insert(END,"\n==================================================================================\n")
        receipt.insert(END," Bill no.:"+adbill+"                                                                                                             TOTAL:    ₱"+to+"\n")
        receipt.insert(END,"==================================================================================\n")
    elif(bc10==1):
        adbill=adb.peekbil()
        adbill=adbill + 1
        adbill=str(adbill)
        conn = sqlite3.connect('TABLE_1.sqlite')
        cursor = conn.cursor()
        for row in cursor.execute("SELECT ITEM,QUANTITY,PRICE,TOTAL from TABLE10"):
            c1=row[1]
            c1=str(c1)
            d1=row[3]
            d1=str(d1)
            item=row[0]
            quantity=row[1]
            total=row[3]
            adb.insert(adbill,"TABLE 10",item,quantity,total)
            receipt.insert(END," "+row[0]+"			                             "+c1+"			                                                     "+d1+"\n")
        conn.commit()
        conn.close()
        to=str(db.peek10())
        receipt.insert(END,"\n==================================================================================\n")
        receipt.insert(END," Bill no.:"+adbill+"                                                                                                             TOTAL:    ₱"+to+"\n")
        receipt.insert(END,"==================================================================================\n")
    
    receipt.config(state=DISABLED)
    photo10 = PhotoImage(file = r"Resources\exit.png")
    b10=Button(bil, image = photo10, font=('LITHOGRAPH',20,'bold'), compound = TOP, command=ex)
    b10.image=photo10
    b10.place(x=1250,y=10)
    if(bc1==1):
        bil.title("TABLE 1 BILL")
    elif(bc2==1):
        bil.title("TABLE 2 BILL")
    elif(bc3==1):
        bil.title("TABLE 3 BILL")
    elif(bc4==1):
        bil.title("TABLE 4 BILL")
    elif(bc5==1):           
        bil.title("TABLE 5 BILL")
    elif(bc6==1):            
        bil.title("TABLE 6 BILL")
    elif(bc7==1):           
        bil.title("TABLE 7 BILL")
    elif(bc8==1):            
        bil.title("TABLE 8 BILL")
    elif(bc9==1):            
        bil.title("TABLE 9 BILL")
    else:
        bil.title("TABLE 10 BILL")
def ex():
    global bc1
    global bc2
    global bc3
    global bc4
    global bc5
    global bc6
    global bc7
    global bc8
    global bc9
    global bc10
    global bil
    if(bc1==1):
        db.del1()
        bc1=0
        bil.withdraw()
        t.withdraw()
    elif(bc2==1):
        db.del2()
        bc2=0
        bil.withdraw()
        t.withdraw()
    elif(bc3==1):
        db.del3()
        bc3=0
        bil.withdraw()
        t.withdraw()
    elif(bc4==1):
        db.del4()
        bc4=0
        bil.withdraw()
        t.withdraw()
    elif(bc5==1):
        db.del5()
        bc5=0
        bil.withdraw()
        t.withdraw()
    elif(bc6==1):
        db.del6()
        bc6=0
        bil.withdraw()
        t.withdraw()
    elif(bc7==1):
        db.del7()
        bc7=0
        bil.withdraw()
        t.withdraw()
    elif(bc8==1):
        db.del8()
        bc8=0
        bil.withdraw()
        t.withdraw()
    elif(bc9==1):
        db.del9()
        bc9=0
        bil.withdraw()
        t.withdraw()
    elif(bc10==1):
        db.del10()
        bc10=0
        bil.withdraw()
        t.withdraw()

def mp():
    w.focus_set()
    menu1 = Menu(w) 
    w.config(menu=menu1) 
    filemenu = Menu(menu1, tearoff=0) 
    menu1.add_cascade(label='Go', menu=filemenu) 
    filemenu.add_command(label='Admin',command=admin)
    filemenu.add_command(label='Order',command=fun)
    filemenu.add_separator() 
    filemenu.add_command(label='Exit',command=w.destroy) 
    helpmenu = Menu(menu1, tearoff=0) 
    w.title("Pastry Palette")

Billno=StringVar()
Cost=StringVar()
Items=StringVar()
Quantity=StringVar()
TimeOfOrder=StringVar()
DateOfOrder=StringVar()
TimeOfOrder.set(now.strftime("%I:%M:%S %p"))
DateOfOrder.set(now.strftime("%x"))

mp()
mainloop()

