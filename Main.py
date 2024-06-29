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
    #todo 4a: when the user chooses a drink the program should chick if there are enough resources
    #todo 4b: if not report what is insufficient

#todo 5: process coins
    #todo 5a: if there are sufficient resources, program should prompt user to insert coins.
    #todo 5b: calculate inserted value

#todo 6: check if transaction successful
    #todo 6a: check if funds are sufficient after coin counting operation
    #todo 6b: if successful add money to profit to be reflected in report
    #todo 6c: offer change


prompt = input('what would you like?\n')

if prompt.lower() == 'report':
    coffee_maker.report()
    money_machine.report(r)
elif prompt.lower() == 'off':
    exit()
elif prompt.lower() == 'latte':
    CoffeeMaker().is_resource_sufficient('latte')



