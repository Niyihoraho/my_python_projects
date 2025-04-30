alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt_and_decrypt(shift_amount, message_text, direction):
    cipher_text = ""
    for letter in message_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            if direction == 'encode':
                new_position = (position + shift_amount) % 26
            elif direction == 'decode':
                new_position = (position - shift_amount) % 26
            cipher_text += alphabet[new_position]
        else:
            cipher_text += letter  # keep spaces/punctuation unchanged
    return cipher_text

result = encrypt_and_decrypt(shift, text, direction)
print(f"Result: {result}")
