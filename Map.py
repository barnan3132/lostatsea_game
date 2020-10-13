from tabulate import tabulate
from colorama import Fore, Back, Style

# User Input
print(f'Hello survivor! You are lost at sea! What is your name?')
x = input()

print(f'{x}, You are lost at sea, can you find your way home?')

# Providing color
print(Back.BLUE)
print(Fore.BLACK)

sea = (Back.BLUE + 'sea')
structure = ('Island')

# Table map
table = [
    [sea, sea, sea, sea, sea, sea],
    [sea, sea, sea, structure, sea, sea],
    [sea, sea, sea, sea, sea, sea],
    [sea, sea, sea, sea, sea, sea],
    [sea, structure, sea, sea, sea, sea],
    [sea, sea, sea, sea, structure, sea],
]

# Print the table Map
def ocean():
    print(tabulate(table, tablefmt="fancy_grid"))

ocean()

print(Style.RESET_ALL)