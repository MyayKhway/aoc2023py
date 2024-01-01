with open('input1.txt', 'r') as file:
    sum = 0
    numbers =["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"] 
    for line in file.readlines():
        start_flag = True
        last_digit = -1
        s = ''
        i = 0
        while(i < len(line)):
            if start_flag:
                # no first digit yet
                if line[i].isdigit():
                    first_digit = line[i]
                    start_flag = False
                    i = i + 1 
                    continue
                elif line[i] in ['o', 't', 'f', 's', 'e', 'n']:
                    if line[i] == 'o':
                        # check for one
                        if i+2 < len(line)-1:
                            if line[i:i+3] in numbers:
                                first_digit = numbers.index(line[i:i+3]) + 1
                                start_flag = False
                                i = i + 3
                                continue
                    if line[i] == 't':
                        # check for two and three
                        if line[i:i+3] in numbers:
                            first_digit = numbers.index(line[i:i+3]) + 1
                            start_flag = False
                            i = i + 3
                            continue
                        if line[i:i+5] in numbers:
                            first_digit = numbers.index(line[i:i+5]) + 1
                            start_flag = False
                            i = i + 5
                            continue
                    if line[i] == 'f':
                        # check for four and five
                        if line[i:i+4] in numbers:
                            first_digit = numbers.index(line[i:i+4]) + 1
                            start_flag = False
                            i = i + 4
                            continue
                    if line[i] == 's':
                        # check for six and seven
                        if line[i:i+3] in numbers:
                            first_digit = numbers.index(line[i:i+3]) + 1
                            start_flag = False
                            i = i + 3
                            continue
                        if line[i:i+5] in numbers:
                            first_digit = numbers.index(line[i:i+5]) + 1
                            start_flag = False
                            i = i + 5
                            continue
                    if line[i] == 'e':
                        # check for eight
                        if line[i:i+5] in numbers:
                            first_digit = numbers.index(line[i:i+5]) + 1
                            start_flag = False
                            i = i + 5
                            continue
                    if line[i] == 'n':
                        # check for nine
                        if line[i:i+4] in numbers:
                            first_digit = numbers.index(line[i:i+4]) + 1
                            start_flag = False
                            i = i + 4
                            continue
            else:
                # the first digit has already been found
                if line[i].isdigit():
                    last_digit = line[i]
                    i = i + 1 
                    continue
                elif line[i] in ['o', 't', 'f', 's', 'e', 'n']:
                    if line[i] == 'o':
                        # check for one
                        if i+2 < len(line)-1:
                            if line[i:i+3] in numbers:
                                last_digit = numbers.index(line[i:i+3]) + 1
                                i = i + 3
                                continue
                    if line[i] == 't':
                        # check for two and three
                        if line[i:i+3] in numbers:
                            last_digit = numbers.index(line[i:i+3]) + 1
                            i = i + 3
                            continue
                        if line[i:i+5] in numbers:
                            last_digit = numbers.index(line[i:i+5]) + 1
                            i = i + 5
                            continue
                    if line[i] == 'f':
                        # check for four and five
                        if line[i:i+4] in numbers:
                            last_digit = numbers.index(line[i:i+4]) + 1
                            i = i + 4
                            continue
                    if line[i] == 's':
                        # check for six and seven
                        if line[i:i+3] in numbers:
                            last_digit = numbers.index(line[i:i+3]) + 1
                            i = i + 3
                            continue
                        if line[i:i+5] in numbers:
                            last_digit = numbers.index(line[i:i+5]) + 1
                            i = i + 5
                            continue
                    if line[i] == 'e':
                        # check for eight
                        if line[i:i+5] in numbers:
                            last_digit = numbers.index(line[i:i+5]) + 1
                            i = i + 5
                            continue
                    if line[i] == 'n':
                        # check for nine
                        if line[i:i+4] in numbers:
                            last_digit = numbers.index(line[i:i+4]) + 1
                            i = i + 4
                            continue
            i += 1
        if last_digit == -1:
            value = (int(first_digit) * 10) + int(first_digit)
        else:
            value = (int(first_digit) * 10) + int(last_digit)
        sum += value
print(sum)