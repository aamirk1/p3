

def bim(height,weight):
    return round((weight / height**2),2)

h = float(input("Enter Your Height in Meter: "))
w = float(input("Enter Your Weight in Kg: "))
print()
print("Welcome To The BMI Calculator")

bmi1 = bim(h, w)
print("Your BMI is: ",bmi1)
if bmi1 <= 18.5:
    print("You Are Underweight.")
elif 18.5 < bmi1 <= 24.9:
    print("Your Weight is Normal.")
elif 25 < bmi1 <= 29.29:
    print("You Are Overweight.")
else:
    print("You Are Obse")