from itertools import combinations

def combinations_test(s, n):
    for i in s:
        print(i)
    return list(combinations(s, n))
    
s, n = input().split()
n = int(n)
result = combinations_test(s, n)
for j in result:
    print(''.join(j))
