from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_order =  False
the_menu = Menu()
the_coffe_maker = CoffeeMaker()
the_money_machine = MoneyMachine()

def ordering():
    global order_input
    drink = the_menu.find_drink(order_name=order_input)
    if the_coffe_maker.is_resource_sufficient(drink):
        payment = the_money_machine.make_payment(drink.cost)
        if payment:
            the_coffe_maker.make_coffee(drink)

if __name__ == '__main__':
    is_order = True

    while is_order:
        order_input = input(f"what would you like? {the_menu.get_items()}: ")
        if order_input == 'report':
            the_coffe_maker.report()
            the_money_machine.report()
        else:
            if order_input == 'espresso':
                print('Ordering espresso')
                ordering()
            if order_input == 'latte':
                print('Ordering latte')
                ordering()
            if order_input == 'cappuccino':
                print('Ordering cappuccino')
                ordering()
            if order_input == 'no':
                is_order = False