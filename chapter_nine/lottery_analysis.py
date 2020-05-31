"""
 You can use a loop to see how hard it might be to win the kind of lottery you just modeled.
 Make a list or tuple called my_ticket.
 Write a loop that keeps pulling numbers until your ticket wins.
 Print a message reporting how many times the loop had to run to give you a winning ticket.
"""

from chapter_nine.lottery_functions import Lottery

combination = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 'a', 'b', 'c', 'd', 'e')
winning_ticket = Lottery.generate_lottery_ticket(combination)
win = False
count = 0

while not win:
    lottery_ticket = Lottery.generate_lottery_ticket(combination)
    win = Lottery.check_winner(possible_winner=winning_ticket, random_ticket=lottery_ticket)
    count += 1
    if count >= 1000000:
        break

if win:
    print(f'We have a winner!')
    print(f'{winning_ticket} is the winning ticket')
    print(f'{lottery_ticket} owner of this ticket, won')
    print(f'It took only {count} counts to find a winner')

else:
    print(f'We have no winner!')
    print(f'{winning_ticket} is the winning ticket')
    print(f'It took {count} count but we could not found a winner')
