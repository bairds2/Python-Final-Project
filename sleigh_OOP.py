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
    # increase the speed by 50
    def set_speed(self, speed):
        self.speed = speed + 50
        return self.speed

    def set_color(self, color):
        self.color = color

    def set_driver(self, driver):
        self.driver = driver
    
    def set_reindeer(self, reindeer):
        self.reindeer = reindeer

    # define a deliver presents method
    def deliver_presents(self):
        return "The Sleigh takes off and you deliever 100 presents"
    
    # define a eat cookies method
    def eat_cookies(self):
        cookies = input(f"How many cookies do you want? ")
        return (f"You ate {cookies} cookies!")
    # make a display method that displays the class attributes
    def sleigh_info(self):
        sleigh_details = f"The Sleigh is {self.color} and {self.driver} is driving. {self.driver}'s Sleigh is going {self.speed} miles per hour.\n{self.driver} has {self.reindeer} reindeer!"
        return sleigh_details


color = "red"
driver = "Santa"
reindeer = 0
speed = 100 

sleigh = Sleigh(speed, color, driver, reindeer)
print("Welcome to Dave's Sleigh Studio!")
# allow for user input of variables
color = input("What color is your sleigh? ")
sleigh.set_color(color)
driver = input("Who is driving the Sleigh? ")
sleigh.set_driver(driver)
reindeer = int(input("How many reindeer do you have? "))
sleigh.set_reindeer(reindeer)
speed = int(input("How fast do you want to go?"))
sleigh = Sleigh(speed, color, driver, reindeer)
print(sleigh.sleigh_info())


sleigh = Sleigh(speed, color, driver, reindeer)
# print a menu of choices
menu = input("Build your sleigh! [(d)eliver presents] [add (r)eindeer] [increase (s)peed] [(c)ookie break] [(v)iew] [e(x)it]: ")
# use a while loop to allow to keep going through the menu
while menu != "x":
    # menu == d
    if menu == "d":
        print(sleigh.deliver_presents())
        menu = input("Build your sleigh! [(d)eliver presents] [add (r)eindeer] [increase (s)peed] [(c)ookie break] [(v)iew] [e(x)it]: ")
    # menu == r
    elif menu == "r":
        reindeer = input("How many Reindeer do you want now? ")
        sleigh.set_reindeer(reindeer)
        menu = input("Build your sleigh! [(d)eliver presents] [add (r)eindeer] [increase (s)peed] [(c)ookie break] [(v)iew] [e(x)it]: ")
    # menu == r
    elif menu == "c":
        print(sleigh.eat_cookies())
        menu = input("Build your sleigh! [(d)eliver presents] [add (r)eindeer] [increase (s)peed] [(c)ookie break] [(v)iew] [e(x)it]: ")
    # menu == s
    elif menu == "s":
        speed = sleigh.set_speed(sleigh.speed)
        print(f"{driver}'s sleigh is going {speed} mph")

        menu = input("Build your sleigh! [(d)eliver presents] [add (r)eindeer] [increase (s)peed] [(c)ookie break] [(v)iew] [e(x)it]: ")
    # menu == v
    elif menu == "v":
        print(sleigh.sleigh_info())
        menu = input("Build your sleigh! [(d)eliver presents] [add (r)eindeer] [increase (s)peed] [(c)ookie break] [(v)iew] [e(x)it]: ")

    # catch bad input
    else:
        print("Invalid Input. Please Try again.")
        menu = input("Build your sleigh! [(d)eliver presents] [add (r)eindeer] [increase (s)peed] [(c)ookie break] [(v)iew] [e(x)it]: ")



# print("Welcome to Dave's Sleigh Studio!")
# # allow for user input of variables
# color = input("What color is your sleigh? ")
# sleigh.set_color(color)
# driver = input("Who is driving the Sleigh? ")
# sleigh.set_driver(driver)
# reindeer = input("How many reindeer do you have? ")
# sleigh.set_reindeer(reindeer)
# speed = int(input("How fast do you want to go?"))
# sleigh = Sleigh(speed, color, driver, reindeer)
# print(sleigh.sleigh_info())
# # call teh option function

print("Have a nice day!")

