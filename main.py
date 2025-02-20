from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)
direction = input("Type 'encode' to encrypt, "
                  "type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(original_text, shift_amount):
    encrypted_text = ""
    for letter in original_text:
        if letter not in alphabet:
            encrypted_text += letter
        else:
            index = alphabet.index(letter)
            shifted_index = index + shift_amount
            if shifted_index >= len(alphabet):
                encrypted_text += alphabet[shifted_index - len(alphabet)]
            else:
                encrypted_text += alphabet[shifted_index]
    return encrypted_text


def decrypt(original_text, shift_amount):
    decrypted_text = ""
    for letter in original_text:
        if letter not in alphabet:
            decrypted_text += letter
        else:
            index = alphabet.index(letter)
            decrypted_text += alphabet[index - shift_amount]
    return decrypted_text


def ceaser(decrypt_or_encrypt, original_text, shift_amount):
    result = ""
    if decrypt_or_encrypt == "encode":
        result = encrypt(original_text, shift_amount)
        print(f"Your result is: {result}")
    elif decrypt_or_encrypt == "decode":
        result = decrypt(original_text, shift_amount)
        print(f"Your result is: {result}")
    else:
        print("Wrong input!")


start = True

while start:

    ceaser(direction, text, shift)

    user_answer = input("Want to go again? Type 'yes' or 'no': ")
    if user_answer == "no":
        start = False
    elif user_answer == "yes":
        direction = input("Type 'encode' to encrypt, "
                          "type 'decode' to decrypt:\n").lower()
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
    else:
        print("Wrongt input! Try again")
        user_answer = input("Want to go again? Type 'yes' or 'no': ")
