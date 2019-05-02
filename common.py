import numpy as np

def create_dataset(number, variance, step=2, correlation=1, offset=(0, 1)):
    x_off, y_off = offset
    xs = np.arange(x_off, number + x_off)
    ys = np.arange(y_off, number*step + y_off, step)
    if correlation == -1:
        ys = ys[::-1]
    ys += np.random.randint(-variance, variance, size=number)
    return xs, ys