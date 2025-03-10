from itertools import product

def cartesian_product(arr1, arr2):
    lst_product = list(product(arr1, arr2))
    return " ".join(map(str, lst_product))
    
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

result = cartesian_product(arr1, arr2)
print(result)
