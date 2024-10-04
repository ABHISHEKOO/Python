import time

def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

def calculate_time_complexity(n):
    start_time = time.time()
    fibonacci_recursive(n)
    end_time = time.time()
    return end_time - start_time

def calculate_space_complexity(n):
    # Recursion creates a stack frame for each function call
    return n

# Get user input for the number of Fibonacci terms
n = int(input("Enter the number of Fibonacci terms: "))

# Generate Fibonacci sequence using recursion
fibonacci_sequence = [fibonacci_recursive(i) for i in range(n)]

# Calculate and print time and space complexity
time_taken = calculate_time_complexity(n)
space_used = calculate_space_complexity(n)

print("Fibonacci Sequence:", fibonacci_sequence)
print("Time Complexity (in seconds):", time_taken)
print("Space Complexity (number of stack frames):", space_used)