alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
new_alphabet = []

direction = input("Type 'encode' to encrypt, \
type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#def ceaser(original_text, shift_amount, decode_or_encode):

def encrypt(original_text, shift_amount):
    encrypted_word = ""
    for letter in original_text:
        index = alphabet.index(letter)
        shifted_index = index + shift_amount
        if shifted_index >= len(alphabet):
            encrypted_word += alphabet[shifted_index - len(alphabet)]
        else:
            encrypted_word += alphabet[shifted_index]
    print(encrypted_word)

def decrypt(original_text, shift_amount):
    decrypted_text = ""
    for letter in original_text:
        index = alphabet.index(letter)
        decrypted_text += alphabet[index - shift_amount]
    print(decrypted_text)

def ceaser(decrypt_or_encrypt, original_text, shift_amount):
    if decrypt_or_encrypt == "encode":
        encrypt(original_text, shift_amount)
    elif decrypt_or_encrypt == "decode":
        decrypt(original_text, shift_amount)
    else:
        print("Wrong input!")

ceaser(direction, text, shift)