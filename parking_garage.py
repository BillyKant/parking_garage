class Parking_Garage():

    def __init__(self) -> None:
        self.tickets = ['1','2','3','4','5','6','7','8','9','10']
        self.parking_spaces = ["1","2","3","4","5","6","7","8"," 9","10"]# We didn't need to use this for our code...
        self.current_ticket = {}
        self.first_call = True
        self.ticket_price = ["$1,000", "Visa", "MasterCard", "American Express", "Run the gate"] 

    def take_ticket(self):
        if self.tickets:
        #1st ticket needs to leave self.tickets % assign to self.current_ticket
            ticket_num = self.tickets.pop(0)
            self.current_ticket[ticket_num] = ''
            print(f'\nYour ticket number is: {ticket_num}')
        #2Remove corresponding ticket value from parking_spaces
        else:
            print('\nSorry no spaces are available... ')

    def pay_for_parking(self,leaving=False):
        #1: User input selects what ticket to pay for in current_ticket | List current tickets
        ticket_pay = input(f"""\n 
        --- Which ticket are you paying for?---
        {self.current_ticket}\n
        """)
        

        #2: Have user enter an input to pay for a ticket
        if ticket_pay in self.current_ticket:
            if self.current_ticket[ticket_pay] == '':
                print("\nYour ticket costs $1,000")
                print("\nWe accept cash or credit/debit.")   
                while True:
                    confirm_pay = input("\nPlease enter your payment: ")
                    if confirm_pay in self.ticket_price:                    
                        #3: Update current_ticket value to True
                        self.current_ticket[ticket_pay] = confirm_pay
                        #4: Display that the user has paid, has 15 minutes to leave
                        if not leaving:
                            print("\nThank you for your payment, you have 15 minutes to leave.")
                        break                    
                    else:
                        print("\nInvalid payment, please try again.")

            else:
                print("\n You've already paid for this ticket")
        else:
            print("\nInvalid ticket. Please try again.")
        

    def leave_garage(self):
        
        ticket_leave = input("\nEnter ticket number: ")
        if ticket_leave in self.current_ticket:
            if self.current_ticket[ticket_leave] == True:
                #1 Add tickets back to tickets list
                self.tickets.append(ticket_leave)
                #2 Remove ticket from current_ticket
                del self.current_ticket[ticket_leave]
                print("\nThanks for visiting!")
            else:
                print("\nPlease pay your ticket.")
                self.pay_for_parking(True)
                #1 Add tickets back to tickets list
                self.tickets.append(ticket_leave)
                #2 Remove ticket from current_ticket
                del self.current_ticket[ticket_leave]
                print("\nThanks for visiting!")

        else:
            print("\nThis ticket does not exist. Please try again.")


    def run(self):
        enter = input("\n\nWould you like to enter the garage?\n\n['y', 'n'] ")
        if enter.lower().strip() == "n" in ("n", "no"):
            print("\nYou continue on past the garage")

        elif enter.lower().strip() == 'y' in ('y', 'yes'):

            self.take_ticket()

            while True:
                
                print("""
                What would you like to do?
                ___________________

                [1] - Take Ticket 
                [2] - Pay Ticket
                [3] - Leave 
                [4] - Stop Parking
                ___________________
 
                """)
                action = input('Input: ')

                if action == '1':
                    self.take_ticket()

                elif action == '2':
                    self.pay_for_parking()

                elif action == '3':
                    self.leave_garage()

                elif action == '4':
                    print("\nHope you've enjoyed parking and paying for tickets... see you next time!")
                    break

                else:
                    print('\nInvalid Input: Try again')

test = Parking_Garage()

test.run()