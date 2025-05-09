import random

word_list = ["aardvark", "baboon", "camel"]
word = random.choice(word_list)

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''


print(logo)
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      | 
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

stages_reverse = stages[::-1]

display = []
word_length = len(word)
for letter in word:
    display += "_"
print(stages[6])
print(f"{' '.join(display)}")

lives = 6

end_of_game = False
while not end_of_game:
    guess = input("Guess the letter: ").lower()
    
    for i in range(word_length):
        if guess == word[i]:
            display[i] = guess
    print(f"{' '.join(display)}")
    
    if "_" not in display:
        end_of_game = True
        print("You win")
        
    if guess not in word:
        lives = lives - 1
        
        if lives == 0:
            end_of_game = True
            print("You lose the game!!")
        
        print(stages[lives]) 