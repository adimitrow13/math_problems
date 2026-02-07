import numpy as np
def absolute_relative_error(p_true, p_approx):
    abs_error = abs(p_true - p_approx)
    rel_error = abs_error / abs(p_true) if p_true != 0 else float ('inf')
    return abs_error, rel_error

p = 3.141592653589793
p_star = 22/7

abs_error, rel_error = absolute_relative_error(p, p_star)
print(f"Absolute error: {abs_error}")
print(f"Relative error: {rel_error}")