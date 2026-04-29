import ast
import operator as _op


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


_OPERATORS = {
    ast.Add: _op.add,
    ast.Sub: _op.sub,
    ast.Mult: _op.mul,
    ast.Div: _op.truediv,
    ast.USub: _op.neg,
}


def _eval_node(node, expression):
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return float(node.value)
    if isinstance(node, ast.BinOp) and type(node.op) in _OPERATORS:
        left = _eval_node(node.left, expression)
        right = _eval_node(node.right, expression)
        if isinstance(node.op, ast.Div) and right == 0:
            raise ValueError("Cannot divide by zero")
        return _OPERATORS[type(node.op)](left, right)
    if isinstance(node, ast.UnaryOp) and type(node.op) in _OPERATORS:
        return _OPERATORS[type(node.op)](_eval_node(node.operand, expression))
    raise ValueError(f"Unsupported expression: {expression!r}")


def calculate(expression: str) -> float:
    """Evaluate an arithmetic expression supporting +, -, *, /, parentheses, and operator precedence."""
    try:
        tree = ast.parse(expression.strip(), mode='eval')
    except SyntaxError:
        raise ValueError(f"Invalid expression: {expression!r}")
    return _eval_node(tree.body, expression)


def main():
    print("계산기 (종료: q)")
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
