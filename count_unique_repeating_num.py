def count_repeating_num(data):
    data=str(data)
    unique=set()
    for i in data:
        if data.count(i)>1:
            unique.add(i)
        
    len_data=len(unique)
    print(len_data)

num = int(input())
count_repeating_num(num)

#input: 121342
#output: 2