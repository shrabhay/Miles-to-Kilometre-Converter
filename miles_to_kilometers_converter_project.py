from tkinter import *
import os
os.system('clear')

FONT = ('Verdana', 15)


def miles_to_km():
    miles = float(miles_entry.get())
    kms = miles * 1.609
    km_value_label.config(text=f'{round(kms, 3)}')


window = Tk()
window.minsize(height=100, width=300)
window.title('Miles to Kilometers Converter')
window.config(padx=20, pady=20)

miles_entry = Entry(width=10)
miles_entry.grid(column=1, row=0)

miles_label = Label(text='Miles', font=FONT)
miles_label.grid(column=2, row=0)

equals_label = Label(text='is equal to', font=FONT)
equals_label.grid(column=0, row=1)

km_value_label = Label(text='0', font=FONT)
km_value_label.grid(column=1, row=1)

km_label = Label(text='Km', font=FONT)
km_label.grid(column=2, row=1)

calculate_button = Button(text='Calculate', font=FONT, command=miles_to_km)
calculate_button.grid(column=1, row=2)

window.mainloop()
