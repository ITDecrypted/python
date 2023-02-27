# keys are strings
# values are prices as integers
# keep everything lowercase for simplicity matching later
menu = {
    'pan con bistec': 7,
    'croqueta': 1,
    'arepa': 9
}

# enter an order
# if dish, print price and running total. Ask again for order.
# if dish but not on menu, scold mildly. Ask again for order.
# if dish is an empty string, stop asking and print total amount
def restaurant():

    total = 0

    # strip outermost characters from ends; default is whitespace
    dish = input('Welcome! What would you like to order?').strip()

    while(True):

        if dish in menu:
            # The assignment operator ':=' is included in Python 3.8+
            dish = input(f'The {dish} is {menu[dish]}, and your total is '
                f'{(total := total + menu[dish])}. Would you like something '
                f'else?').strip()

        # PEP 8 recommends using bools because empty sequences are false
        # This should be checked before the conditional 'dish not in menu'
        # because the empty string is also not in the menu.
        elif not dish:
            print(f'The total due is {total}')
            break

        elif dish not in menu:
            dish = input(f'{dish} is not on the menu. Would you like ' 
                'something else?').strip()
