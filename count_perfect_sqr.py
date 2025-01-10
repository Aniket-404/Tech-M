import math

def count_perfect_square(arr):
    count = 0
    for i in arr:
        x = int(math.sqrt(i))
        if x * x == i:
            count += 1
        else:
            continue
    print(count)

arr = list(map(int,input().split(" ")))
count_perfect_square(arr)

#input: 25 77 54 81 48
#output: 2