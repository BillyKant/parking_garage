tickets = [1,2,3,4,5,6,7,8,9,10]
parking_spaces = [1,2,3,4,5,6,7,8,9,10]
current_ticket = {}

if tickets:

    #1st ticket needs to leave self.tickets % assign to self.current_ticket
    ticket_num = tickets.pop(0)
    current_ticket[ticket_num] = ''
    print(f'Your ticket number is: {ticket_num}')

        #2Remove corresponding ticket value from parking_spaces
else:

    print('Sorry no spaces are available... ')

print(current_ticket)