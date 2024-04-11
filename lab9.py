def main():
    while True:
        print('''Menu
-------------
1. Encode
2. Decode
3. Quit''')
        selection = input('Please enter an option: ')
        if selection == '1':
            original_password = input('Please enter your password to encode: ')
            encoded_password = encoder(original_password)
            print("Your password has been encoded and stored!\n")
            continue
        if selection == '2':
            print(f"The encoded password is {encoded_password}, and the original password is {original_password}.")
        if selection == '3':
            exit()

def encoder(password):
    s = ''
    for digit in password:
        encoded_digit = str((int(digit) + 3)%10)
        s += encoded_digit
    return s

def decoder(password):
    decoded = ''
    for digit in password:
        encoded_digit = str((int(digit) - 3)%10)
        decoded += encoded_digit
    return decoded

main()