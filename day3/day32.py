# look for the *
# check the adjacent box
# add two numbers
def digit_search(line):
        digit_start = False
        digit_start_index = 0
        digit_index_arr = []
        for i in range(len(line)):
            if digit_start: 
                if not line[i].isalnum():
                    # digit end
                    digit_start = False
                    digit_index_arr.append((digit_start_index, i-1))
            else:
                if line[i].isdigit():
                    digit_start = True
                    digit_start_index = i
        return digit_index_arr

def asterisk_search(line):
    stars = []
    for i in range(len(line)):
        if line[i] == '*':
            stars.append(i)
    return stars

def get_adjacent_number(digits_index, index):
    # we will use filter 
    # we can also use interval comparison
    return list(filter(lambda x: x[0]-1 <= index <= x[1]+1, digits_index))

def tuples_to_numbers(tuples, line):
    numbers = []
    for tuple in tuples:
        numbers.append(int(line[tuple[0]:tuple[1]+1]))       
    return numbers

def unpack(list_of_lists_of_tuples):
    answer = []
    for x in list_of_lists_of_tuples:
        if x:
            # only non-empty lists
            for y in x:
                answer.append(y)
    return answer

with open('3.txt', 'r') as file:
    lines = file.readlines()
    answer = 0
    index = 0
    while(index<len(lines)):
        curr_line = lines[index]
        adjacent_numbers = []
        curr_asterisks = asterisk_search(curr_line)
        if index == 0:
            #first line, check only the next line
            next_line = lines[index+1]
            curr_adjacent_digits = []
            next_adjacent_digits = []
            if curr_asterisks:
                for gear_index in curr_asterisks:
                    curr_adjacent_digits.append(get_adjacent_number(digit_search(curr_line), gear_index))
                    next_adjacent_digits.append(get_adjacent_number(digit_search(next_line), gear_index))
                # now join those lists, eliminate the empty lists inside and count the number
                combined = unpack(curr_adjacent_digits) + unpack(next_adjacent_digits)
                # count number of adjacent digits total
                if len(combined) == 2:
                    a = tuples_to_numbers(unpack(curr_adjacent_digits), curr_line)
                    c = tuples_to_numbers(unpack(next_adjacent_digits), next_line)
                    gears = a+c
                    print(gears)
                    gear_ratio = 1
                    for gear in gears:
                        gear_ratio = gear_ratio * gear
                    answer += gear_ratio
        elif index == len(lines) - 1:
            # last line, check only the previous line
            prev_line = lines[index-1]
            curr_adjacent_digits = []
            prev_adjacent_digits = []
            if curr_asterisks:
                for gear_index in curr_asterisks:
                    curr_adjacent_digits.append(get_adjacent_number(digit_search(curr_line), gear_index))
                    prev_adjacent_digits.append(get_adjacent_number(digit_search(prev_line), gear_index))
                # now join those lists, eliminate the empty lists inside and count the number
                combined = unpack(prev_adjacent_digits) + unpack(curr_adjacent_digits)
                # count number of adjacent digits total
                if len(combined) == 2:
                    a = tuples_to_numbers(unpack(curr_adjacent_digits), curr_line)
                    b = tuples_to_numbers(unpack(prev_adjacent_digits), prev_line)
                    gears = a+b
                    print(gears)
                    gear_ratio = 1
                    for gear in gears:
                        gear_ratio = gear_ratio * gear
                    answer += gear_ratio
        else: 
            # check both next and previous lines
            next_line = lines[index+1]
            prev_line = lines[index-1]
            curr_adjacent_digits = []
            next_adjacent_digits = []
            prev_adjacent_digits = []
            if curr_asterisks:
                for gear_index in curr_asterisks:
                    curr_adjacent_digits.append(get_adjacent_number(digit_search(curr_line), gear_index))
                    prev_adjacent_digits.append(get_adjacent_number(digit_search(prev_line), gear_index))
                    next_adjacent_digits.append(get_adjacent_number(digit_search(next_line), gear_index))
                # now join those lists, eliminate the empty lists inside and count the number
                combined = unpack(prev_adjacent_digits) + unpack(curr_adjacent_digits) + unpack(next_adjacent_digits)
                # count number of adjacent digits total
                if len(combined) == 2:
                    a = tuples_to_numbers(unpack(curr_adjacent_digits), curr_line)
                    b = tuples_to_numbers(unpack(prev_adjacent_digits), prev_line)
                    c = tuples_to_numbers(unpack(next_adjacent_digits), next_line)
                    gears = a+b+c
                    print(gears)
                    gear_ratio = 1
                    for gear in gears:
                        gear_ratio = gear_ratio * gear
                    answer += gear_ratio
        index += 1
    print(answer)