def another_function(e):
    print(f"\nValue received As Parameter in another_function: {e}")
    abc = e + 1000
    return abc

def test_function(c):
    print(f"\nValue received As Parameter in test_function : {c}")
    d = 100
    e = d - c
    return e   

def main():
    a = 10
    b = 5
    c = a + b
    return c   

# Main Function call
main_value = main()
print("\nValue of main Function :", main_value)

# Test Function call
test_value = test_function(main_value)
print("\nValue of test_function :", test_value)

#Another Function Call
another_value = another_function(test_value)
print("\nValue of another_function :", another_value)
