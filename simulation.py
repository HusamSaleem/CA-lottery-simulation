import locale
from columnar import columnar
from ticket import Ticket
locale.setlocale(locale.LC_ALL, 'en_US')

class Simulation:
    def __init__(self, ticket_name, ticket_type, num_of_times_to_execute, winning_tickets, verbose):
        self.ticket_name = ticket_name
        self.ticket_type = ticket_type
        self.num_of_times_to_execute = num_of_times_to_execute
        self.winning_tickets = winning_tickets
        self.verbose = verbose
        
        # Dictionary that tracks the number of tickets per match
        self.detailed_winning_result = {
            "None" : 0,
            ticket_type : 0, 
            "1 + " + ticket_type : 0,
            "2 + " + ticket_type : 0,
            "3" : 0,
            "3 + " + ticket_type : 0,
            "4" : 0,
            "4 + " + ticket_type : 0,
            "5" : 0,
            "5 + " + ticket_type : 0}

    def _get_winning_ticket(self) -> Ticket:
        if (self.ticket_type == "Powerball"):
            return self.winning_tickets[0]
        elif (self.ticket_type == "Superball"):
            return self.winning_tickets[1]
        else:
            return self.winning_tickets[2]
    
    def __get_winning_prizes(self) -> list[int]:
        if (self.ticket_type == "Powerball"):
            return self.winning_tickets[0].winning_prizes
        elif (self.ticket_type == "Superball"):
            return self.winning_tickets[1].winning_prizes
        else:
            return self.winning_tickets[2].winning_prizes

    def _generate_random_ticket(self) -> Ticket:
        ticket = Ticket(self.ticket_type, self.ticket_name)
        ticket.generate_ticket()
        return ticket
    
    def _print_final_report(self, money_spent, money_gained, number_of_tickets_generated):
        money_lost = money_spent - money_gained
        # General statistics
        general_stats = "================================================================\n"
        general_stats += "Total number of tickets generated: {:,}\n".format(number_of_tickets_generated)
        general_stats += "Total money spent: ${:,.2f}\n".format(money_spent)
        general_stats += "Total money gained: ${:,.2f}\n".format(money_gained)
        general_stats += "Total money lost: ${:,.2f}\n".format(money_lost)
        general_stats += "================================================================"

        # Winning ticket number statistics
        # Calculate frequencies
        # Also calculate prize money gained per match type
        winning_prizes = self.__get_winning_prizes()
        headers = ["Matches", "Tickets", "Frequency", "Prize money per ticket", "Prize money collected"]
        data = []
        for i, (key, value) in enumerate(self.detailed_winning_result.items()):
            frequency = (float(value) / number_of_tickets_generated) * 100
            
            if (key == "None"):
                data.append([key, "{:,}".format(value), "{:.4f}%".format(frequency), "${:,}".format(0), "${:,}".format(0)])
            else:
                prize = winning_prizes[i - 1]
                prize_money_collected = prize * value
                data.append([key, "{:,}".format(value), "{:.4f}%".format(frequency), "${:,}".format(prize), "${:,}".format(prize_money_collected)])
        
        table = columnar(data, headers, no_borders=False) # Make a table using columnar
        print(general_stats)
        print(table)

    # TODO: replace with non-deprecated code
    def _print_statistics(self, money_spent, money_gained, number_of_tickets_generated):
        # For cursor positions
        UP = "\x1B[6A"
        CLR = "\x1B[0K"

        # Formatting
        number_of_tickets_generated = locale.format("%d", number_of_tickets_generated, True)
        money_lost = money_spent - money_gained
        money_spent = locale.format("%d", money_spent, True)
        money_gained = locale.format("%d", money_gained, True)
        money_lost = locale.format("%d", money_lost, True)

        print(f"{UP}Total number of tickets generated: {number_of_tickets_generated}\nTotal money spent ${money_spent}\nTotal money gained ${money_gained}\nTotal money lost ${money_lost}\nTickets that have matches: {self.detailed_winning_result}\n{CLR}")
    
    def run_simulation(self):
        money_spent = 0
        money_gained = 0
        number_of_tickets_generated = 0
        winning_ticket = self._get_winning_ticket()

        print("\n\n\n\n\n\n")

        # If num_of_times_to_execute = 0, then execute infinitely until we find a jackpot
        while True:
            ticket = self._generate_random_ticket()
            ticket.set_winning_prizes(winning_ticket.winning_prizes)
            result = ticket.calculate_prize(winning_ticket.nums, winning_ticket.special)

            # General statistics
            money_gained += result[1]
            money_spent += ticket.cost
            number_of_tickets_generated += 1
            self.detailed_winning_result[result[0]] += 1

            if (self.verbose):
                self._print_statistics(money_spent, money_gained, number_of_tickets_generated)

            # Found a jackpot
            if (result[0] == "5 + " + self.ticket_type):
                print("JACKPOT!!!")
                print("Winning ticket was:", ticket.nums, ticket.special)
                break
        
            # Break when the # of generated tickets reached the maximum number of tickets we can genreate
            if (number_of_tickets_generated == self.num_of_times_to_execute):
                break
        
        self._print_final_report(money_spent, money_gained, number_of_tickets_generated)
        print("Simulation completed!")