#read the text files
#check if its a new line
# if its not a new line add the current vakue to the largest value

inputs = open('input.txt').readlines()

lists = [ el for idx,el in enumerate(inputs) if el!='\r\n' ]


def calculate_largest(inp, elem_to_sum):
    sums = []
    current_sum = 0
    for value in inp:

        if value == '\n':
            sums.append(current_sum)
            current_sum = 0
        else:
            current_sum = current_sum + int(value)
   
    return sorted(sums)[elem_to_sum:]


    
if __name__ == '__main__':
    print(sum(calculate_largest(inputs,-3)))

