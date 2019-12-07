#! python3
# asr_counter counts number of done asr-s in ditto.av

import os
# import shelve
# import keyboard

def score():
    asr = open('asr.txt', 'r')
    asr_score = asr.read()
    asr.close()
    division = list(asr_score).count('d')
    codes = list(asr_score).count('c')
    print('Division: ' + str(division))
    print('Codes: ' + str(codes))
    print('Points: ' + str(division + codes / 2))

def delete_last():
    asr = open('asr.txt', 'r')
    asr_score = asr.read()
    asr.close()
    asr_score = list(asr_score)
    asr_score.pop()
    asr = open('asr.txt', 'w')
    asr.write(''.join(asr_score))
    asr.close()
    print('Last step deleted')

def counting():
    print('"d" for division\n"c" for codes\n"r" to reverse last step\n"e" to end\n')
    while True:
        asr_type = input().lower()
        if asr_type == 'e':
            break
        if asr_type == 'r':
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

if not os.path.exists(os.getcwd() + '\\asr.txt'):
    asr = open('asr.txt', 'w')
    asr.close()

while True:
    action = input()
    if action.lower() in ['count', 'reset']:
        break

if action.lower() == 'count':
    counting()

if action.lower() == 'reset':
    asr = open('asr.txt', 'w')
    asr.write('')
    asr.close()
    print('Reset done')


input('\nPress enter to exit')

# TODO change normal open to shelve

# TODO:
'''https://stackoverflow.com/questions/48915822/
creating-a-hotkey-to-enter-text-using-python-running-in-background-waiting-for'''