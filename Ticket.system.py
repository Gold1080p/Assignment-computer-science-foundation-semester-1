class Ticket:
    def __init__(self, name, base_price):
        self.__name = name
        self.base_price = base_price
    def get_name(self):
            return self.__name
    def price(self):
            return self.base_price
class studentTicket(Ticket):
    def price(self):
            return super().price*0.5
class groupTicket(Ticket):
    def __init__(self, name, base_price, people):
        super().__init__(name, base_price)
        self.__people = people
    def price(self):
        return super().price() * self.__people * 0.8
##student = studentTicket("museum",150)
##group = groupTicket("zoo",300,4)
##print(student.get_name(),group.price())
