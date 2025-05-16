
print(''' _____                                                                                                                                    _____ 
( ___ )                                                                                                                                  ( ___ )
 |   |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|   | 
 |   |     ███        ▄████████  ▄███████▄   ▄██████▄     ▄████████                   ▄███████▄  ▄█   ▄███████▄   ▄███████▄     ▄████████ |   | 
 |   | ▀█████████▄   ███    ███ ██▀     ▄██ ███    ███   ███    ███                  ███    ███ ███  ██▀     ▄██ ██▀     ▄██   ███    ███ |   | 
 |   |    ▀███▀▀██   ███    █▀        ▄███▀ ███    ███   ███    ███                  ███    ███ ███▌       ▄███▀       ▄███▀   ███    ███ |   | 
 |   |     ███   ▀  ▄███▄▄▄      ▀█▀▄███▀▄▄ ███    ███  ▄███▄▄▄▄██▀                  ███    ███ ███▌  ▀█▀▄███▀▄▄  ▀█▀▄███▀▄▄   ███    ███ |   | 
 |   |     ███     ▀▀███▀▀▀       ▄███▀   ▀ ███    ███ ▀▀███▀▀▀▀▀                  ▀█████████▀  ███▌   ▄███▀   ▀   ▄███▀   ▀ ▀███████████ |   | 
 |   |     ███       ███    █▄  ▄███▀       ███    ███ ▀███████████                  ███        ███  ▄███▀       ▄███▀         ███    ███ |   | 
 |   |     ███       ███    ███ ███▄     ▄█ ███    ███   ███    ███                  ███        ███  ███▄     ▄█ ███▄     ▄█   ███    ███ |   | 
 |   |    ▄████▀     ██████████  ▀████████▀  ▀██████▀    ███    ███                 ▄████▀      █▀    ▀████████▀  ▀████████▀   ███    █▀  |   | 
 |   |                                                   ███    ███                                                                       |   | 
 |___|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|___| 
(_____)                                                                                                                                  (_____)''')

print()
print()



print("welcome to Tezor pizza deliveries!")
size= input('what size pizza do you want?s S, M or L: ')
pepporoni = input("do you want pepporoni on your pizza? Y or N: ")
extra_cheese = input("do you want extra cheese? Y or N: ")
bill=0
if size=="S":
    if pepporoni=="Y":
        if extra_cheese=="Y":
            print("your bill is $18")
        if extra_cheese=="N":
            print("your bill is $17")
    if pepporoni=="N":
        if extra_cheese=="N":
            print("your bill is $15")
        if extra_cheese=="Y":
            print("your bill is $16")
elif size=="M":
    if pepporoni=="N":
        if extra_cheese=="N":
            print("your bill is $20")
        if extra_cheese=="Y":
            print("your bill is $21")
    if pepporoni=="Y":
        if extra_cheese=="Y":
            print("your bill is $24")
        if extra_cheese=="N":
            print("your bill is $23")
elif size=="L":
    if pepporoni=="N":
        if extra_cheese=="N":
            print("your bill is $25")
        if extra_cheese=="Y":
            print("your bill is $26")
    if pepporoni=="Y":
        if extra_cheese=="N":
            print("your bill is $28")
        if extra_cheese=="Y":
            print("your bill is $29")
else:
    print("wrong input")
