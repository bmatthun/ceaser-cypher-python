alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
new_alphabet = []

direction = input("Type 'encode' to encrypt, \
type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(original_text, shift_amount):
    shifted_alphabet = []
    encrypted_word = ""

    for number in range(len(alphabet)):
        # shift_amount = 2 then [y, z, a, b, c,..., w, x]
        if shift_amount > number:
            shifted_alphabet.append(alphabet[0 + number - shift_amount])
        else:
            shifted_alphabet.append(alphabet[number - shift_amount])

    for letter in original_text:
        index = shifted_alphabet.index(letter)
        print(index)
        encrypted_word += alphabet[index]

    print(encrypted_word)


def encode(encrypted_text, shift_amount):
    shifted_alphabet = []
    for number in range(len(alphabet)):
        # shift_amount = 2 then [y, z, a, b, c,..., w, x]
        if shift_amount > number:
            shifted_alphabet.append(alphabet[0 + number - shift_amount])
        else:
            shifted_alphabet.append(alphabet[number - shift_amount])