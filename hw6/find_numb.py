def binary_find_number(sorted_lst: list, numb: int) -> int:
    if numb in sorted_lst:
        min_pos = 0
        max_pos = len(sorted_lst)
        i = len(sorted_lst)//2
        while i != 0 and i != len(sorted_lst):
            if sorted_lst[i] == numb:
                return i
            elif sorted_lst[i] > numb:
                max_pos = i
                i -= (max_pos - min_pos)//2
            else:
                min_pos = i
                i += (max_pos - min_pos)//2
    else:
        return -1


def lazy_binary_find_number(sorted_lst: list, numb: int) -> int:
    if numb in sorted_lst:
        return sorted_lst.index(numb)
    else:
        return -1


lst = [2, 3, 4, 5, 6, 7, 8, 9, 10]
number = 7
print(binary_find_number(lst, number))
print(lazy_binary_find_number(lst, number))
