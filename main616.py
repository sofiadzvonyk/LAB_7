def calc(a, b, op):
    if op == "+":
        return f"{a + b:.2f}"
    elif op == "-":
        return f"{a - b:.2f}"
    elif op == "*":
        return f"{a * b:.2f}"
    elif op == "/":
        return f"{a / b:.2f}"
    else:
        return "Unknown operation"
a = float(input())
b = float(input())
op = input()
print(calc(a, b, op))