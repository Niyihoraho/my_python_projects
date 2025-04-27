import random

#Step 1 

word_list = ["aardvark", "baboon", "camel"]
# rand_num = random.randint(0,2)
# word = word_list[rand_num]
word=random.choice(word_list)
print(word)
length=len(word)
display=["_"for _ in range(length)]
print(display)
guess= input(str("enter guessing letter: ")).lower()
for index in range(length):
    if guess == word[index]:
            display[index]=guess
print(display)
