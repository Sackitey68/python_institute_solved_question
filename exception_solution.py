def read_int(prompt, min, max):
    #
    while True:
        try:
            value = int(input(prompt))
            assert min <= value <= max
            return value

        except AssertionError:
            print("Error: the value is not within permitted range (-10..10)")

        except ValueError:
            print("Error: wrong input")

        else:
            break

    #
v = read_int("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)
