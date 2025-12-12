"""
    Name: sleigh_OOP.py
    Author: Savannah Baird
    Date: 12/11/25
    Purpose: Use Object Oriented Programing to make a vehicle
"""

# TODO: Create a Vehicle Class
class Sleigh:
    # define the init method
    def __init__(self, speed, color, driver, bells):
        self.speed = speed
        self.color = color
        self.driver = driver
        self.bells = bells

    def sleigh_info(self):
        sleigh_details = f"The Sleigh is {self.color} and {self.driver} is driving. {self.driver}'s Sleigh is going {self.speed} miles per hour.\nDoes {self.driver} have bells? {self.bells}"
        return sleigh_details
sleigh = Sleigh(50, "red", "Santa", "Yes")
print (sleigh.sleigh_info())