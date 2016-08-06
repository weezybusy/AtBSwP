'''
display_inventory.py -- takes dictionary with any possible `inventory` in it
and displays it like the following:
    Inventory:
    12 arrow
    42 gold coin
    1 rope
    ...
'''

def display_inventory(inventory):
    print('Inventory:')
    print('-' * 10)
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        item_total += v
    print('-' * 10)
    print('Total number of items: ' + str(item_total))


stuff = { 'arrow': 12, 'gold coin': 42, 'rope': 1, 'torch': 6 }

display_inventory(stuff)
