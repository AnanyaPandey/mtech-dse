# -*- coding: utf-8 -*-
"""
Created on Wed May  4 15:56:06 2022

@author: pandey
"""


class Cars:
    reg_cost = 100
    def __init__(self,no, fuel_cap, ex_price):
        self.no = no 
        self.fuel_cap = fuel_cap
        self.ex_price = ex_price
    def on_road_price(self):
        cor = self.ex_price * self.reg_cost
        return cor + self.ex_price


class e_cars(Cars):
    reg_cost = 250
    def __init__(self,no, fuel_cap, ex_price, ch_type, ch_mileage):
        super().__init__(no, fuel_cap, ex_price)

        self.ch_type = ch_type
        self.ch_mileage = ch_mileage

car1 = Cars('CG17', '35 ltr', 50000)
ecar1 = e_cars('MP09', '42 ltr', 60000, 'CCS', 352)

