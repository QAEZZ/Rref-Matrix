import subprocess as sub


def clear(shell=True):
    sub.call("clear", shell=shell)


class Main():
    
    def __init__(self):
        print("ready")

        self.run()
    
    def run(self):
        self.getNums()
    
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


Main()