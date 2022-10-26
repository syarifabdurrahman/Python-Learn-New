from prettytable import PrettyTable

table = PrettyTable()

# Column by column 
# table.add_column('Pokemon Name',['Pikachu','Squirtle','Charmander','Barbasour'])
# table.add_column('Type',['Electric','Water','Fire','Leaf'])

# Row by row
table.field_names = ['Pokemon Name','Type']
table.add_row(['Pikachu','Electric'])
table.add_row(['Squirtle','Water'])
table.add_row(['Charmander','Fire'])
table.add_row(['Barbasour','Leaf'])
table.align = 'l'

print(table)