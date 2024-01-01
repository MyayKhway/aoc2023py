with open('input4.txt','r') as file:
    wins_by_card = {} 
    for line in file.readlines():
        lotto_card = list(map(lambda x:int(x), list(filter(lambda x: x!='', line.split('|')[0].split(':')[1].strip().split(' ')))))
        owned_card = list(map(lambda x:int(x), list(filter(lambda x:x!='', line.split('|')[1].split(' ')))))
        card_num = int(line.split('|')[0].split(':')[0].strip().split()[1])
        winining_numbers = []
        for number in owned_card:
            if number in lotto_card:
                winining_numbers.append(number)
        wins_by_card[card_num] = list(range(card_num+1,card_num+1+len(winining_numbers),))

# for each element of array in one wins_by_card value
def count(index):
    result = []
    if wins_by_card[index] == []:
        return []
    else:
        result += wins_by_card[index]
        for ele in wins_by_card[index]:
            result += count(ele)
        return result
answer = 0
for key,value in wins_by_card.items():
    answer += len(count(key))
print(answer+len(wins_by_card.keys()))
