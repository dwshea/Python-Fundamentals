"""
def multiply(var1: int, var2: int) -> int:
    answer: int = var1 * var2
    return answer

print(multiply(8,6))

def add(a: float, b: float) -> float:
    answer: float = a + b
    return answer

assert add(2, 3) == 5
assert add(10, -5) == 5
assert add(100, 99.9) == 199.9
#assert add(99.99, 1.99) == 101.98  --- false becasue the computer thinks the answer is 101.97999999999
assert abs(add(99.99, 1.99) - 101.98) < 0.000001
print('All test cases passed!')
"""

line = input()
a, b = line.split()
a = int(a)
b = int(b)

print(f"I have {a} apples, and {b} bannanas")