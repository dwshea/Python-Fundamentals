def multiply(var1: int, var2: int):
    answer: int = var1 * var2
    return answer

print(multiply(8,6))

def add(a: float, b: float) -> float:
    answer: float = a + b
    return answer

assert add(2, 3) == 5
assert add(10, -5) == 5
print('All test cases passed!')