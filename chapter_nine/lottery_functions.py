from random import choice


class Lottery:

    def generate_lottery_ticket( possibilities):
        generated_ticket = []
        while len(generated_ticket) < 4:
            pulled_item = choice(possibilities)
            if pulled_item not in generated_ticket:
                generated_ticket.append(pulled_item)
        return generated_ticket

    def check_winner(possible_winner, random_ticket):
        for number in random_ticket:
            if number not in possible_winner:
                return False

        return True
