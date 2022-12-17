# Isaiah Marshall | Everything Completed | It just works.. ..as long as you have a .txt file for the list reversal func.

# The first function, calc_inflation, will be using its three parameters to calculate basic interest for data the user
# specifies from the While loop portion at the bottom of the program.
def calc_inflation(initial_bal, interest_rate, years_to_go):
    # The following three lines are our Base Case.
    if years_to_go == 0:
        print(f"Your new balance will be ${initial_bal}.")
        return initial_bal
    # The following two lines are our Recursive Case.
    interest = initial_bal * (1 + interest_rate)
    return calc_inflation(interest, interest_rate, years_to_go - 1)


# Two seperate functions used in order to reverse a .txt list. The first portion will isolate the data the
# user specified in the While loop and save it as a list.
def load_data(txt_file):
    file = open(txt_file, 'r')
    all_lines = file.readlines()
    object_list = []
    for line in all_lines:
        object_list.append(line)
    reversed_list = list_reversal(object_list)
    # After returning from list_reversal, we need to print the newly reversed list to the user.
    print(reversed_list)
    return reversed_list


# Now we will use a recursion function to properly reverse this list.
def list_reversal(normal_list):
    # Base Case
    if len(normal_list) == 0:
        return []
    # Recursive Case
    return [normal_list[-1]] + list_reversal(normal_list[:-1])


# The right-hand triangle function is next.
def create_triangle(size):
    # Base Case
    if size <= 0:
        return size
    # Recursive Case
    print("#" * size)
    return create_triangle(size - 1)


# A While loop is used here to ensure that the user is always brought back to this central command line menu until
# option 4 is selected.
while True:
    print("=========== Please Select An Option Below ===========")
    print("[1] Calculate Basic Compounding Interest")
    print("[2] Reverse The Order of a .txt List")
    print("[3] Create a Right Triangle")
    print("[4] Quit the program")
    print("=====================================================")
    answer = input("Enter choice 1-4:")
    if answer == '1':
        user_bal = float(input("What is your current balance? "))
        user_rate = float(input("What is your interest rate (please convert precentage to decimal)? "))
        user_years = int(input("How many years to go? "))
        answer = calc_inflation(user_bal, user_rate, user_years)
    elif answer == '2':
        user_file = input("What is the name of your text file (please include the .txt extension)? ")
        answer = load_data(user_file)
    elif answer == '3':
        user_triangle_size = int(input("How large would you like the right triangle to be? "))
        answer = create_triangle(user_triangle_size)
    elif answer == '4':
        exit(0)
    else:
        print("Sorry, invalid entry. Please enter 1-4")
