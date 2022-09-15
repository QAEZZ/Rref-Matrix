import subprocess as sub
from colorama import init
import re


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
        table = f"{self.num1}x{self.num2}"
        print(table)

        if re.search('[a-zA-Z]', self.num1) or re.search('[a-zA-Z]', self.num2):
          print("num1/2 detected something that isnt a number!")
        else:
            self.num1 = int(self.num1)
            self.num2 = int(self.num2)
    
    def buildTable(self):
        self.numList = []
        self.pre = []

        self.counter = 0
        self.rowCounter = 1

        for i in range(self.num2):
            for i in range(self.num2):
                self.counter += 1
                self.pre.append(input(f"{self.rowCounter}, {self.counter} = "))
            self.rowCounter += 1
            self.counter = 0
            self.numList.append(self.pre)
            self.pre = []
        
        for row in self.numList:
            row = str(row)
            print(row.replace(",", ""))
                


Main()