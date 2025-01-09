import math

def count_perfect_square(n,arr):
    count = 0
    for i in range(n):
        x = int(math.sqrt(arr[i]))
        if x * x == arr[i]:
            count += 1
        else:
            continue
    print(count)

n = int(input())
arr = list(map(int,input().split(" ")))
count_perfect_square(n,arr)

#input: 25 77 54 81 48
#output: 2