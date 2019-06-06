import enum


class Order(enum.IntEnum):
    INCREASE = 1
    DECREASE = -1


SOFT_INF = float(10 ** 7)


def bisect_linfunc(func, target, left=-SOFT_INF, right=SOFT_INF, order=Order.INCREASE, num_repeat=50):
    left = float(left)
    right = float(right)
    best_target = None
    best_res = None
    for _ in range(num_repeat):
        mid = (left + right) / 2
        res = func(mid)
        if order * target >= order * res:
            best_target = mid
            best_res = res
            left = mid
        else:
            right = mid
    return best_target, best_res


if __name__ == '__main__':
    EPS = 1e-7
    assert abs(bisect_linfunc(lambda x: x, 100)[0] - 100) < EPS
    assert abs(bisect_linfunc(lambda x: x, 200)[0] - 200) < EPS
    assert abs(bisect_linfunc(lambda x: -x, 200, order=Order.DECREASE)[0] - -200) < EPS

