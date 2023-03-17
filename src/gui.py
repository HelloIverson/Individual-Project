import tkinter as tk
import datetime as dt
from tkinter import ttk

LARGE_FONT= ("Verdana", 12)

#styling for windows that doesn't work too well
style = ttk.Style()
style.theme_use('clam')
style.configure("Custom.TButton",
                 foreground="white",
                 background="black",
                 padding=[10, 10, 10, 10],
                 font="Verdana 12 underline")

# this is the container for the app itself, and all pages you see are contained inside it
class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True) #creates a frame which will contain all navigable pages

        container.grid_rowconfigure(0, weight=1) # makes sure container is not displayed unnaturally with other pages
        container.grid_columnconfigure(0, weight=1)

        self.title("MentalOut") # title and window size at launch, can be changed
        self.geometry("500x750")

        self.frames = {} # creates a list to contain all frames in app

        for F in (HomePage, PageOne, PageTwo, PageThree): # creates frame based upon objects which are the pages you see

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(HomePage) # starts on home page

    def show_frame(self, cont): # mechanism for changing pages

        frame = self.frames[cont]
        frame.tkraise()

        
class HomePage(tk.Frame): # homepage with 3 buttons

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = ttk.Label(self, text="Main Menu", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button = ttk.Button(self, text="Today", style="Custom.TButton",
                            command=lambda: controller.show_frame(PageOne))
        button.pack()

        button2 = ttk.Button(self, text="Past Days", style="Custom.TButton", 
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack()

        button3 = ttk.Button(self, text="Best Days", style="Custom.TButton",
                            command=lambda: controller.show_frame(PageThree))
        button3.pack()


class PageOne(tk.Frame): # Page 1 with a button and a text entry
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="How was your day today?", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        v = tk.StringVar(self, "1") # creates a value that allows text entry data to be stored as a string

        values = {"Terrible" : "1",
                "Not Well" : "2",
                "Fine" : "3",
                "Pretty Good" : "4",
                "Outstanding" : "5"} # radiobutton options

        for (text, value) in values.items(): # foreach loop to pack radio buttons into frame
            tk.Radiobutton(self, text = text, variable = v,
                value = value).pack()

        entry1 = tk.Text(self, width= 30, height= 20, font=("Verdana", 12, "normal"))
        entry1.pack()

        # button which handles saving the text entry into a text file
        button1 = ttk.Button(self, text="Save",
                             command=lambda: [self.saveDay(entry1, v), controller.show_frame(HomePage)])
        button1.pack()

        # button to return to the main menu
        button2 = ttk.Button(self, text="Main Menu",
                            command=lambda: controller.show_frame(HomePage))
        button2.pack()

    # method which opens a text file and saves text entry data inside it along with date and time of entry
    def saveDay(self, entry, v):
        now = dt.datetime.now()
        INPUT = entry.get("1.0", "end-1c")
        with open("days.txt", "a") as file:
            file.writelines(v.get() + " " + now.strftime("%m/%d/%Y, %H:%M:%S") + " " + INPUT + "\n")

class PageTwo(tk.Frame):
    holder = []
    days = ""

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Look back on these past few days.", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        label2 = ttk.Label(self, text=self.lookBack(), wraplength=300,)
        label2.pack()

        button1 = ttk.Button(self, text="Main Menu",
                            command=lambda: controller.show_frame(HomePage))
        button1.pack()

    def lookBack(self): # method that reads from text file and displays a certain amount of the data onto the frame
        with open("days.txt", "r") as file:
            for line in file:
                self.holder.append(line)
        index = 0
        wordcount = 0
        while (index<1):
            for line in self.holder:
                for char in line:
                    wordcount += 1

            if (wordcount > 1500):
                self.holder.pop(0)
                wordcount = 0
            else:
                index+=1

        for line in self.holder:
            a = line[2:]
            self.days = self.days + a + ""

        return self.days
class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text = "Look back on your recent best 3 days.", font=LARGE_FONT)
        label.pack()

        label1 = ttk.Label(self, text=self.bestSearch(), wraplength=300)
        label1.pack()

        button2 = ttk.Button(self, text="Main Menu",
                            command=lambda: controller.show_frame(HomePage))
        button2.pack()

    def bestSearch(self):
        tops = []
        topDay = "1101101111111111111111111111"
        topDays = []
        showTopDays = ""
        with open("days.txt", "r") as file:
            for line in file:
                if (int(line[0:1]) > 2):
                    tops.append(line)

        for day in tops:
            if(int(day[0:1]) >= int(topDay[0:1])):
                if(int(day[8:12]) >= int(topDay[8:12])): #only needed if data is ever unordered
                    if(int(day[2:4]) >= int(topDay[2:4])):
                        if(int(day[5:7]) >= int(topDay[5:7])):
                            topDay = day
                            topDays.append(day)
                            if(len(topDays) > 3):
                                topDays.pop(0)
        for i in topDays:
            showTopDays = showTopDays + i[2:]
        return showTopDays


try:
    open("days.txt", "r")

except IOError:
    open("days.txt", "x")

app = App()
app.mainloop()
