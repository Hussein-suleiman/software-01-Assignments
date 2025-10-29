class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        print('some animal sound')

    def display_sound(self):
        print(f'Name: {self.name}, Species: {self.species}')


    #2
class lion(Animal):
    def __init__(self, name):
        super().__init__(name, 'lion')

    def make_sound(self):
        print('ROOOOOAR')

class Elephant(Animal):
    def __init__(self, name):
        super().__init__(name, 'elephant')

        def make_sound(self):
            print('Sound like an elephant')


class Snake(Animal):
    def __init__(self, name):
        super().__init__(name, 'snake')

        def make_sound(self):
            print('ssss')

#3
class ZOO:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f'{animal.name} the {animal.species} animal is added to animals list')

    def display_animals(self):
        print('\n Animals list')
        for animal in self.animals:
            animal.display_sound()
        print(f'\n Animals list length: {len(self.animals)}')

    def make_sound(self):
        print('\n Animals list')
        for animal in self.animals:
            animal.make_sound()

    #MAIN PROGRAM
if __name__ == '__main__':
    lion = lion('Royalty')
    elephant = Elephant('Hussein')
    snake = Snake('Princess')

    my_zoo= ZOO()
    my_zoo.add_animal(lion)
    my_zoo.add_animal(elephant)
    my_zoo.add_animal(snake)

    my_zoo.display_animals()
    my_zoo.make_sound()