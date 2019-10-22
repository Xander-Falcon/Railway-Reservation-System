import pymysql
from tkinter import *


def submit():
    var3 = int(e1.get())
    con = pymysql.connect(host='localhost', user='root', password='sayan123', database='sayan_data')
    cursor1 = con.cursor()
    strx = "select * from pssngr_details  where pnr_no='%d'"
    args = var3
    cursor1.execute(strx % args)
    row = cursor1.fetchone()
    str1 = ""
    for i in range(0, 12):
        str1 = str1 + "\t" + str(row[i])
    output1 = Label(frame, text=str1, height=10, width=150, bg='green')
    output1.place(x=500, y=300)
    con.commit()
    cursor1.close()
    con.close()


window = Tk()
window.title("Print Ticket")
frame = Frame(window, height=760, width=1350, bg='cyan')
l1 = Label(frame, text='Ticket Printer', height=2, width=50, bg='blue')
l2 = Label(frame, text='Pnr', height=2, width=20, bg='black', fg='white')
e1 = Entry(frame, width=50, bg='white', fg='blue')
b1 = Button(frame, text='Submit', height=2, width=30, bg='red', fg='white', command=submit)
l1.place(x=500, y=50)
l2.place(x=400, y=150)
e1.place(x=600, y=150)
b1.place(x=500, y=400)
frame.pack()
window.mainloop()
