#Mr Black's ASCII Lesson
def main():
    UPPER_LIMIT = 10
    LOWER_LIMIT = 5
    valid_number = get_number(LOWER_LIMIT,UPPER_LIMIT)

    print("Your valid Number is : ", valid_number)


def get_number(lower, upper):

    print("Please note your Number has to be between ",lower, "and" , upper)
    finished = False
    result = 0
    while not finished:
        try:
            user_number = int(input("Enter a number"))
            finished = True
        except:
            print("Please enter a valid integer.")

    while user_number < lower or user_number > upper:
        print("Invalid Number. Your Number has to be between ", lower, "and", upper)
        user_number = int(input("Please enter a number: "))
    return user_number







main()
