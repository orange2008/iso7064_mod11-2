import json

# 7 9 10 5 8 4 2 1 6 3 7 9 10 5 8 4 2

wi = [7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]

with open("data.json", 'w') as fp:
    json.dump(wi, fp)