alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(shift_amount, message_text):
    cipher_text = ""
    for letter in message_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = (position + shift_amount) % 26
            cipher_text += alphabet[new_position]
        else:
            cipher_text += letter
    return cipher_text

def decrypt(shift, encoded_text):
    decipher_text = ""
    for letter in encoded_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = (position - shift) % 26
            decipher_text += alphabet[new_position]
        else:
            decipher_text += letter
    return decipher_text

run = True
while run:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

    if direction == 'encode' or direction == 'decode':
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))

        if direction == 'encode':
            result = encrypt(shift, text)
            print(f"Encoded text: {result}")
        else:
            result = decrypt(shift, text)
            print(f"Decoded text: {result}")
    else:
        print("Invalid option")

    again = input("Do you want to run the program again? (yes/no): ").lower()
    if again != "yes":
        run = False
        print("Goodbye!")
