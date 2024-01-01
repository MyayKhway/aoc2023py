with open('input2.txt', 'r') as file:
    ans = 0
    for line in file.readlines():
        # create a dict for each line 
        game_num = (line.split(':')[0]).split()[1]
        sets_data = list(map(lambda x: x.strip(), (line.split(':')[1]).split(';')))
        max_blue = 0
        max_red = 0
        max_green = 0
        for each_set in sets_data:
            # get the balls separately
            balls = list(map(lambda x: x.strip(), each_set.split(',')))
            blue = 0
            red = 0
            green = 0
            for ball in balls:
                if 'blue' in ball:
                    blue += int(ball.split()[0])
                if 'red' in ball:
                    red += int(ball.split()[0])
                if 'green' in ball:
                    green += int(ball.split()[0])
            if blue > max_blue:
                max_blue = blue
            if red > max_red:
                max_red = red
            if green > max_green:
                max_green = green
        power = max_blue * max_green * max_red
        ans += power
    print(ans)