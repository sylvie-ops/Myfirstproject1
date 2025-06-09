# binary = input("Enter a binary number: ")
# decimal = int(binary, 2)
# print(f"The decimal value of {binary} is {decimal}")

number1=int(input("Enter  first number: "))
number2=int(input("Enter second number: "))
Operator=input("Enter an operato(+,_,*,/,or %):")
if Operator == "+" :
    print(number1+number2)
elif Operator=="-":
    print(number1-number2)
elif Operator=="%":
    print(number1%number2)
elif Operator=="*":
    print(number1*number2)
elif Operator=="/":
    if number2!=0:
      print(number1/number2)
    else:
     print("error")
else:
 print("Not on you level please , try to use (+,_,*,/,or %" )




