year = int(input("Enter a Year: "))
if (year % 400 == 0) and (year % 100 == 0):
    print(year, "It is a Leap Year")

elif (year % 4 == 0) and (year % 100 != 0):
    print(year, "It is a Leap Year")
else:
    print(year, "It is Not a Leap Year")
