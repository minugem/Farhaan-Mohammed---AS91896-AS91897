#Julie's Party Hire Store Tracker

from tkinter import*
import random
import re

def GUI(): #The Interface of the Program
    global full_name

    #Name
    Label(main_window, text="Name :") .grid(row=1, column=1) #Making a Label for the Name Entry
    name = Entry(main_window)
    name.grid(row=1, column=2, padx=10, pady=10, columnspan=2)

    #Reciept
    Label(main_window, text="Reciept No. :") .grid(row=2, column=1) #Making a Label for the Reciept Number
    Reciept = Entry(main_window)
    Reciept.grid(row=2, column=2, padx=10, pady=10, columnspan=2)

    #What item was Hired
    Label(main_window, text="Item :") .grid(row=3, column=1) #Making a Label for the Item that was Hired
    item = Entry(main_window)
    item.grid(row=3, column=2, padx=10, pady=10, columnspan=2)

    #Quantity
    Label(main_window, text="Quantity :") .grid(row=4, column=1) #Making a Label for the Quantity of Items Hired
    quantity = Entry(main_window)
    quantity.grid(row=4, column=2, padx=10, pady=10, columnspan=2)
    
#Running the Interface
def main():
    global main_window
    global name
    main_window =Tk()
    GUI()  
 
    main_window.title("Julie's Tracker")
    
    main_window.mainloop()

main()
