import os
import re

historyList = []

class InvalidInputError(Exception):
    pass

class Math:
    @staticmethod
    def add(a,b): return a + b
    @staticmethod
    def sub(a,b): return a - b
    @staticmethod
    def mult(a,b): return a * b
    @staticmethod
    def div(a, b): return a / b

def isNumber(s):
    try:
        float(s) 
        return True
    except ValueError:
        return False

def readUserInput(message = "Enter: "):
    userInput = input(message)
    if userInput == "" or userInput == None:
      return None;
    
    if re.search("[a-zA-Z]", userInput):
        raise InvalidInputError("Invalid math value")
    
    return userInput

#function to convert operation to Polish Notation.
def getRpnList(operation = ""):
    priority = {
        "*": 3,
        "/": 3,
        "+": 2,
        "-": 2
    }
    cleanOperation = operation.replace(" ","")
    
    stackOperators = []
    output = []
    pattern = r'\d+\.\d+|\d+|[+*/-]'
    
    for token in re.findall(pattern, cleanOperation):
        if(isNumber(token)):
            output.insert(len(output), token)
        else:
            while stackOperators and priority[stackOperators[-1]] >= priority[token]:
                output.append(stackOperators.pop())
            stackOperators.append(token); 

    while stackOperators:
        output.append(stackOperators.pop())
           
    return output
    
def getOperationResult(calc = ""):
    if not calc:
        return None
    
    ops = {
        "+": Math.add,
        "-": Math.sub,
        "*": Math.mult,
        "x": Math.mult,
        "/": Math.div
    }
    operations = getRpnList(calc)
    stack = []
    
    for token in operations:
        if isNumber(token):
            stack.append(float(token))
        else:
            b = stack.pop()
            a = stack.pop()
            
            resultado_parcial = ops[token](a, b)
            stack.append(resultado_parcial)
    finalResult = stack[0];
    historyList.append(f"{calc} = {stack}")
    return finalResult

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
        
        strOperation = readUserInput("Type your operation: ")
        getOperationResult(strOperation)
        printCalculator()
        
    except InvalidInputError as e:
        print(f"{e}... Press any key to continue")
        input()
        printCalculator();
    
def init():
    printCalculator();
    
init()