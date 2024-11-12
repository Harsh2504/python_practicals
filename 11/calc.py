import tkinter as tk

# Function to handle button clicks
def button_click(number):
    current = entry_field.get()
    entry_field.delete(0, tk.END)
    entry_field.insert(0, current + str(number))

# Function to handle clear button
def button_clear():
    entry_field.delete(0, tk.END)

# Function to handle equal button
def button_equal():
    try:
        result = eval(entry_field.get())
        entry_field.delete(0, tk.END)
        entry_field.insert(0, str(result))
    except:
        entry_field.delete(0, tk.END)
        entry_field.insert(0, "Error")

# Create main Tkinter window
root = tk.Tk()
root.title("Advanced Calculator")

# Entry field to display numbers and results
entry_field = tk.Entry(root, width=20, font=('Arial', 18), borderwidth=2, relief="solid", justify='right')
entry_field.grid(row=0, column=0, columnspan=4, pady=10)

# Define the buttons and their grid positions
buttons = [
    ('C', 1, 0, 1, 1), ('/', 1, 1, 1, 1), ('*', 1, 2, 1, 1), ('-', 1, 3, 1, 1),
    ('7', 2, 0, 1, 1), ('8', 2, 1, 1, 1), ('9', 2, 2, 1, 1), ('+', 2, 3, 2, 1),
    ('4', 3, 0, 1, 1), ('5', 3, 1, 1, 1), ('6', 3, 2, 1, 1),
    ('1', 4, 0, 1, 1), ('2', 4, 1, 1, 1), ('3', 4, 2, 1, 1), ('=', 4, 3, 2, 1),
    ('0', 5, 0, 1, 2), ('.', 5, 2, 1, 1)
]

# Create and place buttons using the grid layout with rowspan and colspan as needed
for (text, row, col, rowspan, colspan) in buttons:
    button = tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 14),
                       command=lambda t=text: button_click(t) if t not in ['C', '=', '+', '-'] else (
                           button_clear() if t == 'C' else button_equal() if t == '=' else button_click(t)))
    button.grid(row=row, column=col, rowspan=rowspan, columnspan=colspan, sticky="nsew", padx=5, pady=5)

# Configure the grid to expand and scale with window resizing
for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for j in range(4):
    root.grid_columnconfigure(j, weight=1)

# Run the Tkinter main loop
root.mainloop()
     