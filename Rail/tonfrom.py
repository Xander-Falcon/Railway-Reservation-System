from tkinter import  *;
import pymysql;
window=Tk();
def submit():
    var1=e1.get()
    var2=e2.get()
    con = pymysql.connect(host='localhost', user='root', password='sayan123', database='sayan_data')
    cursor1 = con.cursor()
    str="select * from train_jrny where from_='%s' and destinatoion='%s'"
    args=(var1,var2)
    cursor1.execute(str % args)
    rows=cursor1.fetchall()
    for i in range(len(rows)):
        for j in range(len(rows[0])):
            e3=Entry(frame,width=20,fg='blue')
            e3.grid(row=i,column=j)
            e3.insert(END,rows[i][j])

window.title("Jrny Details")
frame=Frame(window,height=760,width=1350,bg='cyan')
l1=Label(frame,text='Enter Your Source And Destination',height=2,width=50,bg='blue')
l2=Label(frame,text='From',height=2,width=20,bg='black',fg='white')
l3=Label(frame,text='To',height=2,width=20,bg='black',fg='white')
e1=Entry(frame,width=50,bg='white',fg='blue')
e2=Entry(frame,width=50,bg='white',fg='blue')
b1=Button(frame,text='Submit',height=2,width=30,bg='red',fg='white',command=submit)
l1.place(x=500,y=50)
l2.place(x=400,y=150)
l3.place(x=400,y=200)
e1.place(x=600,y=150)
e2.place(x=600,y=200)
b1.place(x=600,y=600)
frame.pack()
window.mainloop()