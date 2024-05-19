from tkinter import *


def miles_to_km():
    miles = float(mile_input.get())
    kilometer = miles * 1.609
    result.config(text=f"{kilometer}")

window = Tk()
window.title("Miles to km converter")
window.config(padx=20, pady=20)

mile_input = Entry(width=10)
mile_input.grid(column=2, row=1)
mile_input.get()


mile_lab = Label(text="Miles")
mile_lab.grid(column=3, row=1)

is_equal = Label(text="is equal to")
is_equal.grid(column=1, row=2)

result = Label(text="0")
result.grid(column=2, row=2)

km = Label(text="Km")
km.grid(column=3, row=2)


mile_button = Button(text="calculate", command=miles_to_km)
mile_button.grid(column=2, row=3)


window.mainloop()