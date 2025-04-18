import sys

lst_in = [list(map(int, value.split())) for value in list(map(str.strip, sys.stdin.readlines()))]
senior_card = lst_in[0][0] - 1
first_player, second_player = lst_in[1], lst_in[2]

n = 0
len_first = len_second = int(lst_in[0][0] / 2)
while len_first != 0 and len_second != 0:
    if n >= 200_000:
        print('draw')
        break
    card_first, card_second = first_player[n], second_player[n]
    if card_first == 0 and card_second == senior_card:
        first_player.append(card_first)
        first_player.append(card_second)
        len_first += 1
        len_second -= 1
    elif card_second == 0 and card_first == senior_card:
        second_player.append(card_first)
        second_player.append(card_second)
        len_second += 1
        len_first -= 1
    elif card_first > card_second:
        first_player.append(card_first)
        first_player.append(card_second)
        len_first += 1
        len_second -= 1
    elif card_first < card_second:
        second_player.append(card_first)
        second_player.append(card_second)
        len_second += 1
        len_first -= 1

    n += 1

else:
    print('first' if len_first != 0 else 'second', n)
    