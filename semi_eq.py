import numpy as np


def semiEq(array):
    right_sum = np.sum(array)
    left_sum = 0 
    print(right_sum)
    
    for i in range(len(array)):
        print(array[i])
        left_sum += array[i]
        right_sum -= array[i]
        
        if left_sum > right_sum:
            return i
        
    return len(array)


def main():
    array = [1, 1]
    
    if len(array) < 2:
        print('Array is to small. Minimum size is 2.')
        return 
    
    index = semiEq(array)
    print(array)
    print(index)
    
    
if __name__ == '__main__':
    main()