"""Return string that excludes the vowels"""

def exclude_vowels(str_char):
    ans=[]
    vowels = 'aeiouAEIOU'
    for i in str_char:
        if i not in vowels:
            ans.append(i)
            result = "".join(map(str,ans))
    return result

str_char = 'aniket'
print(exclude_vowels(str_char))


# vowels='aeiouAEIOU'
# str_char='aniket'
# excluded = [char for char in str_char if char not in vowels]
# print("".join(excluded))