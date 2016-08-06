'''
add_to_inventory.py -- takes dictionary with player's inventory and list
with the new items as arguments and returns dictionary with updated inventory.
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

def add_to_inventory(inventory, add_items):
    for item in add_items:
            inventory.setdefault(item, 0)
            inventory[item] += 1
    return inventory

stuff = {'gold coin': 42, 'rope': 1}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

stuff = add_to_inventory(stuff, dragon_loot)
display_inventory(stuff)
