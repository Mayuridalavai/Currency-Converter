#!/usr/bin/env python3
"""MDalavai | Currency Converter"""

from locale import currency
from tkinter import *
from tkinter import Tk, ttk
import json
from tkinter.font import names
import pyfiglet
import requests
from helper import exchange_rate, list_currencies



# Currency converting and tkinter windohwh
def convert_window():
    """Converting currencies"""

    #colors
    cor0 = "#d7d7d5"
    cor1 = "#36454F"
    cor2 = "#FF5733"


    #creating the window
    window = Tk()
    window.title('converter')
    window.configure(bg=cor0)
    window.geometry('400x420')
    window.resizable(height= FALSE, width=FALSE)

    #Frames
    top = Frame(window, width=400, height=60, bg=cor2)
    top.grid(row=0,column=0)
    
    main_frame = Frame(window, width=400, height=260, bg=cor0)
    main_frame.grid(row=1,column=0)
    
    
    #create a function convert amount
    def convert():
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
    
        response = requests.request("GET", url, headers=headers, params=querystring)
        data = json.loads(response.text)
        converted_amount = data["result"]["convertedAmount"]
        formatted = symbol + "{:,.2f}".format(converted_amount)
        
        result['text'] = formatted
        
        print(f"Converted : {converted_amount}, Formatted : {formatted}")
    
    
    
    #top Frame
    #icon = Image.open('images/icons8-currency.png')
    #icon = icon.resize((40,40))
    
    app_name = Label(top, text = 'Currency Converter', anchor="center", font=('Arial 16 bold'), bg=cor2, fg=cor0)
    app_name.place(relx ='0.25', rely = '0.2')
    
    #main frame
    result = Label(main_frame, text = "", width=18, height=2, pady=7, relief="solid", anchor=CENTER, font=('Ivy 15 bold'), bg=cor0, fg=cor1)
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
    combo2 = ttk.Combobox(main, width=8, justify=CENTER, font=("Ivy 12 bold"))
    combo2['values'] = (currency_list)
    combo2.place(x=250, y=115)
    
    #for enter the amount
    value = Entry(main_frame, width=30,justify=CENTER, font=("Ivy 12 bold"), relief=SOLID)
    value.place(x=60, y=170)
    
    #to click converter button 
    button = Button(main_frame, text="Converter", width=19, height=1, padx=5, font=('Ivy 12 bold'), bg=cor2, fg=cor0, command=convert)
    button.place(x=95, y=220)
    
    
    window.mainloop()
    

# main function
def main():
    
    """_Main function to get the user inputs"""
    welcome = pyfiglet.figlet_format("Welcome to Curency Converter", font = "bubble")
    print(welcome)
    user_name = input("Enter your Name: ")
    print(user_name)
    print("------------------------------------------------")
    print("List - lists the different currencies")
    print("Convert - convert from one currency to another")
    print("Rate - get the exchange rate of two currencies")
    print("----------------------------------------------------")
    print("-----------------------------------------------------")

    while True:
        answer = input("Enter a option from the List above  or  q to quit: ").lower()
        

        if answer == 'q':
            break
        elif answer == 'list':
            list_currencies()
        elif answer == 'convert':
            convert_window()
        elif answer == 'rate':
            currency1 = input("Enter a base currency: ").upper()
            currency2 = input("Enter a currency to convert to: ").upper()
            exchange_rate(currency1, currency2)

        else:
            print("Invalid Entry")


    end_messeage = pyfiglet.figlet_format("Thank you! for using Currency Converter", font = "digital")
    print(end_messeage)


        
if __name__ == "__main__":
    main()    
