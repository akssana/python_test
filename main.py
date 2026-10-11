# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def in_autotests_we_trust(a, b):
    if a == b:
        print('PASS')
    else:
        print('FAIL')

in_autotests_we_trust(10, '10')

in_autotests_we_trust(0, False)
