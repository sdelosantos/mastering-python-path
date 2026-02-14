import os

historyList = []

class Math:
    @staticmethod
    def Sum(a,b): a + b
    @staticmethod
    def Subtract(a,b): a - b
    @staticmethod
    def Multiply(a,b): a * b
    @staticmethod
    def Divide(a, b): a / b

def readUserInput(message = "Enter: "):
    userInput = input(message)
    return userInput

def getDevideOperations(operation = ""):
    cleanOperation = operation.replace(" ","")
    return []
    
def applyCalculate(calc = None):
    if calc == None:
        return
    
    result = ""
    historyList.append(f"{calc} = {result}")
    return

def clearConsole():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def printCalOptions():
    print("Options: C (clean)   Esc (exit)    B (back to last operation)")
    
def printCalculator():
    clearConsole()
    print("====================== Console Calculator ==========================")
    printCalOptions()
    print("====================================================================")
    
    for hc in historyList:
        print(f" Cal: {hc}")
    input = readUserInput("Type your operation: ")
    applyCalculate(input)
    printCalculator()
    
def init():
    printCalculator();
    
init()