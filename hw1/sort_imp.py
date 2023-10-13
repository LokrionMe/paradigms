def check_root(numbers: list, len_list: int, root: int):
    largest = root
    left = 2 * root + 1
    right = 2 * root + 2
    if left < len_list and numbers[root] < numbers[left]:
        largest = left
    if right < len_list and numbers[largest] < numbers[right]:
        largest = right
    if largest != root:
        numbers[root], numbers[largest] = numbers[largest], numbers[root]
        check_root(numbers, len_list, largest)


def sort_list_imperative(numbers: list):
    n = len(numbers)
    for i in range(n, -1, -1):
        check_root(numbers, n, i)
    return numbers


if __name__ == '__main__':
    arr = [5, 6, 2, 7, 3, 6]
    print(sort_list_imperative(arr))
