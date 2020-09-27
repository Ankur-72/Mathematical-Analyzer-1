def checkStatement(a,b):
    sum1 = a+b
    if sum1< 75:
        print("Their sum is less than 75")
    else:
        print("Their sum is not less than 75")
        
print("Hey, I am your mathematical analyser.")
print("Please provide two numbers and I will check if their sum is below 75.")
    
num1 = int(input())
num2 = int(input())

checkStatement(num1,num2)