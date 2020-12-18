from random import randint
class LotoCard:
    def __init__(self,player_name):
        self.player_name  = player_name
        self.form_card()
    def form_card(self):
        slot1 = randint(1, 90)
        slot2 = randint(1, 90)
        slot3 = randint(1, 90)
        slot4 = randint(1, 90)
        slot5 = randint(1, 90)
        slot6 = randint(1, 90)
        slot7 = randint(1, 90)
        slot8 = randint(1, 90)
        slot9 = randint(1, 90)
        slot10 = randint(1, 90)
        slot11 = randint(1, 90)
        slot12 = randint(1, 90)
        slot13 = randint(1, 90)
        slot14 = randint(1, 90)
        slot15 = randint(1, 90)
        player_layout = [slot1, slot2, slot3, slot4, slot5, slot6, slot7, slot8,
                       slot9, slot9, slot10, slot11, slot12, slot13, slot13, slot14, slot15]
        return player_layout
class LotoGame:
    def __init__(self,player_name,player2_name):
        self.player_name = player_name
        self.player2_card = player2_name
    def start(self,player_card,computer_card):
        f = ' '
        player_card = player_card
        computer_card = computer_card
        spaces_1 = [f * randint(0, 2),f * randint(0, 5),f * randint(0, 5),f * randint(0, 5),f * randint(0, 3),
                    f * randint(0, 3),f * randint(0, 3),f * randint(0, 3),f * randint(0, 3),f * randint(0, 3),
                    f * randint(0, 3),f * randint(0, 3),f * randint(0, 3),f * randint(0, 3),f * randint(0, 3)]
        spaces_2 = [f * randint(0, 2),f * randint(0, 5),f * randint(0, 5),f * randint(0, 5),f * randint(0, 3),
                    f * randint(0, 3),f * randint(0, 3),f * randint(0, 3),f * randint(0, 3),f * randint(0, 3),
                    f * randint(0, 3),f * randint(0, 3),f * randint(0, 3),f * randint(0, 3),f * randint(0, 3)]
        n = 2
        while  any(j.isdigit() for j in list(map(lambda x: str(x), computer_card))) == True or n > 0 == True:
            n -= 1
            winning = randint(1, 90)
            print(f'\nNumbers remaining: {n}')
            print(f'\nThe next number is: {winning}')
            print('-' * 40)
            print((f'Your card looks like \n '
                   f'{spaces_1[0]} {player_card[0]} {spaces_1[1]} {player_card[1]} '
                   f'{spaces_1[2]}  {player_card[2]} {spaces_1[3]} {player_card[3]} {spaces_1[4]} {player_card[4]} '
                   f'\n {spaces_1[5]} {player_card[5]} {spaces_1[6]} {player_card[6]} {spaces_1[7]} {player_card[7]} {spaces_1[8]} {player_card[8]} {spaces_1[9]} {player_card[9]} '
                   f'\n {spaces_1[10]} {player_card[10]} {spaces_1[11]} {player_card[11]} {spaces_1[12]} {player_card[12]} {spaces_1[13]} {player_card[13]} {spaces_1[14]} {player_card[14]}'))
            print('-' * 40)
            print((
                f'Computer card looks like \n'
                f'{spaces_2[0]} {computer_card[0]} {spaces_2[1]} {computer_card[1]} {spaces_2[2]}  {computer_card[2]} {spaces_2[3]} {computer_card[3]} {spaces_2[4]} {computer_card[4]}'
                f'\n {spaces_2[5]} {computer_card[5]} {spaces_2[6]} {computer_card[6]} {spaces_2[7]} {computer_card[7]} {spaces_2[8]} {computer_card[8]} {spaces_2[9]} {computer_card[9]} '
                f'\n {spaces_2[10]} {computer_card[10]} {spaces_2[11]} {computer_card[11]} {spaces_2[12]} {computer_card[12]} {spaces_2[13]} {computer_card[13]} {spaces_2[14]} {computer_card[14]} '))
            if winning in computer_card:
                for j, d in enumerate(computer_card):
                    if d == winning:
                        computer_card[j] = '-'
                    else:
                        pass
            l_string = str(input('\nDo you want to cross out a number y/n:'))
            if l_string == 'y':
                if winning in player_card:
                    for n, i in enumerate(player_card):
                        if i == winning:
                            player_card[n] = '-'
                        else:
                            pass
                else:
                    print('you lose')
                    break
            elif l_string == 'n':
                continue
        if any(j.isdigit() for j in list(map(lambda x: str(x), computer_card))) == False:
            print('Computer Wins')
        elif any(j.isdigit() for j in list(map(lambda x: str(x), player_card))) == False:
            print('Player Wins')
        return ''

loto_player = LotoCard('Player')
loto_player2 = LotoCard('Computer')
game  = LotoGame(loto_player.player_name,loto_player2)
print(game.start(loto_player.form_card(),loto_player2.form_card()))