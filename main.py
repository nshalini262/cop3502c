def main():
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


if __name__ == '__main__':
    main()

