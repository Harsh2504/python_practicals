import tkinter as tk
from tkinter import messagebox
import re

# Function to validate email
def validate_email(email):
    email_regex = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(email_regex, email)

# Function to handle submission
def submit_form():
    # Get values from entry fields
    name = name_entry.get()
    age = age_entry.get()
    course = course_entry.get()
    email = email_entry.get()
    
    # Check if all fields are filled
    if not name.isalpha():
        messagebox.showwarning("Invalid Input", "Name should contain only letters.")
    elif not course.isalpha():
        messagebox.showwarning("Invalid Input", "Course should contain only letters.")
    elif not age.isdigit():
        messagebox.showwarning("Invalid Input", "Age should contain only numbers.")
    elif not validate_email(email):
        messagebox.showwarning("Invalid Input", "Please enter a valid email address.")
    elif name and age and course and email:
        # Display success message with entered details
        success_message = f"Student Registered Successfully!\nName: {name} in {course} course."
        registration_label.config(text=success_message)
        
        # Clear the form fields
        name_entry.delete(0, tk.END)
        age_entry.delete(0, tk.END)
        course_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Incomplete Data", "Please fill all the fields.")

# Create main Tkinter window
root = tk.Tk()
root.title("Student Registration Form")
root.geometry("300x350")

# Heading Label
heading = tk.Label(root, text="Student Registration Form", font=("Arial", 14))
heading.pack(pady=10)

# Name field
tk.Label(root, text="Name").pack()
name_entry = tk.Entry(root, width=30)
name_entry.pack()

# Age field
tk.Label(root, text="Age").pack()
age_entry = tk.Entry(root, width=30)
age_entry.pack()

# Course field
tk.Label(root, text="Course").pack()
course_entry = tk.Entry(root, width=30)
course_entry.pack()

# Email field
tk.Label(root, text="Email").pack()
email_entry = tk.Entry(root, width=30)
email_entry.pack()

# Submit Button
submit_button = tk.Button(root, text="Submit", command=submit_form)
submit_button.pack(pady=10)

# Label to display registration success message
registration_label = tk.Label(root, text="", font=("Arial", 10), fg="green")
registration_label.pack(pady=10)

# Run the Tkinter main loop
root.mainloop()
