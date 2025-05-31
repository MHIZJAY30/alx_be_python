# Prompt the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

#Ensure the input is a positive integer
if size > 0:

#Use a while loop to create rows
    row = 0
    while row < size:
            for col in range(size):
                print("*", end="")
            print()  # Move to the next line after each row
            row += 1

# except ValueError:
    print("Please enter a valid positive integer.")