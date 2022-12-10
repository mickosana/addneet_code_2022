#read the text files
#check if its a new line
# if its not a new line add the current vakue to the largest value

inputs = open('input.txt').readlines()



def calculate_largest(inp):
    largest_sum = 0
    current_sum = 0
    for idx, value in enumerate(inputs):

        print(f"overrall largest {largest_sum}")
        print(f"current largest {current_sum}")
        if value == '\n':
            print("reseting")
            if  current_sum > largest_sum:
                largest_sum = current_sum
            current_sum = 0
        else:
            print(f"this is not an blank")
            current_sum = current_sum + int(value)

    return largest_sum
    
print(calculate_largest(inputs))

