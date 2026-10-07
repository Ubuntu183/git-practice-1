"""Программа приветствия с поддержкой именного приветствия."""

GreetingText = "Hello, from person3!"

def make_greeting(name=None):
    """Возвращает приветствие в верхнем регистре с необязательным именем."""
    if name is None:
        return GreetingText.upper()
    return f"Hello, {name}!".upper()

if __name__ == "__main__":
    print(make_greeting())
