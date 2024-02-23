MOD = 998244353

def fibonacci(N):
    fib = [0] * (N + 1)
    fib[1] = 1
    for i in range(2, N + 1):
        fib[i] = (fib[i - 1] + fib[i - 2]) % MOD
    return fib

# Read the input from the user
N = int(input())

# Generate the Fibonacci sequence
fib_numbers = fibonacci(N)

# Print the Fibonacci sequence
for num in fib_numbers[1:]:
    print(num)
