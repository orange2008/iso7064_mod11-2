import json
import sys

# MOD 11-2 Validation system.

def getid():
    id = input("Enter your ID: ")
    if len(id) != 18:
        print("Illegal ID!")
        return None
    return id


id = getid()
if id == None:
    sys.exit(0)

# Start Calculation
with open("data.json") as fp:
    wi = json.load(fp)

s = 0

for i in range(0,17):
    s += int(id[i]) * int(wi[i])

res = (12-(s%11))%11
print("The correct validate number is: " + str(res))
print("Requested number is: " + str(id[-1]))
if res == 10:
    res = "X"

if str(id[17]) != str(res):
    print("The ID is fake.")
else:
    print("The ID is legal!")