class Plant:
    def __init__(self, name, height_cm=20):
        self.name = name
        self.height = height_cm

    def care_instructions(self):
        return "Water regularly and provide adequate sunlight."

    def __str__(self):
        return f'Name: {self.name}, Height: {self.height} cm, Type: Plant'


class Flower(Plant):
    def __init__(self, name, height_cm=30, color='Green'):
        self.color = color
        super().__init__(name, height_cm)

    def care_instructions(self):
        return "Water regularly, provide full sun, and deadhead spent blooms."

    def __str__(self):
        return f'Name: {self.name}, Height: {self.height} cm, Color: {self.color}, Type: Flower'


class Vegetable(Plant):
    def __init__(self, name, height_cm=10, harvest_days=90):
        self.harvest = harvest_days
        super().__init__(name, height_cm)

    def care_instructions(self):
        return "Water regularly, provide full sun, and fertilize every two weeks."

    def __str__(self):
        return f'Name: {self.name}, Height: {self.height} cm, Harvest Days: {self.harvest}, Type: Vegetable'

