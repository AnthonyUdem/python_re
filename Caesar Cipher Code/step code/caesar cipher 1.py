#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
#TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the
#  shift amount and print the encrypted text.
#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code
#  and encrypt a message.
def caesar_cipher1():
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i','j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
    text_val = input("Type your message: ").lower()
    shift_val = int(input("Type the shift number: "))

    # encrypt function expects the text and shift number, encrypt it, then displays the encrypted message
    def encrypt(text, shift):
        """Expects the text and shift number, encrypt it, then displays the encrypted message"""

        cipher_text = ""
        for char in text:
            if char in alphabet:
                position = int(alphabet.index(char) + shift)
                cipher_text += alphabet[position]
        print(f"The encoded text is: {cipher_text}")

    if direction == 'encode':
        encrypt(text=text_val, shift=shift_val)


caesar_cipher1()