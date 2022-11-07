fruits = ['Apple', 'Banana', 'Pear']


def make_pie(index):
    try:
        fruit = fruits[index]
        print(fruit+"Pie")
    except IndexError:
        print("Fruit Pie")


make_pie(4)
