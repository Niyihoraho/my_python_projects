class Drink:
    def __init__(self,name,water,milk,coffee,cost):
        self.name=name
        self.ingredient={
            "water":water,
            "milk": milk,
            "coffee": coffee
        }
        self.cost=cost