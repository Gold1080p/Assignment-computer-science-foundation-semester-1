class Ticket:
    def __init__(self, name, base_price):
        self.name = name
        self.base_price = base_price
        def get_name(self):
            return self.name__name
        def price(self):
            return self.base_price
        class studentTicket(Ticket):
            def price(self):
                return super().price*0.5
            class groupTicket(Ticket):
                def __init__(self, name, base_price, people)
                super().__init__(name, base_price)
                self.__people = people
