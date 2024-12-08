def err_checker(variable, command, min_val, max_val):
    variable = is_digit_check(variable, command)
    variable = min_val_check(variable, command, min_val)
    variable = max_val_check(variable, command, min_val, max_val)
    variable = float(variable)
    return variable


def is_digit_check(variable, command):
    while not variable.isdigit():
        print('Enter Numbers Only')
        variable = input(command)
    return variable


def min_val_check(variable, command, min_val):
    while float(variable) < min_val:
        print(f"Minimum value is {min_val}")
        variable = input(command)
        variable = is_digit_check(variable, command)
    return variable


def max_val_check(variable, command, min_val, max_val):
    while float(variable) > max_val:
        print(f"Maximum value is {max_val}")
        variable = input(command)
        variable = is_digit_check(variable, command)
        variable = min_val_check(variable, command, min_val)
    return variable
