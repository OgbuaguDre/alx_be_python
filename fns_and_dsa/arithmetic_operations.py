def perform_operation(num1: float, num2: float, operation: str):
    """
    Performs basic arithmetic operations.

    Args:
        num1 (float): The first number.
        num2 (float): The second number.
        operation (str): The operation to perform ('add', 'subtract', 'multiply', 'divide').

    Returns:
        float or str: The result of the operation, or an error message for division by zero.
    """
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2
    else:
        return "Error: Invalid operation"

# Example usage
if __name__ == "__main__":
    print(perform_operation(5, 3, 'add'))        # Output: 8
    print(perform_operation(5, 3, 'subtract'))   # Output: 2
    print(perform_operation(5, 3, 'multiply'))   # Output: 15
    print(perform_operation(5, 0, 'divide'))     # Output: Error: Division by zero
    print(perform_operation(5, 3, 'divide'))     # Output: 1.666...
    print(perform_operation(5, 3, 'modulus'))    # Output: Error: Invalid operation
