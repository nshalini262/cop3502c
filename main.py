
    # This function takes each value in the password and converts it to an integer and then adds 3 to it.
    # Then all the integer values are added to a string. The string is then returned.
def encode(password):
    string = ""
    for i in password:
        i = 3 + int(i)
        string = string + str(i)
    return string

def decode(string): # define function
    decoded = '' # create empty string
    for i in range(8): # iterate
        decoded += str(int(password[i])-3) # subtract 3 from each element in password then convert back to string
    return decoded

def main():

    while True:
        print('Menu\n'
              '-------------\n'
              '1. Encode\n'
              '2. Decode\n'
              '3. Quit\n')
        option = int(input('Please enter an option: '))
        if option == 1:
            password = input('Please enter your password to encode: ')
            encoded_pass = encode(password)
            print('Your password has been encoded and stored!\n')
        elif option == 2:
            decoded = decode(encoded_pass)
            print(f'The encoded password is {encoded_pass}, and the original password is {decoded_pass}.')
        elif option == 3:
            break

if __name__ == '__main__':
    main()

