#getUser.py

import getpass
import time

while True:
    print("Attempting to print username:", flush=True)
    print(getpass.getuser())
    time.sleep(5)

 
