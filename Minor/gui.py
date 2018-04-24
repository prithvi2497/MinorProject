from Tkinter import *
from tkMessageBox import *
from tkFileDialog import *
import sqlite3
from SQLinjector import *
import time


def checkvuln(wsite,name):
         inject=[]
         global result
         for x in name:
             sqlinject=x
             inject.append(wsite.replace("FUZZ",sqlinject))
         result=injector(inject)
         process()
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
    p1.destroy()
    pro=Tk()
    pro.geometry('1024x577')
    pro.configure(bg='white', cursor='circle')
    pic=PhotoImage(file="softwall.gif")
    Label(pro,image=pic).grid(row=0,column=0,rowspan=10,columnspan=10)
    pro.title("SQL Injection Vulnerability Scanner")
    Label(pro,text='SQL Injection Vulnerability Scanner', font='Harrington 18 bold' ).grid(row=1,column=0,columnspan=10)
    Label(pro,text='Processing:', font='Harrington 16 bold underline' ,bg='white').grid(row=2,column=0,sticky='W')
    Label(pro,text='Testing errors:-', font='Harrington 14 bold ' ,bg='white').grid(row=3,column=0,sticky='W')
    '''def testres(wsite,name):
        inject=[]
        for z in name:
                y=(wsite.replace("FUZZ",z))
                Label(pro,text='' , bg='white').grid(row=4,column=0,sticky='EWNS')
                Label(pro,text=y, bg='white').grid(row=4,column=0,sticky='EW')
                break'''
    global i
    i=int(0)
    for x in result:
            i=int(i+1)
            Label(pro,text=x,font='Harrington 12 bold',bg='white').grid(row=5+i,column=0,sticky='NS')
    '''for k in range(12):
            testres(wsite,name)'''
    showinfo('Results','Website is vulnerable to sql injection')
    pro.mainloop()


def checkres():
        if not result:
            print ("Not vulnerable")

            
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
        
    Button(p1, text='select file', command=fileselect, bg='white', cursor='dot').grid(row=8, column=1)
    Button(p1, text="EXPLOIT",bg='white',command=lambda:[webget(),checkvuln(wsite,name)]).grid(row=6,column=8, sticky='EWNS')
    p1.mainloop()
Home()

