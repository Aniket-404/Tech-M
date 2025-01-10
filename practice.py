#count unique repeating numbers
# def countRepeat(num):
#     data=str(num)
#     unique=set()
#     for i in data:
#         if data.count(i)>1:
#             unique.add(i)
#     count=len(unique)
#     return count

# num=121342
# print(countRepeat(num))


#exclude vowel
# def exclude_vowel(char):
#     vowels = 'aeiouAEIOU'
#     ans=[]
#     for i in char:
#         if i not in vowels:
#             ans.append(i)
#     return ans

# char='aniket'
# result=exclude_vowel(char)
# print("".join(map(str,result)))


#product of digits
# def mul_dig(num):
#     num_str = str(num)
#     prod = 1
#     for i in num_str:
#         prod*=int(i)
#     return prod

# num=345
# print(mul_dig(num))



#sum of absolute difference between adjacent numbers from user defined position
# def sum_adjnum(arr,pos):
#     strat_index=pos-1
#     count=0
#     for i in range(strat_index,len(arr)-1):
#         count+=abs(arr[i+1]-arr[i])
#     return count

# arr=[1,2,3,6,4]
# pos=3
# print(sum_adjnum(arr,pos))


#left shift encryption
# def encrypt(num,key):
#     strnum = str(num)
#     key = key % len(strnum)
#     encrypted = strnum[key:] + strnum[:key]
#     return encrypted

# num = 25143
# key = 3
# print(encrypt(num,key))


#max revenue for each day, matrix question
# def revenue(sales):
#     max_revenue=[]
#     for i in sales:
#         max_revenue.append(max(i))
#     return max_revenue

# day,prod= list(map(int,input().split(" ")))
# sales = [list(map(int,input().split())) for i in range(day)]
# print(" ".join(map(str,revenue(sales))))



#print count less than k
# def count(num,k):
#     count=0
#     for i in num:
#         if i<k:
#             count+=1
#     return count

# num=list(map(int,input().split(" ")))
# k = int(input())
# print(count(num,k))



#print negative temp
# def neg_temp(arr):
#     temp=[]
#     for i in arr:
#         if i<0:
#             temp.append(i)
#     return temp

# temp = [10,20,-10,-20]
# print(" ".join(map(str,neg_temp(temp))))



#remove deplicated but preserve sequence
# def rem_dup(arr):
#     ans=[]
#     for i in arr:
#         if i not in ans:
#             ans.append(i)
#     return ans

# arr=[1,2,3,3,5,4,5]
# print(rem_dup(arr))



#sum of different arr elements
# def diff_sum(num):
#     sum = 0
#     for i in range(len(num)-1):
#         sum += abs(num[i+1]-num[i])
#     return sum

# num = [1,2,3,4,5]
# print(diff_sum(num))


#sum of off digits
# def sum_odd(num):
#     str_num=str(num)
#     sum=0
#     for i in str_num:
#         if int(i)%2!=0:
#             sum+=int(i)
#     return sum

# num = 123
# print(sum_odd(num))



# def unchanged_char(char):
#     ans=[]
#     char_rev=char[::-1]
#     for i in range(len(char)):
#         if char[i]==char_rev[i]:
#             ans.append(char[i])
#     return ans

# char='hello'
# print(unchanged_char(char))



#calculate tax
# def cal_tax(arr):
#     tax = 0
#     for i in arr:
#         if i>1000:
#             tax_payable = i-1000
#             tax += (tax_payable//10)
#     return tax

# amt=[1000,2000,3000,4000,5000]
# print(cal_tax(amt))


#count odd even diff
# def count_odd_even(arr):
#     even=0
#     odd=0
#     for i in arr:
#         if i%2==0:
#             even+=1
#         else:
#             odd+=1
#     ans = odd-even
#     return ans

# num=[10,20,30,40,55,66,77,83]
# print(count_odd_even(num))


#count perfect square
# import math
# def count_per_sqr(arr):
#     count=0
#     for i in arr:
#         x=int(math.sqrt(i))
#         if x*x==i:
#             count+=1
#     return count

# arr=[25,77,54,81,48]
# print(count_per_sqr(arr))




#product of 2 largest numbers
# def prod_2_larg_num(arr):
#     arr.sort(reverse=True)
#     return arr[0]*arr[1]

# arr=[4,3,6,7,9]
# print(prod_2_larg_num(arr))



#sum of smallest and largest prime in a given range
# def is_prime(n):
#     if n<2:
#         return False
#     for i in range(2,n):
#         if n%i==0:
#             return False
#     else:
#         return True
    
# def sum_prime(start,end):
#     ans=[]
#     for i in range(start,end+1):
#         if is_prime(i):
#             ans.append(i)
#     return ans[0]+ans[-1]

# start,end=1,7
# print(sum_prime(start,end))



#calculate total energy produced
# def energy(x,r,n):
#     total=0
#     for i in range(n):
#         total+=x
#         x+=r
#     return total

# x=8
# r=2
# n=5
# print(energy(x,r,n))




def energy(x,r,n):
    total=0
    for i in range(n):
        total+=x
        x+=r
    return total

x=8
r=2
n=5
print(energy(x,r,n))