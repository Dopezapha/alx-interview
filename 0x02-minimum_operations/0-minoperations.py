def minOperations(n):
    if n <= 1:
        return n
    
    # Find the largest power of 2 that is less than or equal to n
    power_of_2 = 1
    while power_of_2 * 2 <= n:
        power_of_2 *= 2
    
    # If n is a power of 2, the answer is n
    if n == power_of_2:
        return n
    
    # Otherwise, the answer is the power of 2 plus the minimum operations needed for the remaining part
    return power_of_2 + minOperations(n - power_of_2)
