# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
lowest = 50
highest = 70


def fengshan(tem, lenth):
    siz = int((highest - lowest) / lenth)
    tems = range(lowest, highest, siz)
    i = 0
    while True:
        print(tems[i])
        i += 1
        if i >= lenth:
            break
    pass


fengshan(50, 10)
