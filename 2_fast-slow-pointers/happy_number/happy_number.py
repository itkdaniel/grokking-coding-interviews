# vim: set comments=sb\:\"\"\",mb\:##\ \ \ ,ex-3\:\"\"\",fb\:\*,fb\:-,\:##:
# vim: set fo=tcq1rowapn:

##   Problem Statement
"""
##   Write an algorithm to determine if a number n is a happy number.
##   We use the following process to validate if a given number is a happy 
##   number:
##      * Starting with the given number n, replace the number with the sum of 
##      the sqaures of its digits.
##      * Repeat the process until:
##          - The number equals 1, which will depict that the given number 
##          n is a happy number.
##          - It enters a cycle, which will depict that the given number n is 
##          not a happy number.
##      Return True if n is a happy number, else False if not.
##
##  Constraints:
##  * 1 <= n <= 2^n-1
##
##  Example 1:
##  Input: n = 23
##  Output: True
##      - Explanation:
##      2^2 + 3^2 = 13
##      1^2 + 3^2 = 10
##      1^2 + 0^2 = 1
##      The sum of the square of the two digits 1 and 0 equals 1. Hence, 23 is 
##      a happy number.
##
##  Example 2:
##  Input: n = 2
##  Output: False
##      - Explanation:
##      2^2 = 4 <-- 
##      4^2 = 16
##      1^2 + 6^2 = 37
##      3^2 + 7^2 = 58
##      5^2 + 8^2 = 89
##      8^2 + 9^2 = 145
##      1^2 + 4^2 + 5^2 = 42
##      4^2 + 2^2 = 20
##      2^2 + 0^2 = 4  <--
##      Since we've encountered 4 before, it indicates that there exists 
##      a cycle, thus 2 is not a happy number.
##
"""
##   Understand the Problem
"""   
##   1. Is 28 a happy number?
##   :: --> True
##
##   2. Is 4 a happy number?
##   :: --> False
##      - Explanation: Eventually, we come across a sum of squares which 
##      equals to 4, and 4 is the original number, this indicates a cycle, 
##      thus 4 is not a happy number.
##
"""
##   Arrange the Steps
"""
##   1. Initialize the slow and fast numbers where slow is the inpt number and 
##      fast the the sum of the squares of the input number's digits.
##   2. If fast is not 1 and also not equal to slow, increment slow by one 
##      iteration and fast by two iterations. Essentially, set slow to 
##      SumOfSquaredDigits(slow) and fast to 
##      SumOfSquaredDigits(SumOfSquaredDigits(fast)).
##   3. If fast converges to 1, return True, otherwise return False.
##
"""
##   Write the Solution Code
def is_happy_number(n:int)->bool:
    def sum_of_squared_digits(num:int)->int:
        zsum = 0
        while num > 0:
            digit = num % 10
            num = num // 10
            zsum += digit ** 2
        return zsum
    slow = n
    fast = sum_of_squared_digits(slow)
    while slow != fast and fast != n and fast != 1:
#        if fast == 1:
#            return True
        slow = sum_of_squared_digits(slow)
        fast = sum_of_squared_digits(sum_of_squared_digits(fast))
    if fast == 1:
        print(n, 'is happy! 😄')
        return (True, '😄')
    print(n, 'is not happy...🥺')
    return (False, '🥺')

##   Time Complexty
"""
##   The time complexity for this algorithm is O(log n), where n is the input 
##   number.
##
##   The worst case time complexity of this algorithm is given by the case of 
##   a non-happy number, since it gets stuck in a cycle, whereas a happy 
##   number quickly converges to 1. Let's first calculate the time complexity 
##   of the sum_of_squared_digits function. Since we are calculating the sum 
##   of all digits in a number, the time commplexity of this function is O(log 
##   n), because the number of digits in the number n is log~10~n.  
##
##   The following table can give you an idea of what the time complexity 
##   looks like by considering the largest possible next number for each given 
##   number of digits:
##   
##   Digits         Largest number      Sum of squared digits

        1                   9                   81

        2                  99                   162
    
        3                 999                   243

        4                9999                   324

        12           999999999999               972

        13          9999999999999               1053

        14          99999999999999              1134

##   To estimate the count of numbers in a cycle, let's consider the following 
##   two cases:
##   1. **Numbers with three digits**: The largest three digit number is 
##      999. The sum of the squares of its digits is 243. Therefore, for
##      three-digit numbers, no number in the cycle can go beyond 
##      243. Therefore, the time complexity in this case is given as O(243 x3)
##      , where 243 is the maximumcount of numbers in a cycle and 3 is the 
##      number of digits in a three digit number. This is why the time 
##      complexity in the case of numbers with three digits is O(1).       
##
##   2. **Numbers with more than three digits**: Any number with more than 
##      three digits wil lose at least one digit at every step ntil it becomes 
##      a three-digit number. For example, the first four digit number that we 
##      can get in the cycle is 1053, which is the sum of the squareof digits 
##      in 9999999999999. Therefore, the time complexity of any number with 
##      more than three digits can be expressed as `O(logn + log log n + log 
##      log log n + ...). Since O(logn) is the dominating term, we an write 
##      the time complexity as O(logn). Therefore, the total time complexity 
##      comes out to be O(1 + logn), which is O(logn).
##
"""
##   Space Complexity
"""
##   The space complexity of this algorithm is O(1).
##
"""
