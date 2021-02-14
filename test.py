def dict_compare(d1, d2):
    d1_keys = set(d1.keys())
    d2_keys = set(d2.keys())
    shared_keys = d1_keys.intersection(d2_keys)
    added = d1_keys - d2_keys
    removed = d2_keys - d1_keys
    modified = {o : (d1[o], d2[o]) for o in shared_keys if d1[o] != d2[o]}
    same = set(o for o in shared_keys if d1[o] == d2[o])
    return added, removed, modified, same

x = {'room1': False, 'room2': False, 'room3': False}
y = {'room1': True, 'room2': False, 'room3': True}
added, removed, modified, same = dict_compare(x, y)
print(modified)

for key in modified:
    print(modified[key])