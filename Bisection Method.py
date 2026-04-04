def square_root_bisection(num, tolerance=0.01, iterations=5):
    if num < 0:
        raise ValueError("Square root of negative number is not defined in real numbers")
    
    if num == 0 or num == 1:
        print(f"The square root of {num} is {num}")
        return num

    low = 0
    high = max(1, num)

    for i in range(iterations):
        mid = (low + high) / 2

        if (high - low) <= tolerance:
            print(f"The square root of {num} is approximately {mid}")
            return mid

        if mid * mid < num:
            low = mid
        else:
            high = mid

    print(f"Failed to converge within {iterations} iterations")
    return None

square_root_bisection(12345)
