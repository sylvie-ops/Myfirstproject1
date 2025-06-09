a = float (input("Enter price: "))
print("Price:", a)
if a >= 300:
    print("You will pay:", a - (a * 0.30))
elif 200 <= a < 300:
    print("You will pay:", a - (a * 0.20))
elif 100 <= a < 200:
    print("You will pay:", a - (a * 0.12))
elif a < 100:
    print("You will pay:", a - (a * 0.10))
else:
    print("No discount and you will not pay.")
