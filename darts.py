import numpy as np
import random
import matplotlib.pyplot as plt
import math

"""
Quick simulation estimating pi using the classic example of 
    throwing darts! 
"""

class Darts:
    def __init__(self, num_darts, board_width=2):
        self.num_darts = num_darts
        self.board_width = board_width
        self.center = np.array([board_width / 2, board_width / 2])
    
    def run(self):
        # Keep track of darts that land in or out of the circle
        # Initializing 2d array to seperate x and y values to make plotting easier
        self.darts_in = [[],[]]
        self.darts_out = [[],[]]

        darts_in_circle = 0
        for i in range(self.num_darts):
            # Random point in both x and y axis
            x = random.random() * self.board_width
            y = random.random() * self.board_width

            # Calculating distance to the center using well known formula sqrt((x0-y0)^2 + (x1-y1)^2)
            dist = math.sqrt((self.center[0] - x)**2 + (self.center[1] - y)**2)

            # If distance to center is less than the radius, point must be within the circle 
            if dist < self.board_width / 2:
                darts_in_circle += 1
                self.darts_in[0].append(x)
                self.darts_in[1].append(y)
            else:
                self.darts_out[0].append(x)
                self.darts_out[1].append(y)
        return 4 * darts_in_circle / self.num_darts
    
    def plot_darts(self):
        plt.scatter(self.darts_in[0], self.darts_in[1], c='blue', marker='.')
        plt.scatter(self.darts_out[0], self.darts_out[1],c='red', marker='.')
        plt.show()


# Example usage
def example():
    d = Darts(1000,board_width=2)
    print(d.run())
    d.plot_darts()

