import os
import re

class InvalidInputError(Exception):
    pass

def is_valid_expression(expr: str) -> bool:
    expr = expr.strip()
    number = r'\(?\d+(\.\d+)?\)?'    
    operator = r'[\+\-\*\/]'
    pattern = rf'^[\(\)]*{number}([\(\)]*{operator}[\(\)]*{number})*[\(\)]*$'

    if not bool(re.match(r'^[0-9+\-*/().\s]+$', expr)):
        return False
    
    return bool(re.match(pattern, expr))

def is_number(s: str)->bool:
    try:
        float(s) 
        return True
    except ValueError:
        return False

def read_user_input(message: str)->str:
    userInput = input(message)

    if not userInput:
      return None;
    return userInput

#function to convert operation to Polish Notation.
def get_rpn_list(operation: str) -> list:
    priority = {
        "*": 3, 
        "/": 3,
        "+": 2, 
        "-": 2,
        "(": 1 
    }
    cleanOperation = operation.strip()
    
    stackOperators = []
    output = []
    pattern = r'\d+\.\d+|\d+|[+*/()-]'
    
    for token in re.findall(pattern, cleanOperation):
        if is_number(token):
            output.append(token)
        elif token == '(':
            stackOperators.append(token)
        elif token == ')':
            while stackOperators and stackOperators[-1] != '(':
                output.append(stackOperators.pop())
            if stackOperators:
                stackOperators.pop()
        else:
            while (stackOperators and 
                   stackOperators[-1] != '(' and 
                   priority[stackOperators[-1]] >= priority[token]):
                output.append(stackOperators.pop())
            stackOperators.append(token)
                
    while stackOperators:
        output.append(stackOperators.pop())
           
    return output
def get_operation_result(calc: str, historyList: list)->float:
    if not calc:
        return None
    
    if not is_valid_expression(calc):
        raise InvalidInputError("Invalid math operation")
    
    ops = {
        "+": lambda a,b: a + b,
        "-": lambda a,b: a - b,
        "*": lambda a,b: a * b,
        "x": lambda a,b: a * b,
        "/": lambda a,b: a / b
    }
    
    operations = get_rpn_list(calc)
    stack = []
    
    for token in operations:
        if is_number(token):
            stack.append(float(token))
        else:
            b = stack.pop()
            a = stack.pop()
            
            resultado_parcial = ops[token](a, b)
            stack.append(resultado_parcial)
    finalResult = stack[0];
    historyList.append(f"{calc} = {finalResult}")
    return finalResult

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_calc_options():
    print("====================== Console Calculator ==========================")
    
def run_calculator(historyList:list):
    while True:
        try:
            clear_console()
            print_calc_options()
            for hc in historyList:
                print(f" Cal: {hc}")
            
            strOperation = read_user_input("Type your operation: ")
            get_operation_result(strOperation, historyList)

        except InvalidInputError as e:
            print(f"{e}... Press any enter to continue")
            input()
    
def init():
    run_calculator([]);
    
init()