# TODO-1: Import and print the logo from art.py when the program starts.
# TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
# Try running the program and entering a shift number of 45.
# Add some code so that the program continues to work even if the user enters a shift number greater than 26.
# Hint: Think about how you can use the modulus (%).
# TODO-3: What happens if the user enters a number/symbol/space?
# Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
# e.g. start_text = "meet me at 3"
# end_text = "•••• •• •• 3"
# TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
# e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
# If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
# Hint: Try creating a while loop that continues to execute the program if the user types 'yes'.


def caesar_cipher():
    from art import logo
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    def caesar(cipher_text, shift_number, cipher_direction):
        caesar_text = ""
        if cipher_direction == 'decode':
            shift_number *= - 1
        for char in cipher_text:
            if char not in alphabet:
                caesar_text += char
            else:
                position = alphabet.index(char) + shift_number
                caesar_text += alphabet[position]
        print(f"The {cipher_direction}d text is 📝: {caesar_text}")

    print(logo)
    print("Welcome to The Lonasctech Caesar Cipher program!")

    again = True
    while again:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt 📝✉️: ")
        if direction != 'encode' and direction != 'decode':
            print("--->Please type 'encode' to encrypt, or type 'decode' to decrypt!\n")
        else:
            text = input("Type your message: ").lower()
            shift = int(input("Type the shift number: "))

            shift %= 26

            caesar(cipher_text=text, shift_number=shift, cipher_direction=direction)
            again = input("\nType 'y' for yes if you want to go again. Otherwise type 'n' for no: ").lower()
            if again == 'n':
                print("Thank you for your time in using our services, Goodbye!")
                again = False


caesar_cipher()
