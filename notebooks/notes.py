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


line = input()
a, b = line.split()
a = int(a)
b = int(b)

print(f"I have {a} apples, and {b} bannanas")
"""


def grade(percent: int):
    final = ''
    if percent >= 90:
        final = 'A'
    elif percent >= 80 and percent < 90:
        final = 'B'
    elif percent >= 70 and percent < 80:
        final = 'C'
    elif percent >= 60 and percent < 70:
        final = 'D'
    else:
        final = 'F'

    return final


def main():
    percent = input('What is your grade percent?\n')
    percent = int(percent)
    ans = grade(percent)
    print(f'You have a {ans}')

main()