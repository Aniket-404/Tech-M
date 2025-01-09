def count_odd_even_diff(n,arr):
    count_even = 0
    count_odd = 0
    for i in arr:
        if i%2==0:
            count_even += 1
        else:
            count_odd += 1
    difference = count_even-count_odd
    return difference

n = int(input()) #8
arr=list(map(int,input().split(" "))) # 10 20 30 40 55 66 77 83
print(count_odd_even_diff(n,arr)) # output: 2
