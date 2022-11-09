#!/usr/bin/env python3
"""MDalavai | Currency Converter"""
import tkinter as tk
from tkinter import ttk
from tkinter import CENTER, SOLID, NW, FALSE
from tkinter import Frame, Label, Button, Entry
import json
import time
import requests
import pyfiglet
from helper import exchange_rate, list_currencies


# Currency converting and tkinter windohwh
def convert_window():
    """Converting currencies and Tkinter window"""

    #colors
    cor0 = "#BFD7ED"
    cor1 = "#36454F"
    cor2 = "#0074B7"


    #creating the window
    root = tk.Tk()
    root.title('converter')
    root.configure(bg=cor0)
    root.geometry('400x420')
    root.resizable(height= FALSE, width=FALSE)

    #Frames
    top = Frame(root, width=400, height=60, bg=cor2)
    top.grid(row=0,column=0)
    main_frame = Frame(root, width=400, height=260, bg=cor0)
    main_frame.grid(row=1,column=0)
    #create a function convert amount
    def convert():
        """Currency is converter in this function"""
        url = "https://currency-converter18.p.rapidapi.com/api/v1/convert"
        currency1 = combo1.get()
        currency2 = combo2.get()
        amount = value.get()
        querystring = {"from":currency1,"to":currency2,"amount":amount}
        if currency2 == 'USD':
            symbol = '$'
        elif currency2 == 'INR':
            symbol = '₹'
        elif currency2 == 'EUR':
            symbol = '€'
        elif currency2 == 'BRL':
            symbol = 'R$'
        elif currency2 == 'CAD':
            symbol = 'CA$'
        headers = {
	    "X-RapidAPI-Key": "f28ba617dcmshd66f7ecf9ae61c6p17dd07jsne9a5c2bce5ed",
	    "X-RapidAPI-Host": "currency-converter18.p.rapidapi.com"
        }
        response = requests.request("GET", url, headers=headers, params=querystring, timeout=10)
        data = json.loads(response.text)
        convert_amt = data["result"]["convertedAmount"]
        format_amt = symbol + "{:,.2f}".format(convert_amt)
        result['text'] = format_amt
        print(f"Converted : {convert_amt}, {format_amt}")

    app_name = Label(top, text = 'Currency Converter', anchor="center",
    font=('Arial 16 bold'), bg=cor2, fg=cor0)
    app_name.place(relx ='0.25', rely = '0.2')
    #main frame
    result = Label(main_frame, text = "", width=18, height=2, pady=7, relief="solid",anchor=CENTER, font=('Ivy 15 bold'), bg=cor0, fg=cor1)
    result.place(x=90, y=10)
    currency_list  = ['CAD', 'BRL', 'EUR', 'INR','USD']
    #from label
    from_label = Label(main_frame, text = "From", width=8, height=1, pady=0, padx=0, relief="flat", anchor=NW, font=('Ivy 15 bold'), bg=cor0, fg=cor1)
    from_label.place(x=48,y=90)
    combo1 = ttk.Combobox(main_frame, width=8, justify=CENTER, font=("Ivy 12 bold"))
    combo1['values'] = (currency_list)
    combo1.place(x=50, y=115)
    #to label
    to_label = Label(main_frame, text = "To", width=8, height=1, pady=0, padx=0, relief="flat", anchor=NW, font=('Ivy 15 bold'), bg=cor0, fg=cor1)
    to_label.place(x=250,y=90)
    combo2 = ttk.Combobox(main_frame, width=8, justify=CENTER, font=("Ivy 12 bold"))
    combo2['values'] = (currency_list)
    combo2.place(x=250, y=115)
    #for enter the amount
    value = Entry(main_frame, width=30,justify=CENTER, font=("Ivy 12 bold"), relief=SOLID)
    value.place(x=60, y=170)
    #to click converter button
    button = Button(main_frame, text="Converter", width=19, height=1, padx=5, font=('Ivy 12 bold'), bg=cor2, fg=cor0, command=convert)
    button.place(x=95, y=220)
    root.mainloop()

# main function
def main():
    """Main function to get the user selected inputs"""
    welcome = pyfiglet.figlet_format("Curency Converter", font = "bubble")
    print(welcome,flush=True)
    time.sleep(2)
    user_name = input("Enter your Name --> ")
    time.sleep(2)
    print(f"Hello {user_name}! Welcome to the Currency Converter..\n", end='',flush=True)
    time.sleep(2)

    while True:
        print("------------------------------------------------")
        print("List - lists the different currencies")
        print("Convert - convert from one currency to another")
        print("Rate - get the exchange rate of two currencies")
        print("---------------------------------------------------- \n")
        answer = input("Enter a option from the List above  or  q to quit: \n").lower()
        time.sleep(2)
        if answer == 'q':
            break
        if answer == 'list':
            list_currencies()
        elif answer == 'convert':
            convert_window()
        elif answer == 'rate':
            currency1 = input("Enter a base currency: ").upper
            currency2 = input("Enter a currency to convert to: ").upper()
            exchange_rate(currency1, currency2)
        else:
            print("Sorry! You have not choosen a Valid input")
    end_messeage = pyfiglet.figlet_format("Thank you! for using Currency Converter", font = "digital")
    print(end_messeage)

if __name__ == "__main__":
        main()