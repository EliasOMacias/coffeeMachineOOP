from menu import Menu, MenuItem
from coffe_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()







print(menu.get_items())


is_on = True
while is_on:
    options = menu.get_items()
    invalid_choice = True
    while invalid_choice:
        choice = input(f'What would you like ({options})\n')
        if choice.lower() not in ['latte', 'cappuccino', 'espresso', 'report', 'off']:
            print('sorry, try again')
        else:
            invalid_choice = False
    if choice.lower() == 'report':
        coffee_maker.report()
        money_machine.report()
    elif choice.lower() == 'off':
        is_on = False
    else:
        drink = menu.find_drink(choice)

        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)

