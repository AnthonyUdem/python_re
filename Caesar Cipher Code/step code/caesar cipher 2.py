# TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
# TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the
#  shift amount and print the decrypted text.
# TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable.
#  Then call the correct function based on that 'direction' variable.
#  You should be able to test the code to encrypt *AND* decrypt a message.

def caesar_cipher2():

    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
    text = input("Type your message: ").lower()
    shift = int(input("Type the shift number: "))

    def encrypt(encrypt_text, encrypt_shift):
        """Expects the text and shift number, encrypt it, then displays the encrypted message"""
        en_cipher_text = ""
        for char in encrypt_text:
            position = int(alphabet.index(char) + encrypt_shift)
            en_cipher_text += alphabet[position]
        print(f"The encoded text is: {en_cipher_text}")

    def decrypt(decrypt_text, decrypt_shift):
        """Expects the text and shift number, decrypt it, then displays the decrypted message"""
        de_cipher_text = ""
        for char in decrypt_text:
            position = int(alphabet.index(char) - decrypt_shift)
            de_cipher_text += alphabet[position]
        print(f"The decoded text is: {de_cipher_text}")

    if direction == 'encode':
        encrypt(encrypt_text=text, encrypt_shift=shift)
    elif direction == 'decode':
        decrypt(decrypt_text=text, decrypt_shift=shift)
    else:
        print("Please enter 'encode' to encrypt or 'decode' to decrypt your message")


caesar_cipher2()
