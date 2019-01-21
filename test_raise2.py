def xxx(x, a):
    try:
        y = x + x / a
        if -0.000000000000001 < a and a < 0.000000000000001 and a != 0:
            raise ZeroDivisionError('aの絶対値 < 0.000000000000001')
    except ZeroDivisionError as eee:
        print('warning:関数xxx()')
#         raise
    else:
        return y

try:
    y = xxx(1, 0)
except ZeroDivisionError as eee:
    print(eee.args[0])
else:
    print('x + x / a =',y)

try:
    y = xxx(1, 0.000000000000000001)
except ZeroDivisionError as eee:
    print(eee.args[0])
else:
    print('x + x / a =',y)

try:
    y = xxx(1, 0.1)
except ZeroDivisionError as eee:
    print(eee.args[0])
else:
    print('x + x / a =',y)
