
# daniela villagomez

def display_menu():
    print('Menu\n-------------')
    print('1. Encode\n2. Decode\n3. Quit\n')

def encode(password):
    pass

def decode(password):
    pass

def main():
    while True:
        display_menu()
        user_option = int(input('Please enter an option: '))
        user_pw = ''

        if user_option == 1:
            user_pw = input('Please enter your password to encode: ')
            encoded_pw = encode(user_pw)
            print('Your password has been encoded and stored!\n')
        elif user_option == 2:
            decoded_pw = decode(user_pw)
            print(f'The encoded password is {encoded_pw}, and the original password is {original_pw}.\n')
        elif user_option == 3:
            break
        original_pw = user_pw

if __name__ == '__main__':
    main()
