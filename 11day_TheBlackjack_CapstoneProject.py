import random
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def draw_card():
    return random.randint(1, 10)

def draw_two_cards():
    return [draw_card(), draw_card()]

clear()
endgame=True
while endgame:
    type_1 = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if type_1 == 'y':
        your_cards = draw_two_cards()
        computer_first = draw_card()
        
        print(f"Your cards: {your_cards}")
        print(f"Computer's first card: {computer_first}")
        
        type_2 = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        
        if type_2 == 'n':
            your_final_hand = your_cards
            computer_final_hand = draw_two_cards()
            
            print(f"Your final hand: {your_final_hand} -> Total: {sum(your_final_hand)}")
            print(f"Computer's final hand: {computer_final_hand} -> Total: {sum(computer_final_hand)}")
            
            if sum(your_final_hand) > 21:
                print("Bust!! You went over 21.")
            elif sum(computer_final_hand) > 21 or sum(your_final_hand) > sum(computer_final_hand):
                print("You win!")
            elif sum(your_final_hand) == sum(computer_final_hand):
                print("It's a draw!")
            else:
                print("You lose!")

        elif type_2 == 'y':
            your_cards.append(draw_card())
            computer_second = draw_card()
            computer_total = computer_first + computer_second

            print(f"Your cards: {your_cards} -> Total: {sum(your_cards)}")
            print(f"Computer's cards: [{computer_first}, {computer_second}] -> Total: {computer_total}")
            
            if sum(your_cards) > 21:
                print("Bust!! You went over 21.")
            elif computer_total > 21 or sum(your_cards) > computer_total:
                print("You win!")
            elif sum(your_cards) == computer_total:
                print("It's a draw!")
            else:
                print("You lose!")
        else:
            print("Invalid choice. Please type 'y' or 'n'.")
    else:
        print("Game closed.")
        endgame=False
        
        
    
