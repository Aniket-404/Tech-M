def print_neg_temp(arr):
    neg_temp=[]
    for i in arr:
        if i<0:
            neg_temp.append(i)
    return neg_temp

arr=list(map(int,input().split(" ")))
print(print_neg_temp(arr))