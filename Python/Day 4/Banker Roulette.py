import random

#my code
pay=random.randint(1,6)
friends = ["AMARJIT","SAHIL","AJIT","BINA PAISA DIYE BHAGO","SONU","SUMAN"]
if pay==1:
    print(friends[0], "will pay the bill")
elif pay==2:
    print(friends[1], "will pay the bill")
elif pay==3:
    print(friends[2], "will pay the bill")
elif pay==4:
    print(friends[3], "will pay the bill")
elif pay==5:
    print(friends[4], "will pay the bill")
elif pay==6:
    print(friends[5], "will pay the bill")

#answer1
print(random.choices(friends))

#anser2
payer=random.randint(0,5)
print(friends[payer])

# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
# dirty_dozen = [fruits, vegetables]
 
# print(dirty_dozen[1][1])