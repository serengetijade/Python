#LAMBDA FUNCTIONS

def multiply(i):
    return i*i;
print(multiply(3));

y = lambda x: x * x * x;
print(y(20));

z = lambda a: a +10;
print(z(5));

#lambda function with multiple variables:
x = lambda a, b, c : a + b + c;
print(x(5, 6, 2));
