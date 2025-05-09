from clear import clear
from prettytable import PrettyTable
clear()
table=PrettyTable()
table.add_column("Pokemon Name",["pikachu","squirtle","charmande"])
table.add_column("type",["fire","water","Electic"])
table.align='r'
print(table)
