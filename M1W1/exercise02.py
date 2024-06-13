import math
import numpy as np

# sigmoid
def sigmoid_func(x):
    return 1/(1+math.exp(-x))

def reLU_func(x):
    return x if x>0 else 0

def elu_func(x, a=0.11):
    return x if x>0 else a*(math.exp(x)-1)*0.01

# Given
def is_number ( n ) :
    try :
        float ( n ) # Type - casting the string to ‘float ‘.
        # If string is not a valid ‘float ‘ ,
        # it 'll raise ‘ValueError ‘ exception
    except ValueError :
        return False
    return True

def exercise2(x, act_name):
    if act_name !='sigmoid' and act_name !='relu' and act_name !='elu':
        return print(f'{act_name} use is not support')
    try:
        x = float(x)
    except:
        return print(f'{x} must be number')

    if act_name == 'sigmoid':
        return print(f'sigmoid f({x}):{sigmoid_func(x)}')
    elif act_name == 'relu':
        return  print(f'relu f({x}):{reLU_func(x)}')
    elif act_name == 'elu':
        return print(f'elu f({x}):{elu_func(x, a=0.01)}')
    else:
        return None
    
if __name__ == '__main__':
    exercise2('10', 'relu')
    print('----------------------------------------')
    exercise2('2', 'elu')
    print('----------------------------------------')
    exercise2('a', 'relu')
    print('----------------------------------------')
    exercise2( 3, 'sigmoid')
    print('----------------------------------------')
