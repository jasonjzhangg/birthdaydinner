
while True:
    try:
        person1 = int(input("Please input Person 1's total before tax and tip in dollars.\n"))
        break
# if valid input, then break out of the loop
    except ValueError:
        print("That is not a valid number.")
        #if invalid, re-loop back to original question

while True:
    try:
        person2 = int(input("Please input Person 2's total before tax and tip.\n"))
        break
    except ValueError:
        print("That is not a valid number.")

while True:
    try:
        person3 = int(input("Please input Person 3's total before tax and tip.\n"))
        break
    except ValueError:
        print("That is not a valid number.")

while True:
    try:
        person4 = int(input("Please input Person 4's total before tax and tip.\n"))
        break
    except ValueError:
        print("That is not a valid number.")

while True:
    try:
        person5 = int(input("Please input Person 5's total before tax and tip.\n"))
        break
    except ValueError:
        print("That is not a valid number.")

while True:
    try:
        person6 = int(input("Please input Person 6's total before tax and tip.\n"))
        break
    except ValueError:
        print("That is not a valid number.")

while True:
    try:
        person7 = int(input("Please input Person 7's total before tax and tip.\n"))
        break
    except ValueError:
        print("That is not a valid number.")

while True:
    try:
        person8 = int(input("Please input Person 8's total before tax and tip.\n"))
        break
    except ValueError:
        print("That is not a valid number.")



def bill(person):
    tip_total = person*1.15
    #Tip is 15%; therefore multiply by 1 + 0.15
    tax_tip_total = tip_total*1.05
    #Tax is 5%; therefore multiply by 1 + 0.05
    return round(tax_tip_total, 2)
    #return back from function: the final total rounded with 2 decimal digits

print(f"Person 1's final bill is: ${(bill(person1))}")

print(f"Person 2's final bill is: ${(bill(person2))}")

print(f"Person 3's final bill is: ${(bill(person3))}")

print(f"Person 4's final bill is: ${(bill(person4))}")

print(f"Person 5's final bill is: ${(bill(person5))}")

print(f"Person 6's final bill is: ${(bill(person6))}")

print(f"Person 7's final bill is: ${(bill(person7))}")

print(f"Person 8's final bill is: ${(bill(person8))}")
#print final bills