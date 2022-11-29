from itertools import count


str_arr = input()
val = int(input())
if len(str_arr) == 2:
    print([])
else:
    val_arr = []
    list_arr = list(map(int, str_arr.strip('][').split(', ')))
    val_arr = (list(val for _ in range(list_arr.count(val))))
    list_arr = list(filter(lambda x: x != val, list_arr))
    
    for num in val_arr:
        list_arr.append(num)
    print(list_arr)
    
