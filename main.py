from tkinter import *
window = Tk()
window.minsize(height=500, width=500)
window.title("Distance Converter")


def restart():
    miles.config(text= "Miles")
    label3.config(text= "Km")
    mile_speed.delete(first=0, last=7)
    label4.config(text="0")


def miles_to_km():
    miles.config(text="Miles")
    label3.config(text="Km")
    miles_value = float(mile_speed.get())
    km = miles_value * 1.609
    km_round = km.__round__(2)
    label4.config(text= km_round)


def kilometer_to_miles():
    miles.config(text="Km")
    label3.config(text="miles")
    miles_value = float(mile_speed.get())
    km = miles_value / 1.609
    km_round = km.__round__(2)
    label4.config(text=km_round)


def kilometer_to_meter():
    miles.config(text="Km")
    label3.config(text="Metre")
    miles_value = float(mile_speed.get())
    km = miles_value * 1000
    km_round = km.__round__(2)
    label4.config(text=km_round)


def miles_to_meter():
    miles.config(text="Miles")
    label3.config(text="Metre")
    miles_value = float(mile_speed.get())
    km = miles_value * 1609.3
    km_round = km.__round__(2)
    label4.config(text=km_round)


def meter_to_miles():
    miles.config(text="Metre")
    label3.config(text="Miles")
    miles_value = float(mile_speed.get())
    km = miles_value / 1609
    km_round = km.__round__(2)
    label4.config(text=km_round)


def meter_to_km():
    miles.config(text= "Metre")
    label3.config(text= "Km")
    miles_value = float(mile_speed.get())
    km = miles_value / 1000
    km_round = km.__round__(2)
    label4.config(text=km_round)


button = Button(text= "Restart", font=("Arial", 10, "bold"), command= restart)
button.place(x = 225 , y = 85)


mile_speed = Entry(width= 20)
mile_speed.place(x = 197, y = 120)
mile_speed.focus()

miles = Label(text= "Miles", font=("Arial", 12, "bold"))
miles.place(x= 325, y = 116)
label2 = Label(text= "is equal to", font=("Arial", 12, "bold"))
label2.place(x = 100, y = 145)
label3 = Label(text= "Kilometre", font=("Arial", 12, "bold"))
label3.place(x = 300, y = 145)
label4 = Label(text= "0", font=("Arial", 12, "bold"))
label4.place(x = 210, y = 145)


def listed(event):
    if listbox.get(listbox.curselection()) == "Kilometre to Metre":
        if mile_speed.get() != "":
            kilometer_to_meter()
    elif listbox.get(listbox.curselection()) == "Metre to Kilometre":
        if mile_speed.get() != "":
            meter_to_km()
    elif listbox.get(listbox.curselection()) == "Kilometre to Miles":
        if mile_speed.get() != "":
            kilometer_to_miles()
    elif listbox.get(listbox.curselection()) == "Miles to Kilometre":
        if mile_speed.get() != "":
            miles_to_km()
    elif listbox.get(listbox.curselection()) == "Metre to Miles":
        if mile_speed.get() != "":
            meter_to_miles()
    elif listbox.get(listbox.curselection()) == "Miles to Metre":
        if mile_speed.get() != "":
            miles_to_meter()
    print(listbox.get(listbox.curselection()))


listbox = Listbox(height=3)
conversions = ["Kilometre to Miles", "Miles to Kilometre", "Kilometre to Metre", "Miles to Metre", "Metre to Kilometre", "Metre to Miles"]
for items in conversions:
    listbox.insert(conversions.index(items), items)
listbox.bind("<<ListboxSelect>>", listed)
listbox.place(x=300, y=220)


window.mainloop()