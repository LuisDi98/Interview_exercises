#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum(arr):
    max_sum = 0
    centerIndex = [1, 1]
    
    counter = 1
    while centerIndex[0] < len(arr) - 1 and centerIndex[1] < len(arr[0]) - 1:
        upper_part = arr[centerIndex[1]-1][centerIndex[0]-1:centerIndex[0]+2]
        center_part = [arr[centerIndex[1]][centerIndex[0]]]
        lower_part = arr[centerIndex[1]+1][centerIndex[0]-1:centerIndex[0]+2]
        current_sum = sum(upper_part + center_part + lower_part)
        counter += 1
        if max_sum < current_sum:
            max_sum = current_sum
        if centerIndex[0] == 3:
            centerIndex[0] = 0
            centerIndex[1] = centerIndex[1] + 1
        else:
            centerIndex[0] = centerIndex[0]+1
    return max_sum
        
        
    
        

if __name__ == '__main__':
    arr = [
        [1, 1, 1, 0, 0, 0,],
        [0, 1, 0, 0, 0, 0,],
        [1, 1, 1, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0,]
    ]
    
    result = hourglassSum(arr)
    print("Test case 1:")
    print(result)

    

    arr = [
        [1, 1, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0],
        [0, 0, 2, 4, 4, 0],
        [0, 0, 0, 2, 0, 0],
        [0, 0, 1, 2, 4, 0]
    ]
    
    result = hourglassSum(arr)
    print("Test case 2")
    print(result)


