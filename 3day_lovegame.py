name1=input("YOUR BOYFRIEND NAME: ")
name2=input("YOUR GIRLFRIEND NAME: ")
combine_name=name1+name2
lower_name=combine_name.lower()
T = lower_name.count("t")
R = lower_name.count("r")
U = lower_name.count("u")
E = lower_name.count("e")
first=T+R+U+E

L = lower_name.count("l")
O = lower_name.count("o")
V = lower_name.count("v")
E = lower_name.count("e")

second = L+O+V+E
score = int(str(first)+str(second))

if score >= 60:
    print(f"True Love: {score} "+name1+" "+name2 )
elif score >=40 and score <60:
    print(f"Not Goo: {score} "+name1+" "+name2 )
else:
    print(f"OOPS! no loveeee: {score} "+name1+" "+name2 )




