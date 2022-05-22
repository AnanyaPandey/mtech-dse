# -*- coding: utf-8 -*-
"""
Created on Wed May  4 16:51:46 2022

@author: pandey
"""
# multilevel 

# Base Class
class Vehicles:
    def __init__(self, number, exshowroom_price):
        self.number = number
        self.exshowroom_price = exshowroom_price


# Intermediate class
class Cars(Vehicles):
    def __init__(self, number, exshowroom_price, n_passenger):
        super().__init__(number, exshowroom_price)
        self.n_passenger = n_passenger


# Derived class
class ElectricCars(Cars):
    def __init__(self, number, exshowroom_price, n_passenger, charger_type):
        super().__init__(number, exshowroom_price, n_passenger)
        self.charger_type = charger_type
        
vehicle_1 = Vehicles("RJ06 1719", 500000)
car_1 = Cars("RJ06 2296", 750000, 5)
ecar_1 = ElectricCars("DL14 9996", 200000, 5, "RCA")