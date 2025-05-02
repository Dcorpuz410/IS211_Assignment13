def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def compareTo(s1, s2):
    if not s1 and not s2:
        return 0
    elif not s1:
        return -1
    elif not s2:
        return 1
    else:
        if s1[0] < s2[0]:
            return -1
        elif s1[0] > s2[0]:
            return 1
        else:
            return compareTo(s1[1:], s2[1:])

if __name__ == "__main__":
    print("Fibonacci(5):", fibonacci(5))
    print("Fibonacci(7):", fibonacci(7))

    print("GCD(36, 60):", gcd(36, 60))
    print("GCD(100, 80):", gcd(100, 80))

    print("compareTo('abc', 'abc'):", compareTo("abc", "abc"))
    print("compareTo('abc', 'abd'):", compareTo("abc", "abd"))
    print("compareTo('abd', 'abc'):", compareTo("abd", "abc"))