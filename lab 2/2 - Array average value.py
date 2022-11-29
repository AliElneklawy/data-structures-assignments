str_arr = input()
if len(str_arr) == 2:
    print(0.0)
else:
    list_arr = list(map(float, str_arr.strip('][').split(', ')))
    print(sum(list_arr)/len(list_arr))