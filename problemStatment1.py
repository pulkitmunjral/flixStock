"""
Problem Statement 1: Numpy
● Write python code to create the smallest bounding rectangle of all non zero values in a numpy array
○ Consider a 2D numpy array which is filled with zeros
○ Few random cells have non zero values
○ Find the coordinates(x,y,height,width) of the smallest rectangle that contains all non zero values
"""
# importing the required library numpy as np
import numpy as np


# function to calculate the coordinates which takes 2D list as input
def problem_statement_1(array):

    # converting 2D list into numpy array
    array = np.array(array)

    # getting the size of the array
    size_x, size_y = array.shape

    # initializing the required coordinates with maximum limits
    x_min, y_min, x_max, y_max = size_x, size_y, 0, 0

    # looping on all the elements 1 by 1 to check the non zero element
    # time complexity costing to be size_y*size_x that is O(n^2)
    for row in range(size_x):
        for col in range(size_y):

            # if the non zero element is found storing it's coordinate according
            if array[row, col] != 0:
                x_min = col if x_min > col else x_min
                y_min = row if y_min > row else y_min
                x_max = col if x_max < col else x_max
                y_max = row if y_max < row else y_max

    # return the string output of the function
    return f"The starting coordinates (x,y):- ({x_min},{y_min}) and the (width, height):- ({x_max-x_min},{y_max-y_min})"


inputArray = [[0, 0, 0, 0, 0],
              [0, 1, 0, 0, 0],
              [0, 1, 0, 0, 0],
              [0, 0, 0, 1, 0],
              [0, 0, 0, 0, 0]]

output = problem_statement_1(inputArray)
print(output)
