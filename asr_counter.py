#! python3
# asr_counter counts number of done asr-s in ditto.av (my working environment)

import os


def score():  # shows current asr score
    asr = open('asr.txt', 'r')
    asr_score = asr.read()
    asr.close()
    division = list(asr_score).count('d')
    codes = list(asr_score).count('c')
    print('\nDivision: ' + str(division))
    print('Codes: ' + str(codes))
    print('Points: ' + str(division + codes / 2) + '\n')


def delete_last():  # deletes last entered thing
    asr = open('asr.txt', 'r')
    asr_score = asr.read()
    asr.close()
    asr_score = list(asr_score)
    try:
        asr_score.pop()
    except IndexError:
        print('Score already empty')
        return
    asr = open('asr.txt', 'w')
    asr.write(''.join(asr_score))
    asr.close()
    print('Last step deleted')


def counting():     # counting asr-s
    print('"d" for division\n"c" for codes\n"reverse" to reverse last step\n"end" to end\n')
    score()
    while True:
        asr_type = input().lower()
        if asr_type == 'end':
            break
        if asr_type == 'reverse':
            delete_last()
        if asr_type in ['d', 'c']:
            asr = open('asr.txt', 'a')
            asr.write(asr_type)
            asr.close()
        score()
    score()


print('Hello! What do you want me to do?')
print('Type "count" to enable count mode')
print('Type "reset" to reset asr counter')

if not os.path.exists(os.getcwd() + '\\asr.txt'):   # checks whether .txt exists
    asr = open('asr.txt', 'w')
    asr.close()

while True:     # gets what user wants to do
    action = input()
    if action.lower() in ['count', 'reset']:
        break

if action.lower() == 'count':
    counting()

if action.lower() == 'reset':   # resets score
    asr = open('asr.txt', 'w')
    asr.write('')
    asr.close()
    print('Reset done')

input('\nPress enter to exit')

# TODO change normal open to shelve (import shelve)

# TODO add time of adding asr point

# TODO: (import keyboard)
'''https://stackoverflow.com/questions/48915822/
creating-a-hotkey-to-enter-text-using-python-running-in-background-waiting-for'''

# TODO compile it
