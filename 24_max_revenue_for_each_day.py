#return max revenue for each day
def calcRevenue(sales):
    max_revenue = []
    for day in sales:
        max_revenue.append(max(day))

    return max_revenue

days, product = map(int,input().split(" "))
sales = [list(map(int,input().split())) for i in range(days)]
print(" ".join(map(str,calcRevenue(sales))))