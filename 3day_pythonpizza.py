print("thank you for choosing python pizza")
size=str(input("what size of Pizza do you want? S, M, OR L: "))

if size =="S":
    pepperoni=str(input("you need to add pepperoni Y or N: "))
    price=int(15)
    if pepperoni == "Y":
        price=price+2
        print(f"bill: {price}")
    else:
       print(f"bill: {price}") 
elif size =="M":
    pepperoni=str(input("you need to add pepperoni Y or N: "))
    price=int(20)
    if pepperoni =="Y":
        price=price+3
        print(f"bill: {price}")
    else:
        print(f"bill: {price}")
else:
    pepperoni=str(input("you need to add pepperoni Y or N: "))
    price=int(35)
    if pepperoni =="Y":
        price=price+3
        print(f"bill: {price}")
    else:
        print(f"bill: {price}")
cheese=str(input("do you want extra cheese: Y or N: "))
if cheese== "Y":
    price=price+1
    print(f"total bill: {price}")
else:
    print(f"total bill: {price}")




