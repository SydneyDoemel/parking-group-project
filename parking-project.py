class ParkingGarage:
    def __init__(self, tickets, spaces):
        self.tickets =  [i for i in (range(tickets + 1)[1:])] #make a list from the # of spaces they input. 3 --> [1,2,3]
        self.spaces = [i for i in (range(spaces + 1)[1:])] #same as above
        self.current_ticket = {} #empty dict which is appended when someone takes a ticket

    def takeTicket(self):
        x = self.tickets.pop(-1)
        self.spaces.pop(-1)
        self.current_ticket[x] = False #adding ticket to current tickets and setting it tp F until they pay
        print(f'Ticket #{x}')
    def payForParking(self):
        active = True
        while active: 
            amount = input('Payment complete? Y/N: ')
            if amount.upper() == "Y":
                num = input("Please enter your ticket number: ")
                print("You have payed for your ticket. You have 15 minutes to exit the garage.")
                self.current_ticket[int(num)] = True #marking as paid in current dict
                self.leaveGarage() #do we need to do  something about the 15 minute thing? Shoulditnot  go immediately to leavegarage()?
                active = False
            else:
                continue

    def leaveGarage(self):
        print("Thank you! Have a nice day.")
        add_ticket = len(self.tickets) + 1
        self.tickets.append(add_ticket)
        self.spaces.append(add_ticket)
            


garage1 = ParkingGarage(10, 10)
print(garage1.__dict__)
garage1.takeTicket()
print(garage1.__dict__)
garage1.payForParking()
print(garage1.__dict__)

