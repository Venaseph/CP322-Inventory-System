#!/usr/bin/env python
import sys
import re

# Init dictionaries
desc = {'0001': 'Wireless Mouse', '0002': 'Wireless Keyboard', '0003': '19" Monitor', '0004': '23" Monitor', '0005'
        : 'HDMI Cable', '0006': 'VGA Cable', '0007': 'USB Cable', '0008': 'Power Cable', '0009': '8GB Thumb Drive',
         '0010': '16GB Thumb Drive'}
parts = {'0001': 3, '0002': 3, '0003': 2, '0004': 2, '0005': 5, '0006': 5, '0007': 10, '0008': 5, '0009': 3, '0010': 4}


def main():
    # do/while control
    run = True

    while run:
        # print menu to screen and gather user selection
        selection = menu()

        # dictswitch for user selection control
        run = defswitcher(selection, run)

    return 0


def menu():
    # user input control-loop
    selection = None
    while selection is None:
        print(
            '''P:  Print all inventory
A:  Add a new part
L:  Lookup part by number
R:  List parts that are low on inventory
Z:  Archive a part
Q:  Exit/Quit '''
        )

        choose = input("Enter choice from menu above:   ")

        # Check validity of user selection, rerun if invalid
        if re.fullmatch('[P|A|L|R|Z|Q]', choose):
            selection = choose
            return selection
        else:
            print('\nPlease select a valid option')


def defswitcher(selection, run):
    switcher = {
        'P': printall,
        'A': addpart,
        'L': lookup,
        'R': lowinv,
        'Z': archive,
    }
    # exit control
    if selection is 'Q':
        run = False
    else:
        # get function name
        process = switcher.get(selection)
        # execute correct function
        process()
    return run


def printall():
    print("  Part Number".ljust(20) + "# In Stock ".ljust(20) + "Part Description")
    # iterate though and print
    for key, value in desc.items():
        print("  " + key.ljust(18) + str(parts.get(key)).ljust(20) + value)
    print()


def addpart():

    # user input control-loop
    add = []
    while not add:
        # grab user input and split on comma
        addinput = input("\nEnter inventory and description comma delimited:   ")

        # Check validity of user selection, rerun if invalid
        if re.fullmatch('([\d])+[,]\S+([\w\s])+', addinput):
            add = addinput.split(',')
            partnum = newpartnum()
            updatedictionaries(partnum, add)
        else:
            print("\nPlease follow proper formatting")


def newpartnum():
    # sort and grab highest key value, look for cleaner way to do this
    lastknown = sorted(desc.keys())[-1]
    partnum = int(lastknown)
    partnum += 1

    return str(partnum).zfill(4)


def updatedictionaries(partnum, update):
    # passing global to defs to avoid creating a new box for Schrödinger each run though
    global parts, descr

    parts.update({partnum: update[0]})
    desc.update({partnum: update[1]})


def lookup():
    # user input control-loop
    partnum = None
    while not partnum:
        partnum = input("Enter part number:   ")

        if re.fullmatch('\d{4}', partnum):
            print("  Part Number".ljust(20) + "# In Stock ".ljust(20) + "Part Description")
            print("  " + partnum.ljust(18) + str(parts.get(partnum)).ljust(20) + desc.get(partnum) + "\n")
        else:
            print(partnum + " does not exist, try again")
    changeinv()


def changeinv():
    change = input(
        '''A:  Add to inventory
S:  Subtract from inventory
Q:  Return to main menu 
Enter Choice from above menu:   '''
    )
    # will feed into updatedic()


def lowinv():
    print("lowinv")


def archive():
    print("archive")


if __name__ == "__main__":
    sys.exit(main())
