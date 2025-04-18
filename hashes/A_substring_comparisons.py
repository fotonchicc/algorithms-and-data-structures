import sys

def find_hashes(s, p):
    n = len(s)
    hashes_str = [0] * (n + 1)
    for i in range(1, n + 1):
        hashes_str[i] = (hashes_str[i - 1] * p + ord(s[i - 1])) % M
    return hashes_str

def find_hash_substring(l, r):
    return (hashes[r] - hashes[l] * pow(p, r - l, M)) % M


data = sys.stdin.read().splitlines()
s = data[0]
m = int(data[1])
requests = [list(map(lambda x: int(x), a.split())) for a in data[2:]]


M = 10 ** 9 + 7
p = 256

hashes = find_hashes(s, p)

for i in requests:
    a, b, c, d = i[0], i[1], i[2], i[3]
    a -= 1
    c -= 1
    if b - a != d - c:
        print("No")
    else:
        hash1 = find_hash_substring(a, b)
        hash2 = find_hash_substring(c, d)
        if hash1 == hash2:
            print("Yes")
        else:
            print("No")
