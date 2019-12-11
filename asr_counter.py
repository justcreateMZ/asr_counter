#! python3
# asr_counter counts number of done asr-s in ditto.av (my working environment)

import datetime
import shelve
import os


def score():  # shows current asr score
    asr = shelve.open('asr')
    print('\nDivision: ' + str(asr['d']))
    print('Codes: ' + str(asr['c']))
    print('Points: ' + str(asr['d'] + asr['c'] / 2) + '\n')
    asr.close()


def delete_last():  # deletes last entered thing
    asr = shelve.open('asr')
    asr_history = asr['history']
    if not asr_history == '':
        asr[asr_history[-1]] -= 1
        asr['history'] = asr_history[:-1]
        print('Last step deleted')
    asr.close()


def counting():     # counting asr-s
    score()
    print('"d" for division\n"c" for codes\n"reverse" to reverse last step\n"end" to end\n')
    while True:
        asr_type = input().lower()
        if asr_type == 'end':
            break
        if asr_type == 'reverse':
            delete_last()
        if asr_type in ['d', 'c']:
            asr = shelve.open('asr')
            asr[asr_type] += 1
            asr['history'] += asr_type
            asr.close()
            print(datetime.datetime.now().strftime('%H:%M:%S'))
        score()
    score()


def reset():    # resets score (and used when run for the first time)
    asr = shelve.open('asr')
    asr['d'] = 0
    asr['c'] = 0
    asr['history'] = ''
    asr.close()


# main program
print('Hello! What do you want me to do?')
print('Type "count" to enable count mode')
print('Type "reset" to reset asr counter')

# creates shelf when first run
if not (os.path.exists(os.getcwd() + '\\asr.db') or os.path.exists(os.getcwd() + '\\asr.bak')):
    reset()

while True:     # gets what user wants to do
    action = input().lower()
    if action in ['count', 'reset']:
        break

if action == 'count':
    counting()

if action == 'reset':   # resets score
    reset()
    print('Reset done')

input('\nPress enter to exit')

# TODO: (import keyboard)
'''https://stackoverflow.com/questions/48915822/
creating-a-hotkey-to-enter-text-using-python-running-in-background-waiting-for'''

# TODO compile it

# TODO ditto sniffer
