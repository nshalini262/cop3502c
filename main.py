def main():
    # This function takes each value in the password and converts it to an integer and then adds 3 to it.
    # Then all the integer values are added to a string. The string is then returned.
    def encode(password):
        string = ""
        for i in password:
            i = 3 + int(i)
            string = string + str(i)
        return string


if __name__ == '__main__':
    main()
