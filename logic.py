import secrets
import time 

num_one = secrets.choice(range(1,9))
num_two = secrets.choice(range(1,9))
num_three = secrets.choice(range(1,9))

list = [num_one, num_two, num_three]
newstr = ""

for i in list:
    string = str(i)
    newstr += string
    print(f'\r{newstr}', end='', flush=True)
    time.sleep(1)

print()