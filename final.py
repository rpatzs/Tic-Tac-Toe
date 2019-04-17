from Tkinter import*

from tkMessageBox import*

import sqlite3

con=sqlite3.Connection("tictac.db")

cur=con.cursor()

touch = True

c1=0

c2=0

i=-9
def mai():
    def fun1():

        tk=Tk()

        tk.title("Tic Tac Toe")

        def fun(Buttons):

            global touch,c1,c2,i

            i=i+1

            if Buttons["text"]==" " and touch == True:  

                Buttons["text"]="X" 

                touch=False

            elif Buttons["text"]==" " and touch==False:

                Buttons["text"]="O"

                touch = True

            elif((Button1["text"]=="X" and Button2["text"]=="X" and Button3["text"]=="X" )or

                Button4["text"]=="X" and Button5["text"]=="X" and Button6["text"]=="X" or

                Button7["text"]=="X" and Button8["text"]=="X" and Button9["text"]=="X" or

                Button3["text"]=="X" and Button5["text"]=="X" and Button7["text"]=="X" or

                Button1["text"]=="X" and Button5["text"]=="X" and Button9["text"]=="X" or

                Button2["text"]=="X" and Button5["text"]=="X" and Button8["text"]=="X" or

                Button3["text"]=="X" and Button6["text"]=="X" and Button9["text"]=="X" or

                Button1["text"]=="X" and Button4["text"]=="X" and Button7["text"]=="X" ):

                c1=c1+1

                showinfo("Winner Player1"," you have just won a game")

            elif(Button1["text"]=="O" and Button2["text"]=="O" and Button3["text"]=="O" or

                Button4["text"]=="O" and Button5["text"]=="O" and Button6["text"]=="O" or

                Button7["text"]=="O" and Button8["text"]=="O" and Button9["text"]=="O" or

                Button3["text"]=="O" and Button5["text"]=="O" and Button7["text"]=="O" or

                Button1["text"]=="O" and Button5["text"]=="O" and Button9["text"]=="O" or

                Button2["text"]=="O" and Button5["text"]=="O" and Button8["text"]=="O" or

                Button3["text"]=="O" and Button6["text"]=="O" and Button9["text"]=="O" or

                Button1["text"]=="O" and Button4["text"]=="O" and Button7["text"]=="O" ):

                c2=c2+1

                showinfo("Winner Player2","you have just won a game")

            elif(i==9 and c1==0 and c2==0):

                showinfo("Draw","no one won the match")

        Buttons = StringVar()

        Button1=Button(tk,text=" ",font=("Times 26 bold"),height=4,width=8,command=lambda:fun(Button1))

        Button1.grid(row=1,column=0)
        Button2=Button(tk,text=" ",font=("Times 26 bold"),height=4,width=8,command=lambda:fun(Button2))

        Button2.grid(row=1,column=1)

        Button3=Button(tk,text=" ",font=("Times 26 bold"),height=4,width=8,command=lambda:fun(Button3))

        Button3.grid(row=1,column=2)

        Button4=Button(tk,text=" ",font=("Times 26 bold"),height=4,width=8,command=lambda:fun(Button4))

        Button4.grid(row=2,column=0)

        Button5=Button(tk,text=" ",font=("Times 26 bold"),height=4,width=8,command=lambda:fun(Button5))

        Button5.grid(row=2,column=1)

        Button6=Button(tk,text=" ",font=("Times 26 bold"),height=4,width=8,command=lambda:fun(Button6))

        Button6.grid(row=2,column=2)

        Button7=Button(tk,text=" ",font=("Times 26 bold"),height=4,width=8,command=lambda:fun(Button7))

        Button7.grid(row=3,column=0)

        Button8=Button(tk,text=" ",font=("Times 26 bold"),height=4,width=8,command=lambda:fun(Button8))

        Button8.grid(row=3,column=1)

        Button9=Button(tk,text=" ",font=("Times 26 bold"),height=4,width=8,command=lambda:fun(Button9))

        Button9.grid(row=3,column=2)

        tk.mainloop()
        

    def f1():

    
        fun1()
     
    

    def result():
        if c1==1:
            r=e.get()   
        elif c2==1:
            r=f.get()
        else:
            r="DRAW"
        cur.execute("create table if not exists ttt(fname varchar2(20),sname varchar2(20),result varchar2(20))")
        cur.execute("insert into ttt values(?,?,?)",(e.get(),f.get(),r))

    def res():
        result()
        cur.execute('select result from ttt where fname=? and sname=?',(e.get(),f.get()))
    
        Label(root,text=(cur.fetchall()),font='times 60').grid(row=20,column=0,columnspan=9,sticky=W+E+N+S)
        
    root=Tk()

    

    Label(root,text="Enter first name",font='times 40').grid(row=1,column=0,columnspan=1,sticky=W)

    e=Entry(root,font='times 20')

    e.grid(row=1,column=1)

    Label(root,text="Enter second name",font='times 40').grid(row=2,column=0,columnspan=1,sticky=W)

    f=Entry(root,font='times 20')

    f.grid(row=2,column=1)

  

    Button(root,text='Proceed to play',font='times 10',command=f1).grid(row=3,column=1)

    Button(root,text='Result',font='times 10',command=res).grid(row=4,column=1)

    Label(root,text="please double click on each button after proceeding",font='times 40').grid(row=5,column=0,sticky=W)

    root.mainloop()
main=Tk()
main.minsize(1000,1000)
main.configure(bg='cyan3')
Label(main,text="Topic = Tic Tac Toe",font='ravie 30',bg='dark orange',fg='white').grid(row=1,column=0,columnspan=10)
pm=PhotoImage(file='splash.gif')
Label(main,image=pm).grid(row=2,column=0,sticky=W)
Label(main,text="Name = Bikash Kumar Sharma",font='ravie 15',bg='cyan3',fg='white').grid(row=4,column=0,sticky=W)
Label(main,text="Enroll Number = 161B066",font='ravie 15',bg='cyan3',fg='white').grid(row=5,column=0,sticky=W)
Label(main,text="Email = rpatzs007@gmail.com",font='ravie 15',bg='cyan3',fg='white').grid(row=6,column=0,sticky=W)
Label(main,text="Phone number = 9516939851",font='ravie 15',bg='cyan3',fg='white').grid(row=7,column=0,sticky=W)
Label(main,text="Branch = CSE",font='ravie 15',bg='cyan3',fg='white').grid(row=8,column=0,sticky=W)
Label(main,text="Batch = BX(B3)",font='ravie 15',bg='cyan3',fg='white').grid(row=9,column=0,sticky=W)
main.after(10000,mai)
main.mainloop()

