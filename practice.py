# unchanged characters
# def unchanged(s):
#     str_rev=s[::-1]
#     unchanged = [s[i] for i in range(len(s)) if s[i]==str_rev[i]]
#     print(" ".join(map(str,unchanged)))

# s='hello'
# unchanged(s)


# product of digits
# num=int(input())
# prod=1
# for i in str(num):
#     prod *= int(i)
# print(prod)


# left shift
def encrypt(num,key):
    num_str = str(num)
    key = key % len(num_str)
    encrypted = num_str[key:] + num_str[:key]
    return int(encrypted)

num=int(input())
key=int(input())
print(encrypt(num,key))