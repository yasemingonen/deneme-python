"""
Coding Challenge - 2: Calculate Stock Profit
The purpose of this coding challenge is to write a program that calculates maximum profit you could get from a stock.
Learning Outcomes
At the end of this coding challenge, students will be able to;
analyze a problem, identify, and apply programming knowledge for appropriate solution.
design, implement arithmetic operators effectively in Python to solve the given problem.
demonstrate their knowledge of algorithmic design principles by solving the problem effectively.
Problem Statement
Given an array of numbers representing the stock prices of a company in chronological order, write a function that calculates the maximum profit you could have made from buying and selling that stock once. Note that you must buy before you can sell it.
For example, given [9, 11, 8, 5, 7, 10], you should return 5, since you could buy the stock at 5 dollars and sell it at 10 dollars.
Example of different list of stock prices and respective outputs.
List = [75,73,60,100,120,130]
Output = 70
List = [10,20,23,22,17,30]
Output = 20
List = [1,6,19,59,30,60]
Output = 59
"""


money_list = [75,73,60,100,120,130]
order_list = sorted(money_list)
print(order_list[-1]- order_list[0])

class Line:

    def __init__(self, coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2

        return ((x2-x1)**2 + (y2-y1)**2)**0.5

    def slope(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2

        return (y2-y1) / (x2-x1)

c1 = (3,2)
c2 = (8,10)
myline = Line(c1,c2)
myline.distance()

myline.slope()



"""
second answer
def buy_and_sell(arr):
    current_max, max_profit = 0, 0
    for price in reversed(arr):
        current_max = max(current_max, price)
        potential_profit = current_max - price
        max_profit = max(max_profit, potential_profit)
    return max_profit
"""
