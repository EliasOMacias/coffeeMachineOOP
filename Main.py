from menu import Menu, MenuItem
from coffe_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

#todo 1: Prompt user by asking what would you like?
    #todo 1a: check users input
    #todo 2a: prompt should show after each completed action





#todo 4: check resources sufficient
    #todo 4b: if not report what is insufficient

#todo 5: process coins
    #todo 5a: if there are sufficient resources, program should prompt user to insert coins.
    #todo 5b: calculate inserted value

#todo 6: check if transaction successful
    #todo 6a: check if funds are sufficient after coin counting operation
    #todo 6b: if successful add money to profit to be reflected in report
    #todo 6c: offer change




is_on = True
while is_on:
    options = menu.get_items()
    choice = input(f'What would you like ({options})\n')
    if choice.lower() == 'report':
        coffee_maker.report()
        money_machine.report()
    elif choice.lower() == 'off':
        is_on = False
    else:
        drink = menu.find_drink(choice)
        coffee_maker.is_resource_sufficient(drink):
        if


