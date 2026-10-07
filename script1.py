"""Программа приветствия из практической работы №1."""

GreetingText = "Hello, from person3!"

def make_greeting():
    """Возвращает приветствие в верхнем регистре."""
    return GreetingText.upper()

if __name__ == "__main__":
    print(make_greeting())

