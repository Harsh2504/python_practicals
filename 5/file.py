print("--------------------------Student Data Management---------------------")

def initialize_database():
    try:
        with open("database.txt", "r") as file:
            print("Database found")
    except:
        with open("database.txt", "w") as file:
            print("Database created")

def add_student():
    roll = int(input("Enter Roll Number: "))
    name = input("Enter Name: ")
    marks = int(input("Enter Marks: "))
    with open("database.txt", "a") as file:
        file.write(f"{roll},{name},{marks}\n")
    print("Student added successfully")

def show_student():
    try:
        with open("database.txt", "r") as file:
            data = file.read()
            print(data)
    except FileNotFoundError:
        print("No database found. Please add a student first.")

def delete_student():
    roll = int(input("Enter Roll Number to delete: "))
    try:
        with open("database.txt", "r") as file:
            lines = file.readlines()
        with open("database.txt", "w") as file:
            for line in lines:
                if not line.startswith(f"{roll},"):
                    file.write(line)
        print("Student deleted successfully")
    except:
        print("No database found. Please add a student first.")

def update_student():
    roll = int(input("Enter Roll Number to update: "))
    name = input("Enter new Name: ")
    marks = int(input("Enter new Marks: "))
    try:
        with open("database.txt", "r") as file:
            lines = file.readlines()
        with open("database.txt", "w") as file:
            for line in lines:
                if line.startswith(f"{roll},"):
                    file.write(f"{roll},{name},{marks}\n")
                else:
                    file.write(line)
        print("Student updated successfully")
    except:
        print("No database found. Please add a student first.")

def search_student():
    roll = int(input("Enter Roll Number to search: "))
    try:
        with open("database.txt", "r") as file:
            found = False
            for line in file:
                if line.startswith(f"{roll},"):
                    print(line.strip())
                    found = True
                    break
            if not found:
                print("Student not found")
    except:
        print("No database found. Please add a student first.")

def main():
    initialize_database()
    while True:
        print()
        print("1. Add Student")
        print("2. Show Students")
        print("3. Delete Student")
        print("4. Update Student")
        print("5. Search Student")
        print("6. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            add_student()
        elif choice == 2:
            show_student()
        elif choice == 3:
            delete_student()
        elif choice == 4:
            update_student()
        elif choice == 5:
            search_student()
        elif choice == 6:
            break
        else:
            print("Invalid Choice")

if __name__ == "__main__":
    main()