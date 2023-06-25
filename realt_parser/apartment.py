class Apartment:
    def __init__(self, square, num_of_storeys, price, update_date, realtor, adress_ap):
        self.square = square
        self.num_of_storeys = num_of_storeys
        self.price = price
        self.update_date = update_date
        self.realtor = realtor
        self.adress_ap = adress_ap

    def info(self):
        return self.__dict__
