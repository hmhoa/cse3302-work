#Name: Hoang Ho
#ID: 1001654608
#Date Turned In: April 2, 2021
#OS: Windows 10
#Python 3.9.2 used

#Lab 2 - RPN
#Extra Credit B implemented
#Additional operators added for Extra Credit B: exponential ^ and modulo %

import os

#defining function(s)

#Extra Credit A
#translates the algebraic expression and converts it to Reverse Polish Notation (RPN)
#returns a list of the translated RPN expression, each operand and operator
#being an element in the list
#expression is the untranslated algebraic expression
def toRPN(expression):
    RPN = []
    operands = []
    operators = []
    
    #the position of the last operand or operator added to RPN
    #for the purposes of making sure we are following PEMDAS
    i = 0

    #loop through the algebraic expression and distinguish operands
    #and operators into separate lists to create RPN later
    #parentheses are added to both to indicate when to add operators
    #to the end of operands
    for op in expression:
        if operators:
            if (operators[0] == '(' and op == ')'):
                operators.remove(0)
                for operator in operators:
                    temp = RPN[i-1]
                    #makes sure ^ comes before * or / or %
                    while(operator == '^' and (temp == '*' or temp == '/'):
                        RPN[i-1] = operator
                        RPN.append(temp)
                    #makes sure ^ or * or / or % come before + or -
                    elif((operator == '^' or operator == '*' or operator == '/' or operator == '%') and (temp == '+' or temp == '-')):
                        RPN[i-1] = operator
                        RPN.append(temp)
                        
                    RPN.append(operator)
                    operators.remove(0)
                    i++
                
        elif (op != '(' and op != ')' and op != '+' and op != '-' and op != '*' and  op != '/' and op != '^' and op != '%'):
            RPN.append(op)
            i++
        else:
            operators.append(op)

    #create RPN by combining operands and operators
    for i in operands:
        if(operand == '(')
            
            
    return RPN
    
#solves the current reverse polish notation expression from the input text file
#returns the result of the expression
#expression is assumed to already be in RPN/postfix form
def solveRPN(expression):
    operands = []
    num1 = 0
    num2 = 0
    
    #loop through the list of expressions
    for op in expression:
        if (op != '+' and op != '-' and op != '*' and  op != '/' and op != '^' and op != '%'):
            operands.append(int(op))
        else:
            #num2 will be the first pop() since the number is popped from the end of the list
            num2 = operands.pop()
            num1 = operands.pop()
            
            if op == '+':
                operands.append(num1+num2)
            elif op == '-':
                operands.append(num1-num2)
            elif op == '*':
                operands.append(num1*num2)
            elif op == '/':
                operands.append(num1/num2)
            #Extra Credit B: added exponential  ^ and modulo % below
            elif op == '%':
                num2 = int(num1/num2)
                operands.append(num1-num2)
            elif op == '^':
                #loop to continuously multiply the base by itself num2 number of times and store into num1
                base = num1
                for i in range(1, num2):
                    num1 *= base
                operands.append(num1)

    #return the single resulting number in operands calculated after going through the entire expression
    return operands.pop()

#opens up the input file and stores each line into a list
file = open(os.getcwd() + "/input_RPN_EC.txt", "r")

#solve each RPN expression in the input file and output the results
for text in file:
    #split gets rid of all whitespace leaving only operands and operators in the list
    #translate to RPN/postfix form
    expression = toRPN(text.split())
    result = solveRPN(expression)
    print(expression)
    print(result)

file.close()
