import subprocess as sub
from colorama import init
import re
import numpy as np
import sympy as sp


def clear(shell=True):
    sub.call("clear", shell=shell)


class Main():
    
    def __init__(self):
        init(autoreset=True)

        self.run()
    
    def run(self):
        self.getNums()
        self.buildTable()
    
    def getNums(self):
        print("num1")
        self.num1 = input("_x_\n>>> ")
        clear()
        print("num2")
        self.num2 = input(f"{self.num1}x_\n>>> ")
        clear()
        print("table dimensions")
        self.table = f"{self.num1}x{self.num2}"
        print(self.table)

        if re.search('[a-zA-Z]', self.num1) or re.search('[a-zA-Z]', self.num2):
          print("num1/2 detected something that isnt a number!")
        else:
            self.num1 = float(self.num1)
            self.num2 = float(self.num2)
    
    def buildTable(self):
        self.numList = []
        self.pre = []

        self.counter = 0
        self.rowCounter = 1
        

        for i in np.arange(self.num1):
            for k in np.arange(self.num2):
                self.counter += 1
                self.pre.append(input(f"{self.rowCounter}, {self.counter} = "))
            self.rowCounter += 1
            self.counter = 0
            self.numList.append(self.pre)
            self.pre = []
            clear()
            print(self.table)
        
        self.matrix_ = sp.Matrix(self.numList)

        for row in self.numList:
            row = str(row)
            print(row.replace("'", ""))
        
        print("\nrref:")

        for row in self.numList:
            self.answer = self.matrix_.rref()
            print(self.answer)
            
                
"""
3x4
30 60 60 360
1  1  1  7
2 -1  0  0
"""

Main()
