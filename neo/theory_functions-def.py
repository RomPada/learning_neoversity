
# Приклад функції, що повертає рядок
def greet(name: str) -> str:
    return f"Привіт, {name}!"

greeting = greet("Олексій")
print(greeting)  # Виведе: Привіт, Олексій!


# Приклад функції, яка сумує два числа та повертає результат
def add_numbers(num1: int, num2: int) -> int:
    sum = num1 + num2
    return sum

result = add_numbers(5, 10)
print(result)  # Виведе: 15


# Функція, що повертає булеве значення:
def is_even(num: int) -> bool:
    return num % 2 == 0

check_even = is_even(4)
print(check_even)  # Виведе: True


# функція зі значеннями за замовчуванням
def func(a, b=5, c=10): 
    print('a дорівнює', a,', b дорівнює', b,', а c дорівнює', c)
# a дорівнює 3, b дорівнює 7, а c дорівнює 10
func(3, 7)
# a дорівнює 25, b дорівнює 5, а c дорівнює 24
func(25, c=24)
# a дорівнює 100, b дорівнює 5, а c дорівнює 50
func(c=50, a=100)