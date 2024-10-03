class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    # Method to make the dog bark
    def bark(self):
        return f"{self.name} says Woof!"

    # Method to get the dog's age in dog years (1 human year = 7 dog years)
    def age_in_dog_years(self):
        return self.age * 7

    # Method to make the dog fetch a ball
    def fetch(self, item):
        return f"{self.name} fetched the {item}!"

    # Method to display basic information about the dog
    def __str__(self):
        return f"{self.name} is a {self.age}-year-old {self.breed}."
