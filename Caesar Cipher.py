def caesar_cipher(text, shift, mode):
    result = ''
    for char in text:
        if char.isalpha():
            if mode == 'encode':
                shifted = ord(char) + shift
            elif mode == 'decode':
                shifted = ord(char) - shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            result += chr(shifted)
        else:
            result += char
    return result

while True:
    from art import logo
    print(logo)

    text = input("Enter the text: ")
    print()
    shift = int(input("Enter the shift value: "))
    print()
    mode = input("Do you want to encode or decode? (encode/decode): ").lower()

    while mode not in ['encode', 'decode']:
        print("Invalid mode. Please enter either 'encode' or 'decode'.")
        mode = input("Do you want to encode or decode? (encode/decode): ").lower()
        print()

    result = caesar_cipher(text, shift, mode)
    print()
    print(f"{mode.capitalize()}d text:", result)
    print()

    restart = input("Do you want to use the Caesar cipher again? (yes/no): ").lower()
    if restart != 'yes':
        print()
        print("Thanks for using the Caesar cipher!")
        break
    else:
        print()
        print("=" * 50)
        print()
        print("Welcome again !")
        print()