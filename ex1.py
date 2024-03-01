#Chat GPT generated

import sys

def evaluate_sexpression(expr):
    def tokenize(expression):
        # Tokenize input string into numbers, parentheses, and operators
        tokens = expression.replace('(', ' ( ').replace(')', ' ) ').split()
        return tokens

    def evaluate(tokens):
        stack = []
        for token in tokens:
            if token == ')':
                # Start evaluating when we hit a closing parenthesis
                expr = []
                while stack and stack[-1] != '(':
                    expr.append(stack.pop())
                stack.pop()  # Remove the '(' from the stack
                # The expression should be in reverse order; reverse it back
                expr = expr[::-1]
                # Assuming valid expressions, the first item is the operator, followed by two operands
                operator, operand1, operand2 = expr[0], int(expr[1]), int(expr[2])
                # Perform the calculation and push the result back onto the stack
                if operator == '+':
                    stack.append(operand1 + operand2)
                elif operator == '-':
                    stack.append(operand1 - operand2)
                elif operator == '*':
                    stack.append(operand1 * operand2)
                elif operator == '/':
                    stack.append(operand1 / operand2)  # Note: This does integer division in Python 2
            else:
                # For anything other than ')', push onto the stack (including numbers and '(')
                stack.append(token)
        return stack[0]

    tokens = tokenize(expr)
    return evaluate(tokens)

def main():
    userInput = sys.argv[1]
    result = evaluate_sexpression(userInput)
    print(f"Result of '{userInput}':", result)

if __name__ == "__main__":
    main()