from Tkinter import *
from tkMessageBox import *
from tkFileDialog import *
import sqlite3
from SQLinjector import *


def checkvuln(wsite,name):
        inject=[]
        global result
        for x in name:
            sqlinject=x
            inject.append(wsite.replace("FUZZ",sqlinject))
        result=injector(inject)
        checkres()


def report():
    p1.destroy()
    global rep
    rep=Tk()
    rep.geometry('1024x577')
    rep.configure(bg='white', cursor='circle')
    pic=PhotoImage(file="softwall.gif")
    rep.title("SQL Injection Vulnerability Scanner")
    Label(rep,image=pic).grid(row=0,column=0,rowspan=10,columnspan=10)
    Label(rep,text='SQL Injection Vulnerability Scanner', font='Harrington 18 bold' ).grid(row=0,column=0,columnspan=10)
    Button(rep, text="back", bg='white', command=repback).grid(row=1, column=8)
    Label(rep,text='Report:', font='Harrington 16 bold underline' ,bg='white').grid(row=2,column=0)
    rep.mainloop()

def repback():
    rep.destroy()
    Home()
def process():
    global pro
    pro=Tk()
    pro.geometry('1024x577')
    pro.configure(bg='white', cursor='circle')
    pic=PhotoImage(file="softwall.gif")
    Label(pro,image=pic).grid(row=0,column=0,rowspan=10,columnspan=10)
    pro.title("SQL Injection Vulnerability Scanner")
    Label(pro,text='SQL Injection Vulnerability Scanner', font='Harrington 18 bold' ).grid(row=1,column=0,columnspan=10)
    Label(pro,text='Processing:', font='Harrington 16 bold underline' ,bg='white').grid(row=2,column=0)
    Label(pro,text='Testing errors', font='Harrington 14 bold underline' ,bg='white').grid(row=3,column=0)
    #for x in results:
        
    pro.mainloop()
def Home():
    global p1
    p1=Tk()
    global s
    p1.geometry('1024x577')
    p1.configure(bg='white', cursor='circle')
    pic=PhotoImage(file="softwall.gif")
    Label(p1,image=pic).grid(row=0,column=0,rowspan=10,columnspan=10)
    p1.title("SQL Injection Vulnerability Scanner")
    Label(p1,text='SQL Injection Vulnerability Scanner', font='Harrington 18 bold' ).grid(row=0,column=0,columnspan=10)
    Label(p1,text='Website:', font='Harrington 14 bold' ,bg='white').grid(row=2,column=0)
    s=Entry(p1,bg='LightCyan4', cursor='dot')
    s.grid(row=2,column=1,columnspan=5,sticky='EW')
    Label(p1,text='Injection file select:', font='Harrington 14 bold' ,bg='white').grid(row=8,column=0)
    def fileselect():
        injectionfile=askopenfilename(title = "Select injection  dictionary file",filetypes = (("text files","*.txt"),))
        f = open(injectionfile, "r")
        global name
        name = f.read().splitlines()
        print(name)

    def webget():
        global wsite
        wsite=str(s.get()+"FUZZ")
        print(wsite)
    def checkvuln(wsite,name):
        inject=[]
        global result
        for x in name:
            sqlinject=x
            inject.append(wsite.replace("FUZZ",sqlinject))
        result=injector(inject)
        checkres()

    def checkres():
        if not result:
            print ("Not vulnerable")

    
    Button(p1, text='select file', command=fileselect, bg='white', cursor='dot').grid(row=8, column=1)
    Button(p1, text="EXPLOIT",bg='white',command=lambda:[webget(),'''checkvuln(wsite,name),'''process()]).grid(row=6,column=8, sticky='EWNS')
    p1.mainloop()
Home()

