def print_table(start, end):
    out_string = ''
    for i in range(1, 10):
        plus_string = ''
        for j in range(start, end):
            one_decision = f"{j}x{i}={i*j}   "
            plus_string += one_decision
        out_string += plus_string + '\n'
    return out_string


def multiplication_table(n: int):
    table = ''
    max_step = n
    step = 5
    start = 1
    while max_step > step:
        table += print_table(start, start+5) + '\n'
        max_step -= step
        start += step
    table += print_table(start, n+1)
    return table


if __name__ == '__main__':
    print(multiplication_table(23))
