from utils.decryption import *
from utils.db_operations import *

"""
To fetch the encrypted key from the DB and decrypt them
"""

data = sheet.get_all_records()
key_log = ''
for item in data:
    # print(item)
    if (item['Key']==''):
        continue
    key_log += item['Key']
decrypted_log = decrypt_logs(key_log)
decrypted_log = decrypted_log[::2]
print(decrypted_log)    