from ticketscript import Ticket, studentTicket, groupTicket

def show_all(tickets):
    for t in tickets:
        print(f"{t.get_name()}: rs {t.price():.2f}")

def main():
    tickets_list = [Ticket("concert",200), studentTicket("museum",150)]
    show_all(tickets_list)

main()
            
