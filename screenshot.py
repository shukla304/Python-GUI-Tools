from tkinter import *
from PIL import Image, ImageTk
import pyautogui, time
import os


### To Take Screenshot and Save it #############
def name():
    string=e1.get()
    string=string+'.png'  #saved in PNG 
    #time.sleep(1)
    screenshot = pyautogui.screenshot()
    screenshot.save(string)
    
### Show the Pictures Present in Gallery {Saved Screenshot}#####    
def gallery():
    arr = os.listdir()  #Stores files name in the list 
    j=4
    k=0
    for i in arr:
        if(k>5):  # To move to another row
            k=0
            j=j+1 
        if(i.endswith('.png')):  ##Checks for png files
            fn = i
            #print(fn)         
            width=250
            height=250
            load = Image.open(fn)
            load = load.resize((width,height), Image.ANTIALIAS)  # TO Resize Image
            render = ImageTk.PhotoImage(load)
            img = Label(root, image=render)
            img.image = render
            img.place(x=125+k, y=10+k)
            img.grid(row=j,column=k)
            Label(root, text=fn,height=1,width=30,bg="white",borderwidth=2, relief="solid").grid(row=j,column=k,padx=10+k,pady=10+k)
            k=k+1  # To print in column order 

### Main Window
root = Tk() 
root.title("ScreenShot Tool")
Label(root, text='Enter File Name',height=1,width=30,bg="white",borderwidth=2, relief="solid").grid(row=0,padx=10,pady=10)     
e1=Entry(root)  # Input Field
e1.configure(background='white',width=30,borderwidth=2, relief="solid")
e1.grid(row=0,column=1,padx=30,pady=20)
e1.bind('<Return>',name)  # Binding Fuction
root.config(background="white")
Button(root,text="Gallery",command=gallery,width=20,bg="white",borderwidth=2,relief="solid").grid(row=1,column=0,pady=20,padx=50)
Button(root,text="Take Screenshot",command=name,width=20,bg="white",borderwidth=2,relief="solid").grid(row=1,column=1,pady=20,padx=50)
#Button(root,text="Close",command=root.destroy,width=20,bg="white",borderwidth=2,relief="solid").grid(row=1,column=0,pady=20,padx=50)
mainloop()

