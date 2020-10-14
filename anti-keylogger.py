import os
import time
import psutil

# "someProgram" in (p.name() for p in psutil.process_iter())
for p in psutil.process_iter():
    print(p.name)

# var = os.system("TASKKILL /F /IM keylogger.exe")

# import ctypes # An included library with Python install.
# ctypes.windll.user32.MessageBoxW(0, "Keylogger has been terminated", "Keylogger", 1)