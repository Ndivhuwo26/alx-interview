#!/usr/bin/python3
"""
0. Pascal's Triangle
Mock Technical Interview
"""
def pascal_triangle(n):
    """Returns a list of lists of integers representing Pascal’s triangle of n"""
    
    
    triangle = []
    
    
    if n <= 0:
        return triangle
    
    
    for i in range(n):
        
        row = []
        C = 1
        
        
        for j in range(i + 1):
            row.append(C)
            C = C * (i - j) // (j + 1)
        
        
        triangle.append(row)
    
    return triangle
