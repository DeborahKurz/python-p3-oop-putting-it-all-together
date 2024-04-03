#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size
        self.condition = "New"

    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, size):
        if isinstance(size, int):
            self._size = size 
        else:
            print("size must be an integer")

    @property
    def brand(self):
        return self._brand
    
    @brand.setter
    def brand(self, brand):
        if isinstance(brand, str):
            self._brand = brand 
        else:
            print("brand must be a string")
            
    def cobble(self):
        print("Your shoe is as good as new!")

    def repair(self):
        self.condition = "New"
