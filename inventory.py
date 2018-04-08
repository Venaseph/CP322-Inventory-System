import sys
import re

# Can't use octals for key values, so strings, init dicts
parts = {'0001': 'Wireless Mouse', '0002': 'Wireless Keyboard', '0003': '19" Monitor', '0004': '23" Monitor', '0005'
         : 'HDMI Cable', '0006': 'VGA Cable', '0007': 'USB Cable', '0008': 'Power Cable', '0009': '8GB Thumb Drive',
         '0010': '16GB Thumb Drive'}
descr = {'0001': 3, '0002': 3, '0003': 2, '0004': 2, '0005': 5, '0006': 5, '0007': 10, '0008': 5, '0009': 3, '0010': 4}


def main():
    # do/while control
    run = True

    while run:
        # print menu to screen and gather user selection
        selection = menu()

        # dictonary switch for user selection control
        run = defswitcher(selection, run)

    return 0


def defswitcher(selection, run):
    switcher = {
        'P': printall,
        'A': addpart,
        'L': lookup,
        'R': lowinv,
        'Z': archive,
    }

    if selection is 'Q':
        run = False
    else:
        # get function name
        process = switcher.get(selection)
        # execute correct function
        process()
    return run


def printall():
    # passing global to defs to avoid creating a new box for Schrödinger each run though
    global parts, descr

    print("  ".join())


def addpart():
    print("addpart")


def lookup():
    print("lookup")


def lowinv():
    print("lowinv")


def archive():
    print("archive")


def menu():
    print(
        '''P:  Print all inventory
A:  Add a new part
L:  Lookup part by number
R:  List parts that are low on inventory
Z:  Archive a part
Q:  Exit/Quit '''
    )
    selection = input("Enter choice from menu above:   ")

    # Check validity of user selection, rerun if invalid
    if re.fullmatch('[P|A|L|R|Z|Q]', selection):
        return selection
    else:
        print('\nYou must Choose a valid option')
        menu()


if __name__ == "__main__":
    sys.exit(main())
