# Shift Reduce Parser (Simple Version)

stack = []
input_string = input("Enter input string: ") + "$"

print("\nStack\tInput\tAction")

i = 0

while True:
    # Shift
    if i < len(input_string):
        stack.append(input_string[i])
        i += 1
        print("".join(stack), "\t", input_string[i:], "\tShift")

    # Reduce rule (example: E -> id)
    if "".join(stack[-2:]) == "id":
        stack = stack[:-2]
        stack.append("E")
        print("".join(stack), "\t", input_string[i:], "\tReduce E->id")

    # Accept condition
    if "".join(stack) == "E" and input_string[i:] == "$":
        print("Accepted")
        break

    # Break condition
    if i >= len(input_string):
        break