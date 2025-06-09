# mylist=["apple","banana","banana","rice"]
# print(mylist[2])
# for letter in "Python":
#     print(letter)
# list=["Apple","Pineapple","Pawpaw","Orange"]
# print(",".join(list))
# print(f"{list}")
#num_list = [7,8, 4, 23, 6, 18, 27, 47]hj
#for n in num_list:
  #if n > 10:
    #print(n)
  #break
# n = 2 # Could be any number
# a = 0
# val = n
# while val < 48:
#       a += 1
#       val *=n
# print(a)

# maximum = min("Ban", "Batman")
# print(maximum)

# def pacifique(a,b,c):
#     print(a+b+c)

# pacifique(1,2,3)


# def sylvie(numb1, numb2, numb3):
    
# numb1=int(input("Enter the first number:"))
# numb2=int(input("Enter the second number:"))
# numb3=int(input("Enter the third number:"))

# return max(numb1, numb2, numb3)
# print("the largest number", sylvie(numb1,numb2,numb3))
# def maximum(a, b, c):
#     e = max(a, b, c)
#     print(e)

# d = int(input("Enter 1st number: "))
# e = int(input("Enter 2nd number: "))
# f = int(input("Enter 3rd number: "))

# maximum(d, e, f)

# def is_prime(a):
#     for a in range(1,50):
#         if a /a and a/1:
#             print (a)

# # number=int(input("enter a number: ")) 
# # is_prime(number)         
# def is_prime(a):
#     a = int(a)
#     if a <= 1:
#         print(a, "is not a prime number")
#         return

#     for i in range(2, a):
#         if a % i == 0:
#             print(a, "is not a prime number")
#             return
#     print(a, "is a prime number")

# number = input("Enter a number: ")
# is_prime(number)
# def is_prime(num):
#        if num < 2:
#            return False
#        for i in range(2, int(num ** 0.5) + 1):
#            if num % i == 0:
#                return False
#        return True
#    for i in range(1, 51):
#        if is_prime(i):
#            print(i, "is a prime number")
a, b = 0, 1
for _ in range(10):
       print(a)
       a , b=  b , a  + b


