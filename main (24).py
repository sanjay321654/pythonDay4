import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(",")
#length = len(names)
#r_no = random.randint(0,length-1)
#person_to_pay = names[r_no]
#print( person_to_pay + " is going to buy meal today")
person_to_pay = random.choice(names)
print(person_to_pay + " is going to pay today")