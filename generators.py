from functools import reduce
numbers = [5, 12, 7, 20, 3, 18, 2, 15, 9, 30,11, 6]
def greater_than_ten(nums):
    for num in nums:
        if num > 10:
            yield num

def square_numbers(nums):
    for num in nums:
        yield num**2

greater_iter = greater_than_ten(numbers)
squares_iter =square_numbers(numbers)
even_squares = filter(lambda x: x % 2 ==0, squares_iter)

strings_iter = map(lambda x: f"value={x}", even_squares)
print("чётные квадраты чисел > 10:")
for s in strings_iter:
    print(s)

total = reduce(lambda a, b: a + b, numbers)
maximum = reduce(lambda a, b: a if a > b else b, numbers)
print(f"Сумма всех чисел списка: {total}")
print(f"Максимальное число списка: {maximum}")

def multiples_of_three(n):
    count = 0
    num = 3
    while count < n:
        yield num
        num += 3
        count += 1

print("Первые 10 чисел, кратных 3:")
for val in multiples_of_three(10):
    print(val, end=" ")
print()

def word_generator(text):
    for word in text.split():
        yield word

text_example = "Python это мощный и простой язык программирования"
print(f"Слова из строки '{text_example}':")
for w in word_generator(text_example):
    print(w, end=" | ")
print()

text_for_filter = "Программирование требует практики и терпения"
words = text_for_filter.split()
long_words = filter(lambda w: len(w) > 4, words)
upper_words = map(str.upper, long_words)
print(f"\nСлова длиной >4 в верхнем регистре из строки '{text_for_filter}':")
for uw in upper_words:
    print(uw, end=" ")
print()

def fibonacci(n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

print("Первые 10 чисел Фибоначчи:")
for fib in fibonacci(10):
    print(fib, end=" ")
print()
