from Tkinter import *
from tkMessageBox import *
import random
import datetime;
import time
global page1
root=Tk()
    
def enter():
    root1=Tk()
    root1.geometry("1600x800+0+0")
    root1.attributes('-fullscreen',True)
    root1.title("PAGE 1")
    root1.configure(background="black")
    

    f2=Frame(root1,width=900,height=650,bd=8,relief="flat")
    f2.pack(side=LEFT,fill="both",expand="yes")

    f3=Frame(root1,width=440,height=650,bd=8,relief="flat")
    f3.pack(side=RIGHT,fill="both",expand="yes")

    f2a=Frame(f2,width=900,height=330,bd=8,relief="flat")
    f2a.pack(side=TOP,fill="both",expand="yes")
    f2b=Frame(f2,width=900,height=320,bd=6,relief="flat")
    f2b.pack(side=BOTTOM,fill="both",expand="yes")

    f3a=Frame(f3,width=440,height=450,bd=12,relief="raise")
    f3a.pack(side=TOP,fill="both",expand="yes")
    f3b=Frame(f3,width=440,height=250,bd=12,relief="raise")
    f3b.pack(side=BOTTOM,fill="both",expand="yes")

    f2aa=Frame(f2a,width=400,height=330,bd=16,relief="flat")
    f2aa.pack(side=LEFT,fill="both",expand="yes")
    f2bb=Frame(f2a,width=400,height=330,bd=16,relief="flat")
    f2bb.pack(side=RIGHT,fill="both",expand="yes")
    f2cc=Frame(f2a,width=400,height=330,bd=16,relief="flat")
    f2cc.pack(fill="both",expand="yes")

    f2aa1=Frame(f2b,width=450,height=330,bd=14,relief="flat")
    f2aa1.pack(side=LEFT,fill="both",expand="yes")
    

    f2.configure(background="black")
    f3.configure(background="black")


    

    a=IntVar()
    a1=IntVar()
    a2=IntVar()
    a3=IntVar()
    a4=IntVar()
    a5=IntVar()
    a6=IntVar()
    a7=IntVar()
    a8=IntVar()
    a9=IntVar()

    b=IntVar()
    b1=IntVar()
    b2=IntVar()
    b3=IntVar()
    b4=IntVar()
    

    d1=StringVar()
    d2=StringVar()
    d3=StringVar()
    d4=StringVar()
    d5=StringVar()
    d6=StringVar()
    d7=StringVar()
    d8=StringVar()
    d9=StringVar()
    d10=StringVar()
    d11=StringVar()
    d12=StringVar()
    d13=StringVar()
    d14=StringVar()
    d15=StringVar()

    d1.set("0")
    d2.set("0")
    d3.set("0")
    d4.set("0")
    d5.set("0")
    d6.set("0")
    d7.set("0")
    d8.set("0")
    d9.set("0")
    d10.set("0")
    d11.set("0")
    d12.set("0")
    d13.set("0")
    d14.set("0")
    d15.set("0")

    

    

    def click():
        if a.get()==1:
            e1.configure(state=NORMAL)
        elif a.get()==0:
            e1.configure(state=DISABLED)
        if a1.get()==2:
            e2.configure(state=NORMAL)
        elif a1.get()==0:
            e2.configure(state=DISABLED)
        if a2.get()==3:
            e3.configure(state=NORMAL)
        elif a2.get()==0:
            e3.configure(state=DISABLED)
        if a3.get()==4:
            e4.configure(state=NORMAL)
        elif a3.get()==0:
            e4.configure(state=DISABLED)
        if a4.get()==5:
            e5.configure(state=NORMAL)
        elif a4.get()==0:
            e5.configure(state=DISABLED)
        if a5.get()==6:
            e6.configure(state=NORMAL)
        elif a5.get()==0:
            e6.configure(state=DISABLED)
        if a6.get()==7:
            e7.configure(state=NORMAL)
        elif a6.get()==0:
            e7.configure(state=DISABLED)
        if a7.get()==8: 
            e8.configure(state=NORMAL)
        elif a7.get()==0:
            e8.configure(state=DISABLED)
        if a8.get()==9:
            e9.configure(state=NORMAL)
        elif a8.get()==0:
            e9.configure(state=DISABLED)
        if a9.get()==10:
            e10.configure(state=NORMAL)
        elif a9.get()==0:
            e10.configure(state=DISABLED)
        if b.get()==11:
            f1.configure(state=NORMAL)
        elif b.get()==0:
            f1.configure(state=DISABLED)
        if b1.get()==12:
            f2.configure(state=NORMAL)
        elif b1.get()==0:
            f2.configure(state=DISABLED)
        if b2.get()==13:
            f3.configure(state=NORMAL)
        elif b2.get()==0:
            f3.configure(state=DISABLED)
        if b3.get()==14:
            f4.configure(state=NORMAL)
        elif b3.get()==0:
            f4.configure(state=DISABLED)
        if b4.get()==15:
            f5.configure(state=NORMAL)
        elif b4.get()==0:
            f5.configure(state=DISABLED)
            



    Label(f2aa,text="STARTERS",font="Chiller 14 bold").grid(row=0,column=0,sticky=W)
    c1=Checkbutton(f2aa,font="Chiller 14 bold",text="Chilli Paneer",command=click,variable=a,onvalue=1).grid(row=1,column=0,sticky=W)
    Label(f2aa,font="Arial 14 bold",text="90").grid(row=1,column=4)
    c2=Checkbutton(f2aa,font="Chiller 14 bold",text="Honey chilli potato",command=click,variable=a1,onvalue=2).grid(row=2,column=0,sticky=W)
    Label(f2aa,font="Arial 14 bold",text="75").grid(row=2,column=4)
    c3=Checkbutton(f2aa,font="Chiller 14 bold",text="Spring rolls",command=click,variable=a2,onvalue=3).grid(row=3,column=0,sticky=W)
    Label(f2aa,font="Arial 14 bold",text="120").grid(row=3,column=4)
    c4=Checkbutton(f2aa,font="Chiller 14 bold",text="Tomato Soup",variable=a3,command=click,onvalue=4).grid(row=4,column=0,sticky=W)
    Label(f2aa,font="Arial 14 bold",text="60").grid(row=4,column=4)
    c5=Checkbutton(f2aa,font="Chiller 14 bold",text="Manchurian",command=click,variable=a4,onvalue=5).grid(row=5,column=0,sticky=W)
    Label(f2aa,font="Arial 14 bold",text="75").grid(row=5,column=4)

    e1=Entry(f2aa,bd=8,width=6,font="Arial 14 bold",justify='left',textvariable=d1,state=DISABLED)
    e1.grid(row=1,column=1)
    e2=Entry(f2aa,bd=8,width=6,font="Arial 14 bold",justify='left',textvariable=d2,state=DISABLED)
    e2.grid(row=2,column=1)
    e3=Entry(f2aa,bd=8,width=6,font="Arial 14 bold",justify='left',textvariable=d3,state=DISABLED)
    e3.grid(row=3,column=1)
    e4=Entry(f2aa,bd=8,width=6,font="Arial 14 bold",justify='left',textvariable=d4,state=DISABLED)
    e4.grid(row=4,column=1)
    e5=Entry(f2aa,bd=8,width=6,font="Arial 14 bold",justify='left',textvariable=d5,state=DISABLED)
    e5.grid(row=5,column=1)

    Label(f2bb,text="MAIN COURSE",font="Chiller 14 bold").grid(row=0,column=0,sticky=W)
    c6=Checkbutton(f2bb,font="Chiller 14 bold",text="Kadhai Paneer",command=click,variable=a5,onvalue=6).grid(row=1,column=0,sticky=W)
    Label(f2bb,font="Arial 14 bold",text="140").grid(row=1,column=4)
    c7=Checkbutton(f2bb,font="Chiller 14 bold",text="Chole bhature",command=click,variable=a6,onvalue=7).grid(row=2,column=0,sticky=W)
    Label(f2bb,font="Arial 14 bold",text="120").grid(row=2,column=4)
    c8=Checkbutton(f2bb,font="Chiller 14 bold",text="Dal Makhni",command=click,variable=a7,onvalue=8).grid(row=3,column=0,sticky=W)
    Label(f2bb,font="Arial 14 bold",text="160").grid(row=3,column=4)
    c9=Checkbutton(f2bb,font="Chiller 14 bold",text="Paneer Masala",command=click,variable=a8,onvalue=9).grid(row=4,column=0,sticky=W)
    Label(f2bb,font="Arial 14 bold",text="140").grid(row=4,column=4)
    c10=Checkbutton(f2bb,font="Chiller 14 bold",text="Bhindi Fry",command=click,variable=a9,onvalue=10).grid(row=5,column=0,sticky=W)
    Label(f2bb,font="Arial 14 bold",text="100").grid(row=5,column=4)

    e6=Entry(f2bb,bd=8,width=6,font="Arial 14 bold",justify='left',textvariable=d6,state=DISABLED)
    e6.grid(row=1,column=1)
    e7=Entry(f2bb,bd=8,width=6,font="Arial 14 bold",justify='left',textvariable=d7,state=DISABLED)
    e7.grid(row=2,column=1)
    e8=Entry(f2bb,bd=8,width=6,font="Arial 14 bold",justify='left',textvariable=d8,state=DISABLED)
    e8.grid(row=3,column=1)
    e9=Entry(f2bb,bd=8,width=6,font="Arial 14 bold",justify='left',textvariable=d9,state=DISABLED)
    e9.grid(row=4,column=1)
    e10=Entry(f2bb,bd=8,width=6,font="Arial 14 bold",justify='left',textvariable=d10,state=DISABLED)
    e10.grid(row=5,column=1)

    Label(f2cc,text="DESERT",font="Chiller 14 bold").grid(row=0,column=0,sticky=W)
    c11=Checkbutton(f2cc,font="Chiller 14 bold",text="Gulab Jamun",command=click,variable=b,onvalue=11).grid(row=1,column=0,sticky=W)
    Label(f2cc,font="Arial 14 bold",text="60").grid(row=1,column=4)
    c12=Checkbutton(f2cc,font="Chiller 14 bold",text="Kulfi Faluda",command=click,variable=b1,onvalue=12).grid(row=2,column=0,sticky=W)
    Label(f2cc,font="Arial 14 bold",text="75").grid(row=2,column=4)
    c13=Checkbutton(f2cc,font="Chiller 14 bold",text="Choclate Icecream",command=click,variable=b2,onvalue=13).grid(row=3,column=0,sticky=W)
    Label(f2cc,font="Arial 14 bold",text="45").grid(row=3,column=4)
    c14=Checkbutton(f2cc,font="Chiller 14 bold",text="Brownie",command=click,variable=b3,onvalue=14).grid(row=4,column=0,sticky=W)
    Label(f2cc,font="Arial 14 bold",text="50").grid(row=4,column=4)
    c15=Checkbutton(f2cc,font="Chiller 14 bold",text="Jalebi",command=click,variable=b4,onvalue=15).grid(row=5,column=0,sticky=W)
    Label(f2cc,font="Arial 14 bold",text="55").grid(row=5,column=4)

    f1=Entry(f2cc,bd=8,width=6,font="Arial 14 bold",justify='left',textvariable=d11,state=DISABLED)
    f1.grid(row=1,column=1)
    f2=Entry(f2cc,bd=8,width=6,font="Arial 14 bold",justify='left',textvariable=d12,state=DISABLED)
    f2.grid(row=2,column=1)
    f3=Entry(f2cc,bd=8,width=6,font="Arial 14 bold",justify='left',textvariable=d13,state=DISABLED)
    f3.grid(row=3,column=1)
    f4=Entry(f2cc,bd=8,width=6,font="Arial 14 bold",justify='left',textvariable=d14,state=DISABLED)
    f4.grid(row=4,column=1)
    f5=Entry(f2cc,bd=8,width=6,font="Arial 14 bold",justify='left',textvariable=d15,state=DISABLED)
    f5.grid(row=5,column=1)
    def qexit():
        qexit=askyesnocancel("Quit System","Do you want to quit?")
        if qexit>0:
            root1.destroy()
            return

    def reset():
        
        
        d1.set("0")
        d2.set("0")
        d3.set("0")
        d4.set("0")
        d5.set("0")
        d6.set("0")
        d7.set("0")
        d8.set("0")
        d9.set("0")
        d10.set("0")
        d11.set("0")
        d12.set("0")
        d13.set("0")
        d14.set("0")
        d15.set("0")

        a.set(0)
        a1.set(0)
        a2.set(0)
        a3.set(0)
        a4.set(0)
        a5.set(0)
        a6.set(0)
        a7.set(0)
        a8.set(0)
        a9.set(0)
        b.set(0)
        b1.set(0)
        b2.set(0)
        b3.set(0)
        b4.set(0)

        e1.configure(state=DISABLED)
        e2.configure(state=DISABLED)
        e3.configure(state=DISABLED)
        e4.configure(state=DISABLED)
        e5.configure(state=DISABLED)
        e6.configure(state=DISABLED)
        e7.configure(state=DISABLED)
        e8.configure(state=DISABLED)
        e9.configure(state=DISABLED)
        e10.configure(state=DISABLED)
        f1.configure(state=DISABLED)
        f2.configure(state=DISABLED)
        f3.configure(state=DISABLED)
        f4.configure(state=DISABLED)
        f5.configure(state=DISABLED)

        

        l1.destroy()
        l2.destroy()
        l3.destroy()
        l4.destroy()
        
        l5.destroy()
        

        l6.destroy()
        l7.destroy()
        l8.destroy()
        l9.destroy()
        l10.destroy()
        
        l11.destroy()
        l12.destroy()
        l13.destroy()
        l14.destroy()
        l15.destroy()
        
        t1.destroy()
        t2.destroy()
        t3.destroy()
        t4.destroy()

        t5.destroy()
        
        t6.destroy()
        t7.destroy()
        t8.destroy()
        t9.destroy()
        t10.destroy()
        
        t11.destroy()
        t12.destroy()
        t13.destroy()
        t14.destroy()
        t15.destroy()
        
       
    def printbill():
        global l,l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15,t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,t11,t12,t13,t14,t15
        v1=StringVar()
        v2=StringVar()
        v3=StringVar()
        v4=StringVar()
        v5=StringVar()
        v6=StringVar()
        v7=StringVar()
        v8=StringVar()
        v9=StringVar()
        v10=StringVar()
        v11=StringVar()
        v12=StringVar()
        v13=StringVar()
        v14=StringVar()
        v15=StringVar()
        t1=Label(f3a,textvariable=v1)
        t2=Label(f3a,textvariable=v2)
        t3=Label(f3a,textvariable=v3)
        t4=Label(f3a,textvariable=v4)
        t5=Label(f3a,textvariable=v5)
        t6=Label(f3a,textvariable=v6)
        t7=Label(f3a,textvariable=v7)
        t8=Label(f3a,textvariable=v8)
        t9=Label(f3a,textvariable=v9)
        t10=Label(f3a,textvariable=v10)
        t11=Label(f3a,textvariable=v11)
        t12=Label(f3a,textvariable=v12)
        t13=Label(f3a,textvariable=v13)
        t14=Label(f3a,textvariable=v14)
        t15=Label(f3a,textvariable=v15)

        l1=Label(f3a,text="Chilli Paneer")        
        l2=Label(f3a,text="Honey Chilli potato")
        l3=Label(f3a,text=" Spring Roll")
        l4=Label(f3a,text="Tomato Soup")
        l5=Label(f3a,text="Manchurian")
        l6=Label(f3a,text="Kadhai Paneer")
        l7=Label(f3a,text="Chole Bhature")
        l8=Label(f3a,text="Dal Makhni")
        l9=Label(f3a,text="Paneer Masala")
        l10=Label(f3a,text="Bhindi Fry")
        l11=Label(f3a,text="Gulab Jamun")
        l12=Label(f3a,text="Kulfi Faluda")
        l13=Label(f3a,text="Choclate Icecream")
        l14=Label(f3a,text=" Brownie")
        l15=Label(f3a,text=" Jalebi")
                                                        
        Label(f3a,text="Recipt:",font="Arial 16 bold").grid(row=1,column=0,sticky=W)
        if a.get()==1:
            l1.grid(row=16,column=0,sticky=W)
            v1.set((int(e1.get()))*90)
            t1.grid(row=16,column=1,sticky=E)
        if a1.get()==2:
            l2.grid(row=2,column=0,sticky=W)
            v2.set((int(e2.get()))*75)
            t2.grid(row=2,column=1,sticky=E)
        if a2.get()==3:
            l3.grid(row=3,column=0,sticky=W)
            v3.set((int(e3.get()))*120)
            t3.grid(row=3,column=1,sticky=E)
        if a3.get()==4:
            l4.grid(row=4,column=0,sticky=W)
            v4.set((int(e4.get()))*60)
            t4.grid(row=4,column=1,sticky=E)
        if a4.get()==5:
            l5.grid(row=5,column=0,sticky=W)
            v5.set((int(e5.get()))*75)
            t5.grid(row=5,column=1,sticky=E)
        if a5.get()==6:
            l6.grid(row=6,column=0,sticky=W)
            v6.set((int(e6.get()))*140)
            t6.grid(row=6,column=1,sticky=E)
        if a6.get()==7:
            l7.grid(row=7,column=0,sticky=W)
            v7.set((int(e7.get()))*120)
            t7.grid(row=7,column=1,sticky=E)
        if a7.get()==8:
            l8.grid(row=8,column=0,sticky=W)
            v8.set((int(e8.get()))*160)
            t8.grid(row=8,column=1,sticky=E)
        if a8.get()==9:
            l9.grid(row=9,column=0,sticky=W)
            v9.set((int(e9.get()))*140)
            t9.grid(row=9,column=1,sticky=E)
        if a9.get()==10:
            l10.grid(row=17,column=0,sticky=W)
            v10.set((int(e10.get()))*100)
            t10.grid(row=17,column=1,sticky=E)
        if b.get()==11:
            l11.grid(row=11,column=0,sticky=W)
            v11.set((int(f1.get()))*60)
            t11.grid(row=11,column=1,sticky=E)
        if b1.get()==12:
            l12.grid(row=12,column=0,sticky=W)
            v12.set((int(f2.get()))*75)
            t12.grid(row=12,column=1,sticky=E)
        if b2.get()==13:
            l13.grid(row=13,column=0,sticky=W)
            v13.set((int(f3.get()))*45)
            t13.grid(row=13,column=1,sticky=E)
        if b3.get()==14:
            l14.grid(row=14,column=0,sticky=W)
            v14.set((int(f4.get()))*50)
            t14.grid(row=14,column=1,sticky=E)
        if b4.get()==15:
            l15.grid(row=15,column=0,sticky=W)
            v15.set((int(f5.get()))*55)
            t15.grid(row=15,column=1,sticky=E)

    photo=PhotoImage(file="Python Project.gif")
    Label(f2aa1,image=photo).pack(fill='both',expand='yes')

    def new():
        root1.withdraw()
        master=Tk()
        #master.geometry('600x800')
        master.attributes('-fullscreen',True)
        
        global num
        num=0
        if a.get()==1:
            num=num+(int(e1.get())*90)
        if a1.get()==2:
            num=num+(int(e2.get())*75)
        if a2.get()==3:
            num=num+(int(e3.get())*120)
        if a3.get()==4:
            num=num+(int(e4.get())*60)
        if a4.get()==5:
            num=num+(int(e5.get())*75)
        if a5.get()==6:
            num=num+(int(e6.get())*140)
        if a6.get()==7:
            num=num+(int(e7.get())*120)
        if a7.get()==8:
            num=num+(int(e8.get())*160)
        if a8.get()==9:
            num=num+(int(e9.get())*140)
        if a9.get()==10:
            num=num+(int(e10.get())*100)
        if b.get()==11:
            num=num+(int(f1.get())*60)
        if b1.get()==12:
            num=num+(int(f2.get())*70)
        if b2.get()==13:
            num=num+(int(f3.get())*45)
        if b3.get()==14:
            num=num+(int(f4.get())*50)
        if b4.get()==15:
            num=num+(int(f5.get())*55)
        Label(master,text=" ").pack(side=TOP,expand=NO, fill=X)
        Label(master,text=" ").pack(side=TOP,expand=NO, fill=X)
        Label(master,text=" ").pack(side=TOP,expand=NO, fill=X)
        Label(master,text=" ").pack(side=TOP,expand=NO, fill=X)
        Label(master,text=" ").pack(side=TOP,expand=NO, fill=X)
        Label(master,text=" ").pack(side=TOP,expand=NO, fill=X)
        Label(master, text='\n\n\n\n\n\n\nYou have to pay ',fg='black',font='jokerman 22').pack(side=TOP,anchor=CENTER)
        Label(master, text='\n'+'Rs'+' '+str(num),fg='black',font='jokerman 24 bold').pack(side=TOP,anchor=CENTER)
        button4=Button(master,padx=16,pady=1,bd=4,fg='black',font="jokerman 12 bold",width=5,text="EXIT",command=master.destroy,relief='flat')
        button4.pack(side=BOTTOM,fill="both")

        
    
    
            
        
    button1=Button(f3b,padx=16,pady=1,bd=4,fg='black',font="jokerman 12 bold",width=5,text="GENERATE BILL",command=printbill,relief='flat')
    button1.pack(side=TOP,fill="both")

    button2=Button(f3b,padx=16,pady=1,bd=4,fg='black',font="jokerman 12 bold",width=5,text="RESET",command=reset,relief='flat')
    button2.pack(fill="both")

    button4=Button(f3b,padx=16,pady=1,bd=4,fg='black',font="jokerman 12 bold",width=5,text="PRINT BILL",command=new,relief='flat')
    button4.pack(fill="both")

    button4=Button(f3b,padx=16,pady=1,bd=4,fg='black',font="jokerman 12 bold",width=5,text="EXIT",command=qexit,relief='flat')
    button4.pack(fill="both")
    
    root1.mainloop()

def q1():
    root.destroy()
    enter()
def aboutus():
    master=Tk()
        
    master.attributes('-fullscreen',True)

    shortcutbar = Frame(master, height=30, bg='light green')
    Button(shortcutbar,justify=CENTER,text='CLOSE',font='jokerman',activeforeground='khaki',overrelief=SOLID,relief=GROOVE,command=master.destroy,bg='white',activebackground='black').pack(side=RIGHT,anchor=NE,fill=Y)
    toolbar = Label(shortcutbar, text='HOTEL LEMON TREE',bg='light green',fg='black',font='jokerman 25 bold')
    toolbar1=Label(shortcutbar, text='',bg='light green',fg='dark green',font='CalibriLight 15 bold')
    toolbar.pack(side=TOP,fill=X)
    toolbar1.pack(side=TOP,fill=X)
    shortcutbar.pack(side=TOP,fill=X)
    Label(master, text='').pack(side=TOP,fill=X)
    Label(master,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(master,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(master,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(master,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(master, text='\n\n\n\n\n 151321 (B4)',fg='black',font='jokerman 18 bold').pack(side=TOP,anchor=CENTER)
    #Label(master, text='',fg='blue',font='castellar 20 bold').pack(side=TOP,anchor=CENTER)
    Label(master, text='Maulshree Saxena (7240915259) ',fg='black',font='jokerman 20 bold').pack(side=TOP,anchor=CENTER)

    Label(master, text='Email :maulshreesaxena27@gmail.com',fg='black',font='Chiller 15 bold',relief=RAISED,width=50).pack(side=BOTTOM,anchor=CENTER,fill=X)
    Label(master,text='Project designed by: Maulshree Saxena',justify=CENTER,relief=RIDGE,fg='black',font='Chiller 18 bold',bg='khaki').pack(side=BOTTOM,fill=X)
    #s = Frame(master, height=30, bg='light green')
    #Button(s, text='EXIT',justify=CENTER,cursor="hand2",relief=RIDGE,width=16,height=1,bg='light blue',fg='black',font='SegoeUISemibold 15 bold',command=master.destroy,activebackground='#00A0A0').pack(side=LEFT, anchor=SW)
    #s.pack(side=BOTTOM,expand=NO, fill=X)

root.geometry("1600x800+0+0")
root.title("LEMON TREE")
root.configure(background="black")
root.attributes('-fullscreen',True)


photo=PhotoImage(file="1.gif")
l=Label(root,image=photo,font="jokerman 70 bold",text="  Hotel Lemon Tree ",compound=CENTER,fg='white',bg='black',bd=10)
Button(l,padx=16,pady=1,bd=4,fg='black',font="jokerman 16 bold",width=5,text="EXIT",command=root.destroy).pack(side=BOTTOM,anchor=W)
Button(l,padx=16,pady=1,bd=4,fg='black',font="Jokerman 16 bold",width=5,text="ENTER",command=q1).pack(side=BOTTOM,anchor=N)
Button(l,padx=16,pady=1,bd=4,fg='black',font="Jokerman 16 bold",width=7,text="ABOUT US",command=aboutus).pack(side=BOTTOM,anchor=E)

l.pack(fill="both",expand="yes")
root.mainloop()
    


