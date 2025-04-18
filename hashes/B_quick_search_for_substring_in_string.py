import sys

def find_hashes(s, p):
    n = len(s)
    hashes_str = [0] * (n + 1)
    for i in range(1, n + 1):
        hashes_str[i] = (hashes_str[i - 1] * p + ord(s[i - 1])) % M
    return hashes_str

def find_hash_substring(hashes, l, r):
    return (hashes[r] - hashes[l] * pow(p, r - l, M)) % M


data = sys.stdin.read().splitlines()
s = data[0]
t = data[1]

M = 10 ** 9 + 7
p = 256

hash_s = find_hashes(s, p)[-1]
hash_t = find_hashes(t, p)
n = len(s)

entrances_number = 0
entrances_indexes = []

for i in range(len(t) - n + 1):
    r = i + n
    hash_substring_t = find_hash_substring(hash_t, i, r)
    if hash_substring_t == hash_s:
        entrances_number += 1
        entrances_indexes.append(i + 1)

print(entrances_number)
print(*entrances_indexes)


