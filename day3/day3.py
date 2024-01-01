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
        print(digit_index_arr)
        return digit_index_arr

def check_adjacent(line, start, end):
    symbol = """!@#$%^&*()-+?_=,<>/"""
    if start-1 < 0:
        for ele in line[start: end+2]:
            if ele in symbol:
                return True
    else:
        for ele in line[start-1: end+2]:
            if ele in symbol:
                return True
    return False

with open('input3.txt', 'r') as file:
    lines = file.readlines()
    answer = []
    # check every line together with its adjacent line/s
    # check every number in the line
    # if any adjacent character is a symbol add to the answer
    index = 0
    while(index < len(lines)):
        # extract the numbers in the curr_line first
        curr_line = lines[index]
        curr_digits = digit_search(curr_line)
        if index == 0:
            # first line, chekc only the next line
            next_line = lines[index+1]
            # check adjacent here
            for digit_indexes in curr_digits:
                start = int(digit_indexes[0])
                end = int(digit_indexes[1])
                if check_adjacent(curr_line, start, end) or check_adjacent(next_line, start, end):
                    answer.append(int(curr_line[start: int(end)+1]))
        elif index == len(lines) - 1:
            # check only the previous line
            prev_line = lines[index - 1]
            # check adjacent here
            for digit_indexes in curr_digits:
                start = int(digit_indexes[0])
                end = int(digit_indexes[1])
                if check_adjacent(curr_line, start, end) or check_adjacent(prev_line, start, end):
                    answer.append(int(curr_line[start: int(end)+1]))
        else:
            # check both
            next_line = lines[index+1]
            prev_line = lines[index - 1]
            # check adjacent here
            for digit_indexes in curr_digits:
                start = int(digit_indexes[0])
                end = int(digit_indexes[1])
                if check_adjacent(curr_line, start, end) or check_adjacent(prev_line, start, end) or check_adjacent(next_line, start, end):
                    answer.append(int(curr_line[start: int(end)+1]))
        index += 1
    result = 0
    for ele in answer:
        result += ele
    print(result)