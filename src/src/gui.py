from tkinter import *
import tkinter as tk
import datetime

class menuButton(tk.Button):
    
    def PresentWindow():
        window = Toplevel()
        window.geometry('400x400')
        newlabel = Label(window, text = "How do you feel today?")
        newlabel.pack()
    def PastWindow():
        window = Toplevel()
        window.geometry('400x400')
        newlabel = Label(window, text = "Here are some of your  best days")
        newlabel.pack()
    def SettingWindow():
        window = Toplevel()
        window.geometry('400x400')
        newlabel = Label(window, text = "Settings Window")
        newlabel.pack()
    def ExitApp():
        root.destroy()
 
root = Tk()
root.geometry('500x500')
 
frame = Frame(root, borderwidth= 2, relief= 'sunken')
frame.pack()

launch = Label(frame, text= "You launched at:")
launch.pack()

time = Label(frame, text= datetime.datetime.today())
time.pack()

currentButton = menuButton(frame, text= "Today", command=menuButton.PresentWindow)
currentButton.pack(pady=10)

pastButton = menuButton(frame, text= "Past", command= menuButton.PastWindow)
pastButton.pack(pady=10)

optionButton = menuButton(frame, text = "Options", command = menuButton.SettingWindow)
optionButton.pack(pady = 10)

exitButton = menuButton(frame, text= "Quit", command= menuButton.ExitApp)
exitButton.pack(pady = 10)

root.title("App")
root.mainloop()