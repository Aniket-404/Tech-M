def left_shift(num,key):
    num_str = str(num)
    key = key % len(num_str)
    shifted = num_str[key:] + num_str[:key]
    return int(shifted)

num=int(input())
key=int(input())
print(left_shift(num,key))