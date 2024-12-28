class Parser:
    def __init__(self, text):
        # Tokenize the input text by separating parentheses and splitting by spaces
        self.tokens = text.replace('(', ' ( ').replace(')', ' ) ').split()
        self.current_token = None
        self.next_token()

    def next_token(self):
        # Advance to the next token
        self.current_token = self.tokens.pop(0) if self.tokens else None

    def parse_expression(self):
        # Parse an expression, which can have terms connected by '+' or '-'
        result = self.parse_term()
        while self.current_token in ('+', '-'):
            operator = self.current_token
            self.next_token()
            if operator == '+':
                result += self.parse_term()
            elif operator == '-':
                result -= self.parse_term()
        return result

    def parse_term(self):
        # Parse a term, which can have factors connected by '*' or '/'
        result = self.parse_factor()
        while self.current_token in ('*', '/'):
            operator = self.current_token
            self.next_token()
            if operator == '*':
                result *= self.parse_factor()
            elif operator == '/':
                result /= self.parse_factor()
        return result

    def parse_factor(self):
        # Parse a factor, which can be a number or an expression in parentheses
        if self.current_token == '(':
            self.next_token()  # Skip '('
            result = self.parse_expression()
            self.next_token()  # Skip ')'
        else:
            result = int(self.current_token)  # Convert token to integer
            self.next_token()
        return result

# Example usage:
expression = "3 + 5 * (2 - 8)"
parser = Parser(expression)
result = parser.parse_expression()
print(f"The result of '{expression}' is {result}")

# Additional test cases:
expressions = [
    "3 + 5 * 2 - 8",
    "(3 + 5) * 2",
    "10 / 2 + 3 * 4",
    "10 / (2 + 3) * 4",
    "2 - 3 * 4 + 6 / 2"
]

for expr in expressions:
    parser = Parser(expr)
    result = parser.parse_expression()
    print(f"The result of '{expr}' is {result}")
