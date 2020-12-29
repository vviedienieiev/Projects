import tkinter


window = tkinter.Tk()
window.minsize(width=200,height=100)
window.title("First GUI Programm")
window.config(padx=20, pady=20)


input = tkinter.Entry(width=10)
input.grid(column=1, row=0)

miles_label = tkinter.Label(text="Miles", font = ("Arial", 18, "normal"))
miles_label.grid(column=2, row=0)

equal_label = tkinter.Label(text="is equal to ", font = ("Arial", 18, "normal"))
equal_label.grid(column=0, row=1)

km = tkinter.Label(text="0", font = ("Arial", 18, "normal"))
km.grid(column=1, row=1)

km_label = tkinter.Label(text="Km", font = ("Arial", 18, "normal"))
km_label.grid(column=2, row=1)

def button_clicked():
    km["text"] = int(round(float(input.get())*1.61,0))

button = tkinter.Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)


window.mainloop()