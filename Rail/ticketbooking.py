from tkinter import *
import pymysql


def submit():
    var1 = e1.get()
    var2 = int(e2.get())
    var3 = e3.get()
    var4 = e4.get()
    var5 = e5.get()
    var6 = int(e6.get())
    var7 = int(e7.get())
    var8 = e8.get()
    con = pymysql.connect(host='localhost', user='root', password='sayan123', database='sayan_data')
    cursor1 = con.cursor()
    cursor2 = con.cursor()
    strx = "select distance,departure_time,arrival_time,train_name from train_jrny where train_no='%d'"
    args = var6
    cursor1.execute(strx % args)
    row = cursor1.fetchone()
    price = int(0)
    if var8 == "sleeper":
        price = row[0]*1.5
    elif var8 == "second class ac":
        price = row[0]*2
    elif var8 == "first class ac":
        price = row[0]*3
    str1 = "select max(pnr_no) from pssngr_details"
    cursor1.execute(str1)
    rows = cursor1.fetchone()
    pnr = rows[0]
    pnr = pnr+1
    str2 = "insert into pssngr_details values('%d','%s','%s','%s','%s','%s','%d','%d','%d','%s','%d','%d','%s')"
    args2 = (var6, row[3], var4, var5, row[1], row[2], row[0], pnr, price, var1, var2, var7, var3)
    output1 = Label(frame, text=pnr, height=4, width=5, bg='green')
    output1.place(x=600, y=400)
    cursor2.execute(str2 % args2)
    con.commit()

    cursor1.close()
    cursor2.close()
    con.close()


window = Tk()


window.title("Book Ticket")
frame = Frame(window, height=760, width=1350, bg='cyan')
l1 = Label(frame, text='Ticket Booker', height=2, width=50, bg='blue')
l2 = Label(frame, text='Name', height=2, width=20, bg='black', fg='white')
l3 = Label(frame, text='Age', height=2, width=20, bg='black', fg='white')
l4 = Label(frame, text='Date of Journey', height=2, width=20, bg='black', fg='white')
l5 = Label(frame, text='From', height=2, width=20, bg='black', fg='white')
l6 = Label(frame, text='Destination', height=2, width=20, bg='black', fg='white')
l7 = Label(frame, text='Train No', height=2, width=20, bg='black', fg='white')
l8 = Label(frame, text='Aadhar Card no.', height=2, width=20, bg='black', fg='white')
l9 = Label(frame, text='Class', height=2, width=20, bg='black', fg='white')
e1 = Entry(frame, width=50, bg='white', fg='blue')
e2 = Entry(frame, width=50, bg='white', fg='blue')
e3 = Entry(frame, width=50, bg='white', fg='blue')
e4 = Entry(frame, width=50, bg='white', fg='blue')
e5 = Entry(frame, width=50, bg='white', fg='blue')
e6 = Entry(frame, width=50, bg='white', fg='blue')
e7 = Entry(frame, width=50, bg='white', fg='blue')
e8 = Entry(frame, width=50, bg='white', fg='blue')
b1 = Button(frame, text='Submit', height=2, width=30, bg='red', fg='white', command=submit)
l1.place(x=500, y=50)
l2.place(x=400, y=150)
l3.place(x=400, y=200)
l4.place(x=400, y=250)
l5.place(x=400, y=300)
l6.place(x=400, y=350)
l7.place(x=400, y=400)
l8.place(x=400, y=450)
l9.place(x=400, y=500)
e1.place(x=600, y=150)
e2.place(x=600, y=200)
e3.place(x=600, y=250)
e4.place(x=600, y=300)
e5.place(x=600, y=350)
e6.place(x=600, y=400)
e7.place(x=600, y=450)
e8.place(x=600, y=500)
b1.place(x=600, y=600)
frame.pack()
window.mainloop()
