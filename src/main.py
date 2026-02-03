# Project Z - Hospital Queue System (Version 1)

queue = []


def add_patient():
    name = input("Enter patient name: ")
    queue.append(name)
    print(f"{name} added to queue.")


def call_next():
    if len(queue) == 0:
        print("No patients in queue.")
    else:
        patient = queue.pop(0)
        print(f"Now serving: {patient}")


def show_queue():
    if len(queue) == 0:
        print("Queue is empty.")
    else:
        print("Current queue:")
        for i, name in enumerate(queue, start=1):
            print(i, name)


while True:
    print("\n--- Hospital Queue Menu ---")
    print("1. Add patient")
    print("2. Call next patient")
    print("3. Show queue")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_patient()
    elif choice == "2":
        call_next()
    elif choice == "3":
        show_queue()
    elif choice == "4":
        print("Exiting...")
        break
    else:
        print("Invalid choice")

