# coin operated
# penny = .01, Dime =.10, Nickel = .05, Quarter = .25
from coffee_data import MENU, resources

money_report = 0
is_order = False

def report():
    global money_report
    print(f"Water:{resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${money_report}")

def ordering(Menu,resource):
    global order_input,money_report
    if resource['water'] < Menu['ingredients']['water'] or resource['coffee'] < Menu['ingredients']['coffee']:
            print(f'Not enough resource')
            return

    quarters = float(input('How many quaters?:$ ')) * .25
    nickels = float(input('How many nickels?:$ ')) * .05
    dimes = float(input('How many dimes?:$ ')) * .10
    pennys = float(input('How many pennys?:$ ')) * .01
    total =  round(quarters + nickels + dimes + pennys, 2)

    if total > Menu['cost']:
        change = total - Menu['cost']
        money_report += Menu['cost']
        print(f'Here is ${change} in change')
    else:
        print(f'Not enough $!')
        return

    if order_input == 'espresso':
        water = resource['water'] - Menu['ingredients']['water']
        coffee = resource['coffee'] - Menu['ingredients']['coffee']
        resource['water'] = water
        resource['coffee'] = coffee
        print(f'Here is your espresso ☕')
    else:
        water = resource['water'] - Menu['ingredients']['water']
        coffee = resource['coffee'] - Menu['ingredients']['coffee']
        milk = resource['milk'] - Menu['ingredients']['milk']
        resource['water'] = water
        resource['coffee'] = coffee
        resource['coffee'] = milk
        print(f'Here is your {order_input} ☕')

if __name__ == "__main__":
    is_order = True
    while is_order:
        order_input = input("what would you like? (espresso/latte/cappuccino): ")
        if order_input == 'report':
            report()
        else:
            if order_input == 'espresso':
                print('Ordering espresso')
                ordering(Menu=MENU['espresso'],resource=resources)
            if order_input == 'latte':
                print('Ordering latte')
                ordering(Menu=MENU['latte'],resource=resources)
            if order_input == 'cappuccino':
                print('Ordering cappuccino')
                ordering(Menu=MENU['cappuccino'],resource=resources)
            if order_input == 'no':
                is_order = False
        