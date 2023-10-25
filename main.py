
# daniela villagomez

# display menu and options
def display_menu():
    print('Menu\n-------------')
    print('1. Encode\n2. Decode\n3. Quit\n')

# encode function with user-inputted password as parameter
def encode(password):
    # empty string for encoded password
    encoded_pw = ''
    # iterate through string characters to replace values with encoded version
    for char in password:
        # convert character to int in order to compare value to any int value <= 6
        if int(char) <= 6:
            char = int(char) + 3
        elif char == '7':
            char = '0'
        elif char == '8':
            char = '1'
        elif char == '9':
            char = '2'
        # convert char to string to concatenate to encoded_pw string
        encoded_pw += str(char)
    return encoded_pw

# decode function with user-inputted password as parameter
def decode(password):
    pass

def main():
    # loop program while user chooses to continue
    while True:
        display_menu()
        user_option = int(input('Please enter an option: '))
        user_pw = ''

        # user chooses to encode password
        if user_option == 1:
            user_pw = input('Please enter your password to encode: ')
            encoded_pw = encode(user_pw)
            print('Your password has been encoded and stored!\n')
        # user chooses to decode password
        elif user_option == 2:
            decoded_pw = decode(user_pw)
            print(f'The encoded password is {encoded_pw}, and the original password is {decoded_pw}.\n')
        # user chooses to quit program, break loop
        elif user_option == 3:
            break
        # user inputs invalid selection during menu prompt
        else:
            print('Invalid selection.\n')
            display_menu()
            user_option = int(input('Please enter an option: '))
if __name__ == '__main__':
    main()
