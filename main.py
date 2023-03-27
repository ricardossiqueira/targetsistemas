# 2)
# Given a certain number calculate the fibonnaci sequence up to that number and
# returns a message if the number belongs or not to the sequence
# @param number
# @return string
def fibonnaci(number):
    if number == 0 or number == 1:
        return f"The number {number} belongs to the sequence"
    else:
        # initialize the sequence
        sequence = [0, 1]
        # loop through the sequence
        for i in range(2, number):
            # append the next number to the sequence
            sequence.append(sequence[i-1] + sequence[i-2])
        # check if the number belongs to the sequence
        if number in sequence:
            return f"The number {number} belongs to the sequence"
        else:
            return f"The number {number} does not belong to the sequence"

# 5)
# Given a certain string return it's inverse
# @param string
# @return string
def inverse(string):
    # initialize the inverse string
    inverse = ""
    # loop through the string
    for i in range(len(string)):
        # append the last character to the inverse string
        inverse += string[len(string) - i - 1]
    # print the inverse string
    return inverse

