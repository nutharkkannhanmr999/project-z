# Project Z – Hospital Queue System (Version 2 – class based)

class HospitalQueue:

    def __init__(self):
        self.queue = []

    def add_patient(self):
        name = input("Enter patient name: ")
        self.queue.append(name)
        print(f"{name} added to queue.")

    def call_next(self):
        if len(self.queue) == 0:
            print("No patients in queue.")
        else:
            patient = self.queue.pop(0)
            print(f"Now serving: {patient}")

    def show_queue(self):
        if len(self.queue) == 0:
            print("Queue is empty.")
        else:
            print("Current queue:")
            for i, name in enumerate(self.queue, start=1):
                print(i, name)


def main():
    system = HospitalQueue()

    while True:
        print("\n--- Hospital Queue Menu ---")
        print("1. Add patient")
        print("2. Call next patient")
        print("3. Show queue")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            system.add_patient()
        elif choice == "2":
            system.call_next()
        elif choice == "3":
            system.show_queue()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()