def abb_diff(arr,start_pos):
    start_index = start_pos-1
    total = 0
    for i in range(start_index, len(arr)-1):
        total += abs(arr[i+1]-arr[i])
    return total

arr = list(map(int,input().split(" ")))
start_pos = int(input())
print(abb_diff(arr,start_pos))

#input: 1 2 3 6 4
#input2: 3

#output: 5