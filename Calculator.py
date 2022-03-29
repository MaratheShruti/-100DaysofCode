from art import logo

# Addition
def add(n1,n2):
  return n1 + n2

# Substraction
def sub(n1,n2):
  return n1 - n2

# Multiplication
def multi(n1,n2):
  return n1 * n2

# division
def div(n1,n2):
  return n1/n2

source_dict = {"+":add, "-":sub, "*":multi, "/":div}
def calculator():
  print(logo)
  num1 = float(input("What is the first number?\n"))
  
  for operation in source_dict:
    print(operation)
  cal_continue = True
  while cal_continue ==  True:
    operations = input("Which operation to you choose to perform? '+','-','*','/'\n")
    num2 = float(input("What is the next number?\n"))
    calculation = source_dict[operations]
    answer = calculation(num1,num2)
    print(f"{num1} {operations} {num2} = {answer}")
    
    continue_cal = input(f"Type 'y' to continue calculating with {answer} or type 'n' to start a new calculation.\n")
  
    if continue_cal == 'y':
      num1 = answer
    else:
      cal_continue = False
      calculator()


calculator()
