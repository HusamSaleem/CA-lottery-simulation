from scraper import get_winning_nums
from simulation import Simulation
from ticket import Ticket
from datetime import date
import sys

def print_options_one():
    print("--------------------------------")
    print("0. Quit")
    print("1. Run Powerball simulation")
    print("2. Run SuperLotto simulation")
    print("3. Run Mega Millions simulation")
    print("--------------------------------")

def print_options_two():
    print("--------------------------------")
    print("0. Go Back")
    print("1. Run simulation until a jackpot is found (May take a very long time)")
    print("2. Run 'n' times (Generate only n tickets)")
    print("--------------------------------")

def handle_user_input():
    user_input = int(input("Enter your option as a number: "))
     
    if (user_input == 0):
        print("Exiting program...")
        sys.exit()
    
    ticket_type = user_input
    if (ticket_type != 1 and ticket_type != 2 and ticket_type != 3):
        print("Please enter a valid number")
        print_options_one()
        handle_user_input()
        return

    if (ticket_type == 1):
        ticket_type = "Powerball"
    elif (ticket_type == 2):
         ticket_type = "Superball"
    else:
        ticket_type = "Megaball"

    print_options_two()
    user_input = int(input("Enter your option as a number: "))
    
    if (user_input == 0):
        print_options_one()
        handle_user_input()
        return
    
    simulation_type = user_input
    while (simulation_type != 1 and simulation_type != 2):
        print("Invalid number")
        print_options_two()
        simulation_type = int(input("Enter your option as a number: "))

        if (simulation_type == 0):
            print_options_one()
            handle_user_input()
            return
    
    # Choose how many times to execute
    num_of_times_to_execute = 0
    if (simulation_type == 2):
        while (num_of_times_to_execute <= 0):
            num_of_times_to_execute = int(input("Enter how many tickets to simulate (1-n): "))
    
    verbose_option = input("Do you want to see what is happening during the simulation? (Y/N): ")
    while (verbose_option.lower() != "y" and verbose_option.lower() != "n"):
        verbose_option = input("Do you want to see what is happening during the simulation? (Y/N): ")

    verbose_option = True if verbose_option.lower() == "y" else False
    simulation = Simulation(ticket_type, num_of_times_to_execute, winning_tickets, verbose_option)
    simulation.run_simulation()

if __name__ == "__main__":
    # Web scrape the CA Lottery website for drawings
    global winning_tickets
    winning_tickets = get_winning_nums()

    print("--------------------------------")
    print("The winning numbers for:", date.today())
    print()
    for ticket in winning_tickets:
        ticket.to_string()
    print("--------------------------------")

    print_options_one()
    handle_user_input()