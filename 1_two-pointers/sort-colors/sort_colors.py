# vim: set comments=sb\:\"\"\",mb\:##\ \ \ ,ex-3\:\"\"\",fb\:\*,fb\:-,\:##:
# vim: set fo=tcq1rowapn:

## Problem Statement
"""
##   Given an array, colors, which contains a combination of the following three elements:
##   - 0 (representing red)
##   - 1 (representing white)
##   - 2 (representing blue)
##
##   Sort the array in place so that the elements of the same color are adjacent, with the colors in the order of red, white, and blue.
##
##   **Note**: The function should only return the modified colors array.
##
##   Constraints:
##   * 1 <= colors.length <= 300
##   * colors[i] can only contain 0s, 1s, or 2s.
##
##   Example 1:
##   Input: colors = [1,0,2,1,2,2]
##   Output: colors = [0,1,1,2,2,2]
##
##   Example 2:
##   Input: colors = [0,11,2,0,2,0,2,1,2]
##   Output: colors = [0,0,0,1,1,1,2,2,2,2]
##
##   Example 3:
##   Input: colors = [0]
##   Output: colors = [0]
##
"""
##   Understand the Problem
"""
##   1. What is the output if the following array is given as input?
##   colors = [2,2,1,1,0]
##   :: --> colors = [0,1,1,2,2]
##
##   2. What is the output if the following array is given as input?
##   colors = [2,2,0,1,2,2,0,2]
##   :: --> colors = [0,0,1,2,2,2,2,2]
##
##   3. What is the output if the following array is given as input?
##   colors = [0,0,1,0,1,1,1,2,1,2]
##   :: --> [0,0,0,1,1,1,1,1,2,2]
##
"""
##   Arrange the Ste[s
"""
##   1. Initialize 3 pointers, red, white and blue. Where red is set
##      to starting index, white is also set to starting index, and blue
##      is set to the last index.
##   2. If colors[white] is 0, we swap the values of the white and red
##      pointers and increment both pointers by 1.
##   3. Otherwise, if colors[white] is 1, then the index is already in
##      the correct position, so just increment white pointer by 1.
##   4. Otherwise, colors[white] will be 2, so swap the values of white
##      and blue pointers and decrement the blue pointer by 1.
##
"""
##   Write the Solution Code
"""
##             b
##   [0, 0, 1, 1, 2]
##           r    w
##             b
##   [0, 0, 1, 1, 2]
##                w
##                c0181784953
"""
def sort_colors(colors:list[int])->list[int]:
    n = len(colors)
    red,white, = 0,0
    blue = n-1
    while white <= blue:
        if colors[white] == 0:
            if colors[red] != 0:
                colors[red],colors[white] = colors[white],colors[red]
            red+=1
            white+=1
        elif colors[white] == 1:
            white += 1
        else:
            if colors[blue] != 2:
                colors[blue],colors[white] = colors[white],colors[blue]
            blue -= 1
    return colors

##   Solution Sumary
"""
##   This solution traverses the colors array at most one time. In each 
##   iteration, it checks if the value at white pointer is equal to red (0), 
##   then if the value at red pointer is not equal 0, then swap the values at 
##   red and white pointers and increment both pointers by 1, otherwise if 
##   value at red pointer is equal 0 then no need to swap, just increment both 
##   pointers. Otherwise, if the value at white pointer is equal to white (1) 
##   , then it is already in correct position, no need to do any swapping and 
##   just increment the white pointer by 1. Finally, similar to the red case, 
##   if the value at white pointer is equal to blue (2), then if the value at 
##   blue pointer is not equal 2, then swap the values at blue and white 
##   pointers and decrement only the blue counter by 1, otherwise if the value 
##   at blue pointer is equal to 2 then no need to swap, just decrement the 
##   blue pointer by 1. This loop continues while the white pointer is less 
##   than or equal to the blue pointer (or until end of the array in worst 
##   case). After the loop exits, the colors array should be sorted 
##   accordingly, so just return the colors array.
##   
"""
##   Time Complexity
"""
##   The time complexity of this solution is O(n) since it only traverses the 
##   array at most once.
##
"""
##   Space Complexity
"""
##   The space complexity of this solution is O(1) since no additional data 
##   structures are used.
##
"""
