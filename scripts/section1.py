#!/usr/bin/env python3
# add import and helper functions her
import numpy as np
if __name__ == "__main__":
    print("hello world")
    np.random.seed(42)
    A = np.random.normal(size=(4, 4))
    B = np.random.normal(size=(4, 2))
    print(A@B)
    np.random.seed(42)
    x = np.random.normal(size=(4, 10))
    x_1 = x[None, :, :]
    x_2 = x[:, None, :]
    x_sub = x_1 - x_2
    x_square=np.square(x_sub)
    x_sum = np.sum(x_square, 2)
    print(x_sum)

