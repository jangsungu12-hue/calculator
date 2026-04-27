def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def calculate(expression: str) -> float:
    """Evaluate a simple arithmetic expression: number op number."""
    ops = {'+': add, '-': subtract, '*': multiply, '/': divide}
    for op in ('/', '*', '-', '+'):
        if op in expression:
            left, _, right = expression.partition(op)
            return ops[op](float(left.strip()), float(right.strip()))
    raise ValueError(f"No valid operator found in: {expression!r}")


def main():
    print("사칙연산 계산기 (종료: q)")
    while True:
        expr = input("> ").strip()
        if expr.lower() == 'q':
            break
        try:
            result = calculate(expr)
            print(result)
        except ValueError as e:
            print(f"오류: {e}")


if __name__ == "__main__":
    main()
