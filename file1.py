#author:Kanchi Chitaliya, kach6618@colorado.edu
#purpose:Create GUI wtih 3 buttons using tkinter
#date:12/5/2017
#filename:KChitaliya-HW-10.zip (file1.py)

from tkinter import *
import socket
import requests
import re

root=Tk()
root.geometry('480x360')
window=Label(root,text="")
window.pack()

def ip_addr():
    try:
        p=socket.gethostbyname("www.colorado.edu")
        window.configure(text=p)
    except:
        window.configure(text="Not Connected to the internet")

        
def search_title():
    try:
        r=requests.get("http://www.colorado.edu")
        header=re.findall(r'<title>Home \| (.*) </title>',r.text)[0]
        window.configure(text=header)
    except:
        window.configure(text="Not Connected to the internet")
    
def endwindow():
    root.destroy()
      
button3=Button(root,text="Close",command=endwindow,bg="red",fg="white")
button1=Button(root,text="Get IP",command=ip_addr,bg="blue",fg="white")
button2=Button(root,text="Get Title",command=search_title,bg="black",fg="white")

button1.pack(fill=X,padx=15,pady=30)
button2.pack(fill=X,padx=15,pady=30)
button3.pack(pady=30)
root.mainloop()

