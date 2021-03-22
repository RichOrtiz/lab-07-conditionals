firstNum = input("Enter your first number: ")
secondNum = input("Enter your second number: ")


multiplied = int(firstNum) * int(secondNum)
divided = int(firstNum) / int(secondNum)
modulo = int(firstNum) % int(secondNum)

response = input("What operation do you want to do? Multiply(mult), Divide(div), or Modulo(mod)?  ")

if (response == "mult"): 
    print(multiplied)

elif (response == "div"): 
    print(divided)
        
elif (response == "mod"): 
    print(modulo)
        
else: 
    print("*** iNvAlId OpErAtIoN ***")
        
