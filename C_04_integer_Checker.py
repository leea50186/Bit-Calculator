# Ask user for width and loop until they
# enter a number that is more than zero
def int_check(question, low):

    error = f"Please enter a number that is more than zero or equal to {low}\n"
    while True:

        try:
            # ask the user for a number
            response = int(input(question))

            # check that the number is more the zero
            if response >= low:
                   return response
            else:
                print(error)

        except ValueError :
            print(error)

# Main Routine Goes Here
for item in range(0, 2):
    integer = int_check("integer: ", 0 )
    print(integer)

print()

for item in range(0, 2):
    height = int_check("Height: ", 1)
    print(height)

print()

for item in range(0, 2):
    width = int_check("Width: ", 1)
    print(width)