"""
Dynamic programming
"""
import copy
import math


def del_specified_value(list, value):
    list_res = copy.deepcopy(list)
    j = 0
    for i in range(len(list_res)):
        if list_res[j] == value:
            list_res.pop(j)
        else:
            j += 1
    return list_res


def segment(ops):
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    op_nums = []  # oprate numbers indeed
    i = 0
    flag = 0
    temp = 0
    while i < len(ops):
        if flag == 0:
            temp = numbers[i]
        if ops[i] == 0:
            flag = 1
            temp = temp * 10 + numbers[i + 1]
            if i == len(ops) - 1:
                op_nums.append(temp)
        else:
            flag = 0
            op_nums.append(temp)
            if i == len(ops) - 1:
                op_nums.append(numbers[i + 1])
        i += 1
    return op_nums


def compute(ops):
    op_nums = segment(ops)

    ops_cur = del_specified_value(ops, 0)

    res = op_nums[0]
    for index, op in enumerate(ops_cur):
        if op == 1:
            res += op_nums[index + 1]
        elif op == 2:
            res -= op_nums[index + 1]
    return res


def print_expression(ops, res):
    op_nums = segment(ops)
    ops_cur = del_specified_value(ops, 0)
    print(op_nums[0], end='')
    for index, op in enumerate(ops_cur):
        if op == 1:
            print(' + ', end='')
        elif op == 2:
            print(' - ', end='')
        print(op_nums[index + 1], end='')
    print(' = %s' % res)

# def print_expression(ops, res):
#     op_nums = segment(ops)
#     ops_cur = del_specified_value(ops, 0)
#     print('<tr align=\"center\">\n<td>', end='')
#
#     print(op_nums[0], end='')
#     for index, op in enumerate(ops_cur):
#         if op == 1:
#             print(' + ', end='')
#         elif op == 2:
#             print(' - ', end='')
#         print(op_nums[index + 1], end='')
#     print(' = %s' % res, end='')
#
#     print('</td>\n</tr>')


def Find_expression(value):
    # ops represents each operator
    ops = [0, 0, 0, 0, 0, 0, 0, 0]
    cnt = 0
    loop = True
    while loop:
        res = compute(ops)
        if res == value:
            print_expression(ops, res)
            cnt += 1
        for i in range(len(ops)):
            if ops[i] != 2:
                ops[i] += 1
                break
            else:
                ops[i] = 0
                if i == len(ops) - 1:
                    loop = False
    return cnt

# def Find_expression_cnt(value):
#     # ops represents each operator
#     ops = [0, 0, 0, 0, 0, 0, 0, 0]
#     cnt = 0
#     loop = True
#     while loop:
#         res = compute(ops)
#         if res == value:
#             # print_expression(ops, res)
#             cnt += 1
#         for i in range(len(ops)):
#             if ops[i] != 2:
#                 ops[i] += 1
#                 break
#             else:
#                 ops[i] = 0
#                 if i == len(ops) - 1:
#                     loop = False
#     return cnt


# if __name__ == "__main__":
#     for i in range(1, 101):
#         cnt = Find_expression_cnt(i)
#         print('<tr align=\"center\">\n<th rowspan=\"%s\">%s</th>\n</tr>' % (cnt+1, i))
#         Find_expression(i)

if __name__ == "__main__":
    table = []
    for i in range(1, 101):
        cnt = Find_expression(i)
        table.append(cnt)
    max_temp = 0
    min_temp = math.inf
    max = []
    min = []
    for index, t in enumerate(table):
        if t > max_temp:
            max_temp = t
            max.clear()
            max.append(index + 1)
        elif t == max_temp:
            max.append(index + 1)
        if t < min_temp:
            min_temp = t
            min.clear()
            min.append(index + 1)
        elif t == min_temp:
            min.append(index + 1)
    print('Total_solutions: %s' % table)
    print('max solutions: %s' % max)
    print('max solutions count: %s' % table[max[0]-1])
    print('min solutions: %s' % min)
    print('min solutions count: %s' % table[min[0] - 1])
