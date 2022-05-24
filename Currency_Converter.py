from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import tkinter.font as font
from forex_python.converter import CurrencyRates
from forex_python.bitcoin import BtcConverter

root = Tk()
root.title("CURRENCY CONVERTOR")
root.minsize(600,500)
root.maxsize(600,500)
HEIGHT = 500
WIDTH = 500
FONT = font.Font(family ="Engravers MT", size ="10", weight ="bold")


def clear():
    entry.delete(0,END)
    label_down["text"] = ""

def convert(c1,c2,amount):
    try:
        if amount == "":
            messagebox.showerror("Error", "Amount not specified")
        elif c1 == "Select" or c2 == "Select":
            messagebox.showinfo("Error", "Currency not selected")
        else:
            try:
                amount = float(amount)
                b = BtcConverter()
                c = CurrencyRates()
                if c1 == c2:
                    result = amount
                elif c1 == "BTC":
                    result = b.convert_btc_to_cur(amount, c2)
                elif c2 == "BTC":
                    result = b.convert_to_btc(amount, c1)
                else:
                    result = c.convert(c1, c2, int(amount))
                print(result)
                label_down["text"] = f"Conversion Result: \n{amount} {c1} = {result} {c2}"
            except ValueError:
                messagebox.showerror("Error", "Invalid amount")
                clear()
    except Exception:
        messagebox.showerror("Error", "Something went wrong. Please try again")
        
def help():
    newwin = Tk()
    newwin.title("Help")
    newwin.maxsize(400,300)
    newwin.minsize(400,300)
    newcanvas = Canvas(newwin, height = 400, width = 300)
    newcanvas.pack()
    
    newframe = Frame(newwin, bg ="white")
    newframe.place(relwidth = 2, relheight = 1)
    newlabel = Label(newframe, font = ("Comic Sans MS", 11, "bold"), fg ="#001a4d", anchor = "nw", justify = "left", bd =4)
    newlabel.place(relx = 0.05, rely = 0.05,relwidth = 0.90, relheight = 0.90)
    newlabel["text"] = "Abbrevations:\nBTC -> Bitcoin\nUSD ->US Dollar\nEUR -> Euro\nJPY -> Japnese Yen\nGBP -> Pound Sterling\nAUD -> Australian Dollar\nCAD -> Canadian Dollar\nINR -> Indian Rupees\nCNY -> Chinese Yuan"
    newbutton = Button(newframe, text = "Back",font = ("Comic Sans MS", 11, "bold"),  bg = "pink", fg = "black", activeforeground = "pink", activebackground = "black", command = lambda:newwin.destroy())
    newbutton.place(relx = 0.76, rely = 0.82, relwidth = 0.14, relheight = 0.11)
    newwin.mainloop()

def exit():
    root.destroy()

canvas = Canvas(root, height = HEIGHT, width = WIDTH)
canvas.pack()

background_image = ImageTk.PhotoImage(Image.open("D:\\currency.jpg"))
background_label = Label(root, image = background_image)
background_label.place(relwidth = 1, relheight =1)
Label(root, text = "Created By: Aditya Tyagi", font = ('Lora',12)).place(x=400,y=460)

frame = Frame(root, bg ="yellow", bd =5) 
frame.place(relx = 0.5, rely = 0.1, relwidth = 0.80, relheight = 0.25, anchor = "n")

label_up = Label(frame)
label_up.place(relwidth = 1 , relheight = 1)

options = [
    "BTC",
    "USD",
    "EUR",
    "JPY",
    "GBP",
    "AUD",
    "CAD", 
    "INR",
    "CNY"
]

clicked1 = StringVar()
clicked1.set("FROM")

listbox1 = OptionMenu(frame,clicked1, *options)
listbox1.config(bg = "#fc034e", fg = "black", activeforeground = "#fc034e", activebackground = "black", font=FONT)
listbox1.place(relx = 0.06,rely = 0.3, relheight = 0.28, relwidth = 0.32)

image = PhotoImage(file = "D:\\images2.png")
img_label = Label(frame, image = image)
img_label.place(relx = 0.40, rely = 0.18)

clicked2 = StringVar()
clicked2.set("TO")
listbox2 = OptionMenu(frame,clicked2, *options)
listbox2.config(bg = "#fc034e", fg = "black", activeforeground = "#fc034e", activebackground = "black", font=FONT)
listbox2.place(relx = 0.56,rely = 0.3, relheight = 0.28, relwidth = 0.32)

label3 = Label(frame, text = "AMOUNT", font = FONT, bg = "#12a4d9", highlightbackground = "#12a4d9", fg = "white")
label3.place(relx = 0.26,rely = 0.7,relwidth = 0.2, relheight = 0.25)

entry = Entry(frame, font = FONT, fg = "#001a4d")
entry.place(relx = 0.54, rely = 0.7, relwidth=0.26, relheight = 0.25)

button1 = Button(root, text = "CONVERT", font = FONT,bd=6, bg = "pink", fg = "black", activeforeground = "pink", activebackground = "black", command = lambda:convert(clicked1.get(), clicked2.get(), entry.get()))
button1.place(relx = 0.13,rely = 0.4,relwidth = 0.18, relheight = 0.07)

button2 = Button(root, text = "CLEAR", font = FONT,bd=6, bg = "pink", fg = "black", activeforeground = "pink", activebackground = "black", command = clear)
button2.place(relx = 0.35,rely = 0.4,relwidth = 0.15, relheight = 0.07)

button3 = Button(root, text = "Help", font = FONT,bd=6, bg = "pink", fg = "black", activeforeground = "pink", activebackground = "black",  command = help)
button3.place(relx = 0.52, rely = 0.4, relwidth = 0.15, relheight = 0.07)

button4= Button(root, text = "EXIT", font = FONT,bd=6, bg = "pink", fg = "black", activeforeground = "pink", activebackground = "black",  command = exit)
button4.place(relx = 0.7, rely = 0.4, relwidth = 0.12, relheight = 0.07)

lower_frame = Frame(root, bg ="red", bd =5)
lower_frame.place(relx = 0.5, rely = 0.6, relwidth = 0.8, relheight = 0.25, anchor = "n")

FONT = font.Font(family ="Comic Sans MS", size ="12", weight ="bold")
label_down = Label(lower_frame, font = FONT, fg = "#2438b5", anchor = "nw", justify = "left", bd =4)
label_down.place( relwidth=1, relheight = 1)

root.mainloop()