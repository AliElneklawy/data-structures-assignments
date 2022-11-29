str_arr = input()
if len(str_arr) == 2:
    print([])
else:
    list_arr = list(map(int, str_arr.strip('][').split(', ')))

    list_arr = list_arr[::-1]
    print(list_arr)