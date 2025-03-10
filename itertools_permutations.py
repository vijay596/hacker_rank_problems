from itertools import permutations

def possible_permutations(s, n):
    
    return sorted(permutations(s, n))

s, n = input().split()
n = int(n)
result = possible_permutations(s, n)
for i in result:
    print(''.join(i))
