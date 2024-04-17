import tkinter as tk
from tkinter import messagebox

def are_numbers(values):
    for value in values:
        if not value.isdigit():
            return False
    return True

def create_relation_matrix(set_A, set_B):
    matrix = []
    for a in set_A:
        row = []
        for b in set_B:
            if a + b <= 5:
                row.append(1)
            else:
                row.append(0)
        matrix.append(row)
    return matrix

def create_matrix():
    set_A_values = entry_set_A.get().split()
    set_B_values = entry_set_B.get().split()

    if not set_A_values or not set_B_values:
        messagebox.showerror("Помилка", "Множини не можуть бути пустими.")
        return

    if len(set_A_values) != len(set(set_A_values)) or len(set_B_values) != len(set(set_B_values)):
        messagebox.showerror("Помилка", "Множини повинні вводитися через пробіл та без повторень.")
        return

    if not are_numbers(set_A_values) or not are_numbers(set_B_values):
        messagebox.showerror("Помилка", "Множини повинні складатися лише з чисел.")
        return

    set_A = [int(value) for value in set_A_values]
    set_B = [int(value) for value in set_B_values]

    relation_matrix = create_relation_matrix(set_A, set_B)

    for widget in frame_matrix.winfo_children():
        widget.destroy()

    for i, row in enumerate(relation_matrix):
        for j, value in enumerate(row):
            label = tk.Label(frame_matrix, text=str(value))
            label.grid(row=i, column=j)

root = tk.Tk()
root.title("Створення матриці відношення")

label_set_A = tk.Label(root, text="Множина A:")
label_set_A.grid(row=0, column=0, padx=5, pady=5)

entry_set_A = tk.Entry(root)
entry_set_A.grid(row=0, column=1, padx=5, pady=5)

label_set_B = tk.Label(root, text="Множина B:")
label_set_B.grid(row=1, column=0, padx=5, pady=5)

entry_set_B = tk.Entry(root)
entry_set_B.grid(row=1, column=1, padx=5, pady=5)

button_create_matrix = tk.Button(root, text="Створити матрицю", command=create_matrix)
button_create_matrix.grid(row=2, columnspan=2, padx=5, pady=5)

frame_matrix = tk.Frame(root)
frame_matrix.grid(row=3, columnspan=2, padx=5, pady=5)

root.mainloop()
