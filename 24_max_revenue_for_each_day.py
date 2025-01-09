def calcRevenue(days,product,sales):
    max_revenue = [max(day) for day in sales]
    return max_revenue

days, product = map(int,input().split(" "))
sales = [list(map(int,input().split(" "))) for _ in range(days)]

result = calcRevenue(days,product,sales)
print(" ".join(map(str,result)))