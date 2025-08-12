import json

def lambda_handler(event, context):
    print("***********")
    print(event)
    print("************")
    number1 = 10
    number2 = 5
    
    sum = number1 + number2
    sub = number1 - number2
    mul = number1 * number2
    div = number1/number2

    return {
    'statuscode': 200,
    'body': ({	
	    'sum': sum,
	    'sub': sub,
	    'mul': mul
	    'div': div
})
}
