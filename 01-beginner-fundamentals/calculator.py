import os
import re

historyList = []

class InvalidInputError(Exception):
    pass

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
    if userInput == "" or userInput == None:
      return None;
    
    if re.search("[a-zA-Z]", userInput):
        raise InvalidInputError("Invalid math value")
    
    mathValidRegularExpresion
    return userInput

def getOperationsArray(operation = ""):
    cleanOperation = operation.replace(" ","")
    return []
    
def applyCalculate(calc = ""):
    if calc == None:
        return None;
    operations = getOperationsArray(calc)
    
    result = ""
    historyList.append(f"{calc} = {result}")
    return

def clearConsole():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def printCalcHeader():
    print("====================== Console Calculator ==========================")
    print("Options: C (clean)   Esc (exit)    B (back to last operation)")
    print("====================================================================")
    
def printCalculator():
    try:
        clearConsole()
        printCalcHeader()
        for hc in historyList:
            print(f" Cal: {hc}")
            
        value = readUserInput("Type your operation: ")
        applyCalculate(value)
        printCalculator()
        
    except InvalidInputError as e:
        print(f"{e}... Press any key to continue")
        input()
        printCalculator();
    
def init():
    printCalculator();
    
init()