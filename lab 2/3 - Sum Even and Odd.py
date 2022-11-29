str_arr = input()
if len(str_arr) == 2:
    print([0, 0])
else:
    list_arr = list(map(int, str_arr.strip('][').split(', ')))

    even_elems = []; odd_elems = []

    for elem in list_arr:
        if elem % 2 == 0:
            even_elems.append(elem)
        else:
            odd_elems.append(elem)
    
    [even_sum, odd_sum] = (sum(even_elems), sum(odd_elems))
    print([even_sum, odd_sum])
