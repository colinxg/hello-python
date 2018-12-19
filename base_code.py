# 求杨辉三角第n行第k列
# m 行有m个元素，所以k不能大于m
#       1
#       11
#      121
#      1331
m = 5
k = 4
triangle = []
for i in range(m):
    # 所有行都需要1开头
    row = [1]
    triangle.append(row)
    if i == 0 :
        continue
    for j in range(1, i):
        row.append(triangle[i-1][j-1]+triangle[i-1][j])
    row.append(1)

# print(triangle)

# R-1.1
def is_multiple(n, m):
    try:
        if n == int(n) and m == int(m):
            a, b = divmod(n, m)
            return True if a >0 and b == 0 else False
        else:
            print('zhe parameter must be int type')
    except (TypeError, ValueError):
        print('zhe parameter must be int type')
    return 'Error'

# print(is_multiple('a', 'b'))
# print(is_multiple(1,1.5))

# R-1.3
# def minmax(lst):
#     mixnumber = 0
#     maxnumber = 0
#     for i in lst:
#         if

# R-1.4
def sumsquare(n):
    ret = 0
    for i in range(1, n+1):
        ret += i**2
    return ret

# print(sumsquare(3))


# R-1.5
def sumsquare(n):
    ret = [x*x for x in range(1, n+1)]
    return sum(ret)

# print(sumsquare(3))

# R-1.12


