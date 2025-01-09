def calcTotalTax(n,arr):
    tax=0
    for i in arr:
        if i > 1000:
            tax_amt=i-1000
            tax+=(tax_amt//10)
    return tax

# n=int(input())
# arr=list(map(int,input().split(" ")))
n = 5
arr = [1000, 2000, 3000, 4000, 5000]
print(calcTotalTax(n,arr))