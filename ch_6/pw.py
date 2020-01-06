#! python3
#
# A horrible insecure password thing.

import pyperclip
import sys
from time import sleep

PASSWORDS = {'email': 'Password123',
             'bank': 'Password321',
             'aws': '123Password',
             'wifi': '=*qZJyz8?Gje2K(cn}x3#nonUY=YQNd@-,3]d'}

if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copies account password to clipboard')
    sys.exit()

account = sys.argv[1]

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard. This clipboard will self-destruct in ten seconds.')
    sleep(10)
    pyperclip.copy("")
else:
    print('That account is not in the database.')
