#Julie's Party Hire Store Tracker

from tkinter import*


#Quit the Program
def quit(): 
    main_window.destroy()

#Store the Data
def store_details ():
    global print_details, name, receipt, item, quantity, list_entries, total_names
    name = name.get()
    receipt = receipt.get()
    item = item.get()
    quantity = quantity.get()

#Print the Data
def print_details ():
    global print_details, name, receipt, item, quantity, list_entries, total_names

    #The Variable total_names is set to 0
    total_names = 0
    
    #Makes Labels for Row, Name, Receipt No., Item and Quantity
    Label(main_window,text="Row").grid(column=0,row=10, pady=(20,5))
    Label(main_window,text="Name").grid(column=1,row=10, pady=(20,5))
    Label(main_window,text="Receipt No.").grid(column=2,row=10, pady=(20,5))
    Label(main_window,text="Item").grid(column=3,row=10, pady=(20,5))
    Label(main_window,text="Quantity").grid(column=4,row=10, padx=(35,0), pady=(20,5))

    #Displays the Label values
    Label(main_window, text=total_names).grid(column=0,row=total_names+11)
    Label(main_window, text=(name)).grid(column=1,row=total_names+11)
    Label(main_window, text=(receipt)).grid(column=2,row=total_names+11)
    Label(main_window, text=(item)).grid(column=3,row=total_names+11)
    Label(main_window, text=(quantity)).grid(column=4,row=total_names+11)
    main_window.geometry("")
    
    #Increases total_names by 1
    total_names += 1
    



def GUI(): #The Interface of the Program
    global details, name, receipt, item, quantity, list_entries, total_names
    
    #Name
    Label(main_window, text="Name :") .grid(row=1, column=1) #Making a Label for the Name Entry
    name = Entry(main_window)
    name.grid(row=1, column=2, padx=10, pady=10, columnspan=2)


    #Reciept
    Label(main_window, text="Reciept No. :") .grid(row=2, column=1) #Making a Label for the Reciept Number
    receipt = Entry(main_window)
    receipt.grid(row=2, column=2, padx=10, pady=10, columnspan=2)

    #What item was Hired
    Label(main_window, text="Item :") .grid(row=3, column=1) #Making a Label for the Item that was Hired
    item = Entry(main_window)
    item.grid(row=3, column=2, padx=10, pady=10, columnspan=2)

    #Quantity
    Label(main_window, text="Quantity :") .grid(row=4, column=1) #Making a Label for the Quantity of Items Hired
    quantity = Entry(main_window)
    quantity.grid(row=4, column=2, padx=10, pady=10, columnspan=2)

    #Quit Button
    Button(main_window, text="Quit", width= 8, command= quit) .grid(row=0, column=1, padx=0, pady = 10) #Making a button to Quit the Program

    #Store Details
    Button(main_window, text="Store Details", width= 8, command= store_details) .grid(row=0, column=2, padx=0, pady = 10) #Making a Button to Store the details you enter

    #Print Details
    Button(main_window, text="Print Details", width= 8, command= print_details) .grid(row=0, column=3, padx=0, pady = 10) #Button to execute the print command

#Running the Interface
def main():
    global main_window
    global details, name, receipt, item, quantity, list_entries, total_names
    main_window =Tk()
    GUI()
    
 
    main_window.title("Julie's Tracker")
    
    main_window.mainloop()

main()
