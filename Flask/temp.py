from collections import Counter


_str="zsdfxggcf"
m = Counter(_str)
print(m)


_map = {'a':2 , 'b':3 , 'c':5}

# if 'aa' in _map:
#     print("yes present")
# else:
#     print("lol")

for k,v in _map.items():
    print(k,v)
