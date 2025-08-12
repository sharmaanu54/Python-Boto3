import sys

def add(n1, n2):
    sum = n1+n2
    return sum
    
def sub(n1, n2):
    suubtract = n1-n2
    return suubtract    
    
def multi(n1, n2):
    multiplication = n1*n2
    return multiplication

n1 = int(sys.argv[1])   
operation = sys.argv[2]
n2 = int(sys.argv[3])

if operation == 'add':
    output = add(n1, n2)
    print(output)

# if operation == 'sub':
#     output = sub(n1, n2)
#     print(output)
    
#     if operation == 'multi':
#     output = multi(n1, n2)
#     print(output)

    