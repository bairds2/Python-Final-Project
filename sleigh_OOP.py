"""
    Name: sleigh_OOP.py
    Author: Savannah Baird
    Date: 12/11/25
    Purpose: Use Object Oriented Programing to make a vehicle
"""

# TODO: Create a Vehicle Class
class Sleigh:
    # define the init method
    def __init__(self, speed, color, driver, reindeer):
        self.speed = speed
        self.color = color
        self.driver = driver
        self.reindeer = reindeer
    
    # define a setter for each attribute
    def set_speed(self, speed):
        self.speed = speed

    def set_color(self, color):
        self.color = color

    def set_driver(self, driver):
        self.driver = driver
    
    def set_reindeer(self, reindeer):
        self.reindeer = reindeer

    # make a display method that displays the class attributes
    def sleigh_info(self):
        sleigh_details = f"The Sleigh is {self.color} and {self.driver} is driving. {self.driver}'s Sleigh is going {self.speed} miles per hour.\n{self.driver} has {self.reindeer} reindeer!"
        return sleigh_details
    
# Define the attributes of the class and print the sleigh_info method
sleigh = Sleigh(50, "red", "Santa", 10)
print (sleigh.sleigh_info())

