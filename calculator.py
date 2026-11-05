def calculate(first: float, operator: str, second: float) -> float:
    """Return the result of a basic arithmetic operation."""
    if operator == "+":
        return first + second
    if operator == "-":
        return first - second
    if operator == "*":
        return first * second
    if operator == "/":
        if second == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return first / second
    raise ValueError(f"Unsupported operator: {operator}")


def main() -> None:
    try:
        first = float(input("First number: "))
        operator = input("Operator (+, -, *, /): ").strip()
        second = float(input("Second number: "))
        result = calculate(first, operator, second)
    except (ValueError, ZeroDivisionError) as error:
        print(f"Error: {error}")
    else:
        print(f"Result: {result}")


if __name__ == "__main__":
    main()