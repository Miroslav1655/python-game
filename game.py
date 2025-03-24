import random

def guess_the_number():
    secret_number = random.randint(1, 10)
    attempts = 3
    
    print("Угадай число от 1 до 10! У тебя 3 попытки.")
    
    for attempt in range(1, attempts + 1):
        print(f"\nПопытка {attempt} из {attempts}")
        try:
            guess = int(input("Введи число: "))
        except ValueError:
            print("Пожалуйста, введи число от 1 до 10!")
            continue
            
        if guess < 1 or guess > 10:
            print("Число должно быть от 1 до 10!")
            continue
            
        if guess == secret_number:
            print("Поздравляю! Ты угадал число!")
            return
        elif guess < secret_number:
            print("Загаданное число больше.")
        else:
            print("Загаданное число меньше.")
    
    print(f"\nК сожалению, ты не угадал. Загаданное число было: {secret_number}")

# Запуск игры
guess_the_number()
