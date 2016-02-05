hashTable = []
m = 100


def init():
    for i in range(m):
        hashTable.append(dict())


def search(key):
    hkey = h(key)
    bucket = hashTable[hkey]
    if key in bucket:
        return bucket[key]
    else:
        return -1


def delete(key):
    hkey = h(key)
    bucket = hashTable[hkey]
    if key in bucket:
        del bucket[key]
        return True
    else:
        return False


def insert(key, value):
    for i in range(m):
        j = h(key)
        hashTable[j][key] = value
        return key


def h(key):
    a = 1233
    b = 153
    c = key
    if type(c) == type('str'):
        c = stringToAsccii(c)
    return round((a * c + b) % m, 0)


def stringToAsccii(s):
    sum = 0
    for i in [ord(c) for c in s]:
        sum += i
    return sum

init()
insert('hi', 12)
insert('his', 15)

print(search('hi'))
print(delete('hi'))
print(search('hi'))
