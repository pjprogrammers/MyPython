import random
from lists import list_01
def get_valid_number(list_01):
    number = random.choice(list_01) #randomly choose a number from this list.
    while '_' in number or ' ' in number:
        word = random.choice(list_01)

    return number

def guess():
    number = get_valid_number(list_01)
    guessed_number = set(number) #already guessed numbers
    