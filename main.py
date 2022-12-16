while True:
    print("===========Please select an option below=======")
    print("[1] Calculate Basic Compounding Interest")
    print("[2] Reverse The Order of a List")
    print("[3] Create a Right Triangle")
    print("[4] Quit the program")
    print("=================================================")
    answer = input("Enter choice 1-4:")
    if answer == '1':
        largest_so_far = country_data[0]
        for country_dict in country_data:
            if country_dict["pop"] > largest_so_far['pop']:
                largest_so_far = country_dict
        print(f"The largest country is {largest_so_far['name']} with pop {largest_so_far['pop']}")
    elif answer == '2':
        smallest_so_far = country_data[0]
        for country_dict in country_data:
            if country_dict['pop'] < smallest_so_far['pop']:
                smallest_so_far = country_dict
        print(f"The smallest country is {smallest_so_far['name']}")
    elif answer == '3':
        country_name = input("Please enter new country name")
        country_pop = int(input(f"please enter population for {country_name}:"))
        pop_change = float(input(f"Please enter the population change 2021-2022"))
        country = {
            'name': country_name,
            'pop': country_pop,
            'change': pop_change
        }
        country_data.append(country)
    elif answer == '4':
        exit(0)
    else:
        print("Sorry, invalid entry. Please enter 1-4")


def calc_inflation(initial_bal, interest_rate, years_to_go):
    if years_to_go == 0:
        return initial_bal
    interest = initial_bal * interest_rate
    return calc_inflation(initial_bal * interest, interest_rate, years_to_go - 1)


def create_triangle(triangle_size):
    triangle_size = input("How big should the triangle be?")
