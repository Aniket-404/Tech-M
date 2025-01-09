def count_less_than_k(num,k):
    count=0
    for i in num:
        if i<k:
            count+=1
    return count

num = list(map(int,input().split(" ")))
k = int(input())
print(count_less_than_k(num,k))