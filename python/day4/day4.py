import itertools


def check_decreasing(num):
    _num = str(num)
    for i in range(5):
        if int(_num[i+1]) < int(_num[i]):
            return False
    return True


def check_repeating(num):
    num_list = [list(value) for key, value in itertools.groupby(str(num))]
    for number_count in num_list:
        if len(number_count) == 2:
            return True


count = 0
for x in range(248345, 746316):
    if check_decreasing(x) and check_repeating(x):
        count += 1
print(count)

