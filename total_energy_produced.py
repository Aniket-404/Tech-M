def energy_produced(x,r,n):
    total=0
    for i in range (n):
        total+=x
        x+=r
    print(total)

x=int(input())
r=int(input())
n=int(input())
energy_produced(x,r,n)