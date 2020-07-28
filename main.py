#Creating a Basic Calculator
from tkinter import *
root = Tk()
root.title("Simple Calculator")
root.configure(background = "red")
root.geometry("500x900")

def click(event):
    global scvalue
    text = event.widget.cget("text")
    
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get())
            except Exception as e:
                
                value="Error"

        scvalue.set(value)
        screen.update()

        
    elif text == "C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()    


scvalue = StringVar()
scvalue.set("")

screen = Entry(root, textvar = scvalue,bg="white", font = "lucida 60 italic")
screen.pack(fill = X, pady = 10, padx = 10)

f = Frame(root, bg = "red")
b = Button(f, text = "7",fg ="white",bg="green", padx = 20, pady = 20, font = "lucida 20 italic")
b.pack(side = LEFT, padx = 5, pady = 5)
b.bind("<Button-1>", click)


b = Button(f, text = "8",fg ="white",bg="green", padx = 20, pady = 20, font = "lucida 20 italic")
b.pack(side = LEFT, padx = 5, pady = 5)
b.bind("<Button-1>", click)

b = Button(f, text = "9",fg ="white",bg="green", padx = 20, pady = 20, font = "lucida 20 italic")
b.pack(side = LEFT, padx = 5, pady = 5)
b.bind("<Button-1>", click)

b = Button(f, text = "/",fg ="white",bg="green", padx = 22, pady = 20, font = "lucida 20 italic")
b.pack(side = LEFT, padx = 5, pady = 5)
b.bind("<Button-1>", click)



f.pack()

f = Frame(root, bg = "red")
b = Button(f, text = "4",fg ="white",bg="green", padx = 20, pady = 20, font = "lucida 20 italic")
b.pack(side = LEFT, padx = 5, pady = 5)
b.bind("<Button-1>", click)


b = Button(f, text = "5",fg ="white",bg="green", padx = 20, pady = 20, font = "lucida 20 italic")
b.pack(side = LEFT, padx = 5, pady = 5)
b.bind("<Button-1>", click)

b = Button(f, text = "6",fg ="white",bg="green", padx = 20, pady = 20, font = "lucida 20 italic")
b.pack(side = LEFT, padx = 5, pady = 5)
b.bind("<Button-1>", click)

b = Button(f, text = "*",fg ="white",bg="green", padx = 20, pady = 20, font = "lucida 20 italic")
b.pack(side = LEFT, padx = 5, pady = 5)
b.bind("<Button-1>", click)



f.pack()

f = Frame(root, bg = "red")
b = Button(f, text = "1",fg ="white",bg="green", padx = 20, pady = 20, font = "lucida 20 italic")
b.pack(side = LEFT, padx = 5, pady = 5)
b.bind("<Button-1>", click)


b = Button(f, text = "2",fg ="white",bg="green", padx = 20, pady = 20, font = "lucida 20 italic")
b.pack(side = LEFT, padx = 5, pady = 5)
b.bind("<Button-1>", click)

b = Button(f, text = "3",fg ="white",bg="green", padx = 20, pady = 20, font = "lucida 20 italic")
b.pack(side = LEFT, padx = 5, pady = 5)
b.bind("<Button-1>", click)

b = Button(f, text = "-",fg ="white",bg="green", padx = 20, pady = 20, font = "lucida 20 italic")
b.pack(side = LEFT, padx = 5, pady = 5)
b.bind("<Button-1>", click)


f.pack()

f = Frame(root, bg = "red")

b = Button(f, text = "0",fg ="white",bg="green", padx = 20, pady = 20, font = "lucida 20 italic")
b.pack(side = LEFT, padx = 5, pady = 5)
b.bind("<Button-1>", click)

b = Button(f, text = "00",fg ="white",bg="green", padx = 13, pady = 20, font = "lucida 20 italic")
b.pack(side = LEFT, padx = 5, pady = 5)
b.bind("<Button-1>", click)


b = Button(f, text = ".",fg ="white",bg="green", padx =22, pady = 20, font = "lucida 20 italic")
b.pack(side = LEFT, padx = 5, pady = 5)
b.bind("<Button-1>", click)


b = Button(f, text = "+",fg ="white",bg="green", padx = 16, pady = 20, font = "lucida 20 italic")
b.pack(side = LEFT, padx = 5, pady = 5)
b.bind("<Button-1>", click)



f.pack()

f = Frame(root, bg = "red")
b = Button(f, text = "C",fg ="white",bg="green", padx = 15, pady = 20, font = "lucida 20 italic")
b.pack(side = LEFT, padx = 5, pady = 5)
b.bind("<Button-1>", click)

b = Button(f, text = "=",fg ="white",bg="orange", padx = 64, pady = 20, font = "lucida 20 italic")
b.pack(side = LEFT, padx = 5, pady = 5)
b.bind("<Button-1>", click)



b = Button(f, text = "%",fg ="white",bg="green", padx = 13, pady = 20, font = "lucida 20 italic")
b.pack(side = LEFT, padx = 5, pady = 5)
b.bind("<Button-1>", click)



f.pack()






root.mainloop()