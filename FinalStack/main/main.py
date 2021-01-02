# main driver for Stack program
from stack import Stack # used to import implemented Stack class.
import fileinput # used to import data from text file.

def main(): # main driver.

    filePath = "data.txt" # sets path for file to access.
    file = open(filePath) # opens file.
    expressionCount = len(file.readlines()) # gets number of lines in file.
    file = open(filePath) # reopen file.

    for x in range(expressionCount): # loop loads data file line by line, and then converts infix statements to postfix, and calculates.
        line = file.readline()
        print("Infix Expression: ", line.replace("\n",""))
        print("Postfix Expression: ", in2post(line))
        print("Product: ", eval_postfix(in2post(line)))
        print(" ")

def in2post(expression):
    if (type(expression) != str): # throws value error if expression provided is not a String.
        raise ValueError("The provided expression is not a string")
    finalString = ''
    operators = Stack()


    for x in expression.replace("\n", "").replace(" ", ""): # iterates through all non white space characters.
        if (x.isdigit()): # appends all digits immediately to the postfix expression.
            finalString += x
            finalString += " "
        elif (x == '('): # pushes any left parenthesis onto the operators stack.
            operators.push(x)
        elif (x == ')'): # pops all operators on stack until reaches left parenthesis.
            if (operators.size() == 0): # raises error if there are no left parenthesis in stack after finding right parenthesis.
                raise SyntaxError("This is not a balanced infix expression.")
            while (operators.size() != 0 and operators.top() != '('):
                finalString += operators.pop() # appends poped operators onto the postfix expression.
                finalString += " "
            operators.pop() # pops the left parenthesis.
        else:
            while(operators.size() != 0 and getPriority(x) <= getPriority(operators.top())): # compares priority of current operator to operators in stack.
                finalString += operators.pop() # appends all higher priority operators from stack onto the postfix expression.
                finalString += " "
            operators.push(x) # pushes current operator onto the stack.
    while(operators.size() > 0):
        finalString += operators.pop() # pops all remaining operators from stack and appends them to the postfix expression.
        finalString += " "
    return finalString # returns postfix expression.

    

def getPriority(operator): # this function defines the precidence for all of the operators.
    if (operator == "*" or operator == "/"):
        return 3
    if (operator == "+" or operator == "-"):
        return 2
    if (operator == "("):
        return 1

def eval_postfix(expression): # this function used to evaluate postfix expressions.
    operators = Stack() # stack used for operators in expression.
    operands = Stack() # stack used for operands in expression.
    expression = expression.replace(" ", "") # replaces white space in postfix expression.
    for x in range(len(expression)): # iterates through postfix expression.
        if (expression[x] == "*" or expression[x] == "+" or expression[x] == "-" or expression[x] == "/"):
            if (operands.size() < 2): # if unbalanced postfix expression, raises error.
                raise SyntaxError ("Invalid postfix expression.")
            else: # if current position is operand.
                tempA = operands.pop() # pops top two operands when reaches first operator.
                tempB = operands.pop()
                if (expression[x] == "+"): # perform operations, converting strings to floats.
                    operands.push(float(tempA) + float(tempB))
                elif (expression[x] == "*"):
                    operands.push(float(tempA) * float(tempB))
                elif (expression[x] == "/"):
                    operands.push(float(tempB) / float(tempA))
                elif (expression[x] == "-"):
                    operands.push(float(tempB) - float(tempA))
        else:
            operands.push(float(expression[x])) # pushes operands onto the operand stack.
    return operands.top() # returns the final operand stack top, which is final solution.
    

main()
