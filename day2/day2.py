with open('input2.txt', 'r') as file:
    game_nums = []
    for line in file.readlines():
        # create a dict for each line 
        game_num = (line.split(':')[0]).split()[1]
        sets_data = list(map(lambda x: x.strip(), (line.split(':')[1]).split(';')))
        flag = False
        blue = 0
        red = 0
        green = 0
        for each_set in sets_data:
            # get the balls separately
            balls = list(map(lambda x: x.strip(), each_set.split(',')))
            for ball in balls:
                if 'blue' in ball:
                    blue += int(ball.split()[0])
                if 'red' in ball:
                    red += int(ball.split()[0])
                if 'green' in ball:
                    green += int(ball.split()[0])
            if blue > 14 or red > 12 or green > 13:
                game_nums.append(int(game_num))
    ga = list(set(game_nums))
    print(5050 - sum(ga))