arr = list(map(int,input().split(" ")))
sort = sorted(arr,reverse=True)
print(sort[0]*sort[1])