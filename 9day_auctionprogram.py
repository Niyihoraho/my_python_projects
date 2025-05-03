import os
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
clear()

auction={}
print("welcome to the secret auction program")

end=True
while end:
    name = input("what is you name: ")
    bid = input("what's your bid?: $")
    auction[name]=bid
    other_bid=input("Are there any other bidders? Type 'yes' 'no'.\n").lower()
    if other_bid !='yes':
        end=False
    clear()
winner=max(auction, key=auction.get)   
winner_value=auction[winner]

print(f"the winner is {winner} with a bid of ${winner_value}")
       
        
    
    
