def odd_sum(num):
    count=0
    for i in str(num):
        if int(i)%2!=0:
            count+=int(i)
    return count

num = int(input())
print(odd_sum(num))