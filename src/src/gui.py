import tkinter as tk
import datetime as dt
from tkinter import ttk

LARGE_FONT= ("Verdana", 12)

print("Debug")
style = ttk.Style()
style.configure("Custom.TButton",
                 foreground="white",
                 background="black",
                 padding=[10, 10, 10, 10],
                 font="Verdana 12 underline")

class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.title("MentalOut")
        self.geometry("500x750")

        self.frames = {}

        for F in (HomePage, PageOne, PageTwo):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(HomePage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

        
class HomePage(tk.Frame):

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


class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="How was your day today?", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        v = tk.StringVar(self, "1")

        values = {"Terrible" : "1",
                "Not Well" : "2",
                "Fine" : "3",
                "Pretty Good" : "4",
                "Outstanding" : "5"}

        for (text, value) in values.items():
            tk.Radiobutton(self, text = text, variable = v,
                value = value).pack()

        entry1 = tk.Text(self, width= 30, height= 20, font=("Verdana", 12, "normal"))
        entry1.pack()

        button1 = ttk.Button(self, text="Save",
                             command=lambda: self.saveDay(entry1, v))
        button1.pack()

        button2 = ttk.Button(self, text="Main Menu",
                            command=lambda: controller.show_frame(HomePage))
        button2.pack()

    def saveDay(self, entry, v):
        now = dt.datetime.now()
        INPUT = entry.get("1.0", "end-1c")
        with open("days.txt", "a") as file:
            file.writelines(v.get() + " " + now.strftime("%m/%d/%Y, %H:%M:%S") + " " + INPUT + "\n")

class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Look back on your best days.", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Main Menu",
                            command=lambda: controller.show_frame(HomePage))
        button1.pack()

app = App()
app.mainloop()
