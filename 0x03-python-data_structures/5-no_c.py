#!/usr/bin/python3
def no_c(my_string):
    # Initialize an empty string to store the result
    result = ""

    # Iterate through each character in the input string
    for char in my_string:
        # Check if the current character is 'c' or 'C'
        if char != 'c' and char != 'C':
            # If not 'c' or 'C', add it to the result string
            result += char

    # Return the result string without 'c' and 'C'
    return result

# Test the function with your examples
if __name__ == "__main__":
    print(no_c("Best School"))
    print(no_c("Chicago"))
    print(no_c("C is fun!"))
