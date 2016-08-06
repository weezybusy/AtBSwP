'''
table_printer.py -- takes a list of lists of strings and displays it in a
well-organized table with each column right-justified.
'''

table_data = [['apples', 'oranges', 'cherries', 'banana'],
              ['Alice', 'Bob', 'Carol', 'David'],
              ['dogs', 'cats', 'moose', 'goose']]

def print_table(table: list):
    padding = []
    for item in table:
        # Padding = maximum string length in subarray + space.
        padding.append(len(max(item, key=len)) + 1)

    rows = len(table)
    cols = len(table[0])

    for col in range(cols):
        for row in range(rows):
            print(table[row][col].rjust(padding[row]), end='')
        print()

print_table(table_data)
