#Dzień 87 - List Comprehensions

# Zamiast pętli for, możesz użyć list comprehension, aby uzyskać kwadraty liczb od 1 do 10
from tkinter.font import names

squares = [x ** 2 for x in range(1, 11)]
print(squares) # Wynik: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Utwórz listę z parzystymi liczbami z zakresu od 1 do 20
even_numbers = [x for x in range(1, 21) if x % 2 == 0]
print(even_numbers) # Wynik: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

#Set Comprehensions
# Utwórz zbiór zawierający długości słów z podanej listy
words = ["apple", "banana", "cherry", "kiwi"]
word_lengths = {len(word) for word in words}
print(word_lengths) # Wynik: {4, 5, 6}

#Dictionary Comprehensions
# Utwórz słownik, gdzie kluczem jest słowo, a wartością jego długość
word_length_dict = {word: len(word) for word in words}
print(word_length_dict) # Wynik: {'apple': 5, 'banana': 6, 'cherry': 6, 'kiwi': 4}

#Zagnieżdżone listy
nested_list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]

]

# Utworzenie jednowymiarowej listy liczb - zagnieżdzona lista
flattened_list = [number for row in nested_list for number in row]
print(flattened_list) # Wynik: [1, 2, 3, 4, 5, 6, 7, 8, 9]

#Zgniedżone comprehensions z warunkami
nested_dict = {
    "fruits": {"apple": 3, "banana": 4, "cherry": 5},
    "vegetables": {"carrot": 7, "broccoli": 2, "cabbage": 6}
}

# Utwórz nowy słownik, który zawiera tylko te produkty, których liczba jest większa niż 4
filtered_dict = {category: {item: count for item, count in items.items() if count > 4} for category, items in nested_dict.items()}
print(filtered_dict) # Wynik: {'fruits': {'cherry': 5}, 'vegetables': {'cabbage': 6}}

# Zadanie
students = [("Ania", 3.5), ("Kamil", 4.5), ("Ola", 4.0), ("Piotr", 5.0), ("Ewa", 3.0)]
filtred_students = {category: item: count for item, count in item. items()
if count > 4.0} for category, item in students()}
print(filtred_students)

name_length_dict = {name:len(name) for name in names}
print(name_length_dict)




