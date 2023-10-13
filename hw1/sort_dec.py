def sort_list_declarative(numbers: list):
    return sorted(numbers, reverse=True)


if __name__ == '__main__':
    arr = [5, 6, 2, 7, 3, 6]
    print(sort_list_declarative(arr))