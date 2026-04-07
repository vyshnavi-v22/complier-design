# Stack Allocation Implementation

stack = []

def push(item):
    stack.append(item)
    print(f"Pushed: {item}")

def pop():
    if not stack:
        print("Stack is empty")
    else:
        item = stack.pop()
        print(f"Popped: {item}")

def display():
    print("Stack:", stack)


while True:
    print("\n1. Push\n2. Pop\n3. Display\n4. Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        val = input("Enter value: ")
        push(val)

    elif choice == 2:
        pop()

    elif choice == 3:
        display()

    elif choice == 4:
        break

    else:
        print("Invalid choice")