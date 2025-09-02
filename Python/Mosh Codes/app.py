print("The price of the house is 1M")
price = 1_000_000
income = int(input("What is your income? : $"))
credit = input("Do you have a good credit score? Yes/No: ")
if credit.upper() == 'YES' and income>=100_000:
    print(f"The down payment the house is: ${str(price*0.10)} and you are eligible for a loan")
elif credit.upper() == 'NO' and income<100_000:
    print(f"The down payment the house is: ${str(price*0.20)} and unaku loan kedaiyaadhu poda")
else:
    print("Kurutu kabodhi")




