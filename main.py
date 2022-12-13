def calc_inflation(initial_bal, interest_rate, years_to_go):
    if years_to_go == 0:
        return initial_bal
    interest = initial_bal * interest_rate
    return calc_inflation(initial_bal * interest, interest_rate, years_to_go - 1)


def create_triangle():
    triangle_size = input("How big should the triangle be?")

