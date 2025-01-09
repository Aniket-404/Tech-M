def remove_dup(n,arr):
    ans=[]
    for i in arr:
        if i not in ans:
            ans.append(i)
    print(" ".join(map(str, ans)))

n = 8
arr = [1, 1, 3, 2, 1, 4, 5, 4]
remove_dup(n,arr)