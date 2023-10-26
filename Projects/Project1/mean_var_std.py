# This entrypoint file to be used in development. Start by reading README.md
import mean_var_std
from unittest import main
import numpy as np

# solution: calculate()
def calculate(input: list):
    if (len(input) < 9):
        raise ValueError('List must contain nine numbers.')
    
    a = np.array(input).reshape(3, 3)
    
    # axis == 0 == columns
    # axis == 1 == rows
    mean = [a.mean(axis=0).tolist(), a.mean(axis=1).tolist(), a.mean().tolist()]
    variance = [a.var(axis=0).tolist(), a.var(axis=1).tolist(), a.var().tolist()]
    std = [a.std(axis=0).tolist(), a.std(axis=1).tolist(), a.std().tolist()]
    maximum = [a.max(axis=0).tolist(), a.max(axis=1).tolist(), a.max().tolist()]
    minimum = [a.min(axis=0).tolist(), a.min(axis=1).tolist(), a.min().tolist()]
    soma = [a.sum(axis=0).tolist(), a.sum(axis=1).tolist(), a.sum().tolist()]

    return {
        'mean': mean,
        'variance': variance,
        'standard deviation': std,
        'max': maximum,
        'min': minimum,
        'sum': soma
    }

print(mean_var_std.calculate([0,1,2,3,4,5,6,7,8]))

# Run unit tests automatically
main(module='test_module', exit=False)