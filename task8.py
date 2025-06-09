year=int (input("enter any year that you want"))
if year % 4==0 and year%400==0 and year%100 !=0 :
    print ("This year is leap year")
else:
    print ("No, it is not aleap year ")