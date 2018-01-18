class Product():
    def __init__(self, price, item_name, weight, brand, cost, status="For Sale"):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = status

    def sell(self):
        self.status = "Sold"
        return self

    def add_tax(self, tax):
        self.price = self.price + self.price * tax
        return self

    def Return(self, reason):
        if reason == "defective":
            self.status = "Defective"
            self.price = 0
        elif reason == "in the box, like new":
            self.status = "For Sale"
        elif reason == "box opened":
            self.status = "Used"
            self.price = self.price - (self.price * .20)
        return self

    def displayinfo(self):
        print "Price: ${}, Item Name: {}, Weight: {}, Brand: {}, Cost: ${}, Status: {}".format(self.price, self.item_name, self.weight, self.brand, self.cost, self.status)
        return self

item1 = Product(10.99, "One", "5lbs", "Anon", 10.99).displayinfo()
item2 = Product(3.50, "Two", "1lb", "Anon", 3.50).sell().displayinfo()
item3 = Product(6.00, "Three", "4lbs", "Anon", 6.50).add_tax(0.07).displayinfo()
item4 = Product(5.00, "Four", "2lbs", "Anon", 5.00).Return("defective").displayinfo()
item5 = Product(12.50, "Five", "10lbs", "Anon", 12.50).Return("box opened").displayinfo()


