k = 4
hashTable = dict()
bucket = []

def init():
    for i in range(k):
        bucket[i] = None


def get(key):
    return hashTable[h(key)]


def delete(key):
    hkey = h(key)
    if hashTable[hkey] is not None:
        del hashTable[hkey]
        return 'valor borrado de llave ' + hkey
    else:
        return 'La llave ' + hkey + ' no tiene valor que borrar'


def insert(key, value):
    for i in range(k):
        j = h(key, i)
        if hashTable[j] is not None:
            hashTable[j] = value
            return key


def h(key):
    a = 3
    if len(arg) > 1:
        return (a*key % len(hashTable)) % k
    else:
        return key


print(h(5, 2))
