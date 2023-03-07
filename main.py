def main():

    def encode(password):
        string = ""
        for i in password:
            i = 3 + int(i)
            string = string + str(i)
        print(string)


if __name__ == '__main__':
    main()
