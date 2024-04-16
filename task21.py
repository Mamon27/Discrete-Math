import tkinter as tk
from tkinter import messagebox

def validate_input(input_string):
    """Перевірка правильності формату введення"""
    try:
        set(map(int, input_string.split()))
        return True
    except ValueError:
        return False

def union():
    """Об'єднання множин"""
    if validate_input(entry_set1.get()) and validate_input(entry_set2.get()):
        set1 = set(map(int, entry_set1.get().split()))
        set2 = set(map(int, entry_set2.get().split()))
        result = set1.union(set2)
        messagebox.showinfo("Результат", f"Об'єднання множин: {result}")
    else:
        messagebox.showerror("Помилка", "Поля множин повинні бути введені числами через пробіл.")

def intersection():
    """Перетин множин"""
    if validate_input(entry_set1.get()) and validate_input(entry_set2.get()):
        set1 = set(map(int, entry_set1.get().split()))
        set2 = set(map(int, entry_set2.get().split()))
        result = set1.intersection(set2)
        messagebox.showinfo("Результат", f"Перетин множин: {result}")
    else:
        messagebox.showerror("Помилка", "Поля множин повинні бути введені числами через пробіл.")

def difference():
    """Різниця множин"""
    if validate_input(entry_set1.get()) and validate_input(entry_set2.get()):
        set1 = set(map(int, entry_set1.get().split()))
        set2 = set(map(int, entry_set2.get().split()))
        result = set1.difference(set2)
        messagebox.showinfo("Результат", f"Різниця множин: {result}")
    else:
        messagebox.showerror("Помилка", "Поля множин повинні бути введені числами через пробіл.")

def symmetric_difference():
    """Симетрична різниця множин"""
    if validate_input(entry_set1.get()) and validate_input(entry_set2.get()):
        set1 = set(map(int, entry_set1.get().split()))
        set2 = set(map(int, entry_set2.get().split()))
        result = set1.symmetric_difference(set2)
        messagebox.showinfo("Результат", f"Симетрична різниця множин: {result}")
    else:
        messagebox.showerror("Помилка", "Поля множин повинні бути введені числами через пробіл.")

# Створення графічного інтерфейсу
root = tk.Tk()
root.title("Операції теорії множин")

# Поля для вводу множин
label_set1 = tk.Label(root, text="Множина 1:")
label_set1.grid(row=0, column=0, padx=10, pady=5, sticky="e")
entry_set1 = tk.Entry(root)
entry_set1.grid(row=0, column=1, padx=10, pady=5)

label_set2 = tk.Label(root, text="Множина 2:")
label_set2.grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry_set2 = tk.Entry(root)
entry_set2.grid(row=1, column=1, padx=10, pady=5)

# Кнопки для виконання операцій
button_union = tk.Button(root, text="Об'єднання", command=union)
button_union.grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky="we")

button_intersection = tk.Button(root, text="Перетин", command=intersection)
button_intersection.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky="we")

button_difference = tk.Button(root, text="Різниця", command=difference)
button_difference.grid(row=4, column=0, columnspan=2, padx=10, pady=5, sticky="we")

button_symmetric_difference = tk.Button(root, text="Симетрична різниця", command=symmetric_difference)
button_symmetric_difference.grid(row=5, column=0, columnspan=2, padx=10, pady=5, sticky="we")

root.mainloop()
