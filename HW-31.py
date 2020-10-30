class Dogs:
    animal = 'Dog'

    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def __str__(self):
        return f'Dog name is {self.name} and age is {self.age}'

    def dog_sound(self, sound):
        return f'{self.animal} {self.name} says "{sound}"'


Snappy = Dogs('Snappy', '4', 'Rottweiler')
Snappy_sound = input('Put a sound of Snappy: ')
print(Snappy.dog_sound(Snappy_sound))


class Alabai(Dogs):

    def __init__(self, name, age, breed, loudness):
        super().__init__(name, age, breed)
        self.loudness = loudness

    def dog_sound(self, sound):
        return f'{super().dog_sound(sound)} {self.loudness}'


Chappy = Alabai('Chappy', 2, 'Alabai', 'loudly')
Chappy_sound = input('Put a sound of Chappy: ')
print(Chappy.dog_sound(Chappy_sound))


class Spitz(Alabai):

    def dog_sound(self, sound):
        return f'{super().dog_sound(sound)} {self.loudness}'


Ronny = Spitz('Ronny', 6, 'Spitz', 'quietly')
Ronny_sound = input('Put a sound of Ronny: ')
print(Ronny.dog_sound(Ronny_sound))
