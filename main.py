from tkinter import *
def button_clicked():
    print("i got clicked")
    new = input.get()
    my_label.config(text=new)

window = Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)
window.config(padx=10, pady=10)

# Label

my_label = Label(text="i am a label", font=("Arial", 24, "bold"))
my_label.config(text="new text")
my_label.grid(column=0, row=0)

# button

button = Button(text="Click me", command=button_clicked)
button.grid(column=1, row=1)

button1 = Button(text="new")
button1.grid(column=2, row=0)
# entry

input = Entry(width=10)
print(input.get())
input.grid(column=3, row=2)

window.mainloop()
