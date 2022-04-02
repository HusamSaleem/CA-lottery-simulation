import locale
from copy import copy
import random
locale.setlocale(locale.LC_ALL, 'en_US')

class Ticket:
    def __init__(self, ticket_name, special_name):
        self.name = ticket_name
        self.special_name = special_name
        self.nums = []
        self.special = 0
        self.winning_prizes = []

        # Cost per ticket in USD
        if (ticket_name == "Powerball" or ticket_name == "Megaball"):
            self.cost = 2
        elif (ticket_name == "Superball"):
            self.cost = 1
    
    def set_ticket_nums(self, nums):
        self.nums = nums
        self.special = self.nums[-1]
        self.nums = self.nums[0: 5]
    
    def copy_ticket(self, ticket):
        self.nums = copy(ticket.nums)
        self.special = ticket.special
        self.winning_prizes = ticket.winning_prizes
    
    def set_winning_prizes(self, winning_prizes):
        self.winning_prizes = winning_prizes

    def to_string(self):
        if (len(self.winning_prizes) != 0):
            print(self.name, self.nums, self.special, "\n\tJackpot prize: $", locale.format("%d", self.winning_prizes[-1], True))
        else:
            print(self.name, self.nums, self.special)

    def _generate_nums(self, nums_range, special_range):
        for i in range(5):
            self.nums.append(random.randint(1, nums_range))
        self.special = random.randint(1, special_range)

    # Generate a random ticket based on the ticket type
    def generate_ticket(self):
        if self.name == "Powerball":
            # Powerball -> 5 numbers between 1 and 69, power number between 1 and 26
            self._generate_nums(69, 26)
        elif self.name == "Superball":
            #SuperLotto -> 5 numbers between 1 and 47 and super number between 1 27
            self._generate_nums(47, 27)
        elif self.name == "Megaball":
            #Mega Millions -> 5 numbers between 1 and 70 and super number between 1 25
            self._generate_nums(70, 25)

    # Returns the amount of money that this ticket could have won and the amount of matching numbers
    # return[0] = number of matching numbers, return[1] = $
    # Refer to https://www.calottery.com/draw-games/powerball#section-content-1-3
    def calculate_prize(self, winning_nums, special_num) -> list[int]:
        special_matches = self.special == special_num
        matched_nums = 0
        temp_winning_nums = copy(winning_nums)

        for i in range(0, len(self.nums)):
            # Have a match
            if (self.nums[i] in temp_winning_nums):
                temp_winning_nums.remove(self.nums[i])
                matched_nums += 1
        
        if special_matches:
            if matched_nums == 5:
                return ["5 + " + self.name, self.winning_prizes[-1]] # Jackpot prize matched
            elif matched_nums == 4:
                return ["4 + " + self.name, self.winning_prizes[-3]] # 4 numbers + special matched
            elif matched_nums == 3:
                return ["3 + " + self.name, self.winning_prizes[-5]] # 3 numbers + special matched
            elif matched_nums == 2:
                return ["2 + " + self.name, self.winning_prizes[-7]] # 2 numbers + special matched
            elif matched_nums == 1:
                return ["1 + " + self.name, self.winning_prizes[-8]] # 1 numbers + special matched
            else:
                return [self.name, self.winning_prizes[0]] # special matched
        else:
            if matched_nums == 5:
                return ["5", self.winning_prizes[-2]] # 5 numbers matched
            elif matched_nums == 4:
                return ["4", self.winning_prizes[-4]] # 4 numbers matched
            elif matched_nums == 3:
                return ["3", self.winning_prizes[-6]] # 3 numbers matched
            else:
                return ["None", 0] # Losing ticket