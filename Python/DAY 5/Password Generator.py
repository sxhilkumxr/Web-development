letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers=["0","1","2","3","4","5","6","7","8","9"]
symbols=['!','@','#','$','*','&']

import random

print("Welcome to Password Generator!")
n_letters=int(input("How many number of letters you like in password\n"))
n_numbers=int(input(f"How many number you like in  password\n"))
n_symbols=int(input(f"how many symbols you like in  password\n"))

password=[]
for char in range(0,n_letters):
     password.append (random.choice(letters))
for char in range(0,n_numbers):
     password.append (random.choice(numbers))
for char in range(0,n_symbols):
     password.append (random.choice(symbols))
b=""
for a in password :
     b+=a
print(b)
