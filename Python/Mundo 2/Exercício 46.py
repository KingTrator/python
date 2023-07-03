from emoji import emojize
from time import sleep
for i in range(10, 0, -1):
    print('{}{}{}'.format('\033[1m', i, '\033[m'), end=' ')
    sleep(1) if i > 1 else print('\n...')
sleep(1)
print('\033[1;7;40mHAPPY NEW YEAR BITCHES!\033[m', emojize(':party_popper:')*3)
