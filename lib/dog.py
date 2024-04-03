#!/usr/bin/env python3



class Dog:
    APPROVED_BREEDS = [
        "Mastiff",
        "Chihuahua",
        "Corgi",
        "Shar Pei",
        "Beagle",
        "French Bulldog",
        "Pug",
        "Pointer"
    ]

    def __init__(self, name="Zeus", breed="Mastiff"):
        self._name = None
        self._breed = None
        self.name = name  # This triggers the name setter for validation
        self.breed = breed  # This triggers the breed setter for validation

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._name = value
        else:
            print("Name must be string between 1 and 25 characters.")

    @property
    def breed(self):
        return self._breed

    @breed.setter
    def breed(self, value):
        if value in Dog.APPROVED_BREEDS:
            self._breed = value
        else:
            print("Breed must be in list of approved breeds.")