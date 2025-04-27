import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("what do you choose? type 0 for Rock, 1 for paper or 2 for Scissors")
choose=int(input("your turn: "))
computer = random.randint(0,2)
game_image=[rock,paper,scissors]
typ=game_image[computer]
typec=game_image[choose]


# if computer==0:
#     typ=rock
# elif computer==1:
#     typ=paper
# elif computer== 2:
#     typ=scissors
# else: 
#     print("inavlid input")

# if choose==0:
#     typec=rock
# elif choose==1:
#     typec=paper
# elif choose== 2:
#     typec=scissors
# else: 
#     print("inavlid input")
     
if choose==0 and computer==2:
    print(f"your choice:\n{typec}")
    print(f"computer choose:\n{typ}")
    print("you win")
elif choose==2 and computer==1:
    print(f"your choice:\n{typec}")
    print(f"computer choose:\n{typ}")
    print("you win")
elif choose==1 and computer==0:
    print(f"your choice:\n{typec}")
    print(f"computer choose:\n{typ}")
    print("you win")
elif choose==computer:
    print(f"your choice:\n{typec}")
    print(f"computer choose:\n{typ}")
    print("Draw")
else:
    print(f"your choice:\n{typec}")
    print(f"computer choose:\n{typ}")
    print("Lost")

  