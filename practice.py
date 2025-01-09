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