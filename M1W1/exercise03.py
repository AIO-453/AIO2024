
import numpy as np
import random

def MAE(y, y_hat):
    n = len(y)
    return np.sum(abs(y-y_hat))/n

def MSE(y, y_hat):
    n = len(y)
    return np.sum((y-y_hat)**2)/n

def RMSE(y, y_hat):
    n = len(y)
    return np.sum(np.sqrt((y-y_hat)**2/n))

def exercise3(num_sample, loss_name):
    if type(num_sample) != int:
        return print(f'{num_sample} must be int')
    if loss_name !='MAE' and loss_name !='MSE' and loss_name !='RMSE':
        return print(f'{loss_name} use is not support')

    else:
        y = np.array([random.randint(0, 10) for i in range(num_sample)])
        y_hat = np.array([random.randint(0, 10) for i in range(num_sample)])

        if loss_name == 'MAE':
            return print(f'mae:{MAE(y, y_hat)}')
        elif loss_name == 'MSE':
            return  print(f'mse:{MSE(y, y_hat)}')
        elif loss_name == 'RMSE':
            return print(f'RMSE:{RMSE(y, y_hat)}')
        else:
            return None
        
if __name__ == '__main__':
    exercise3(0, 'RMSE')
    exercise3(10, 'MSE')
    exercise3(10, 'MAE')
    exercise3(0.3, 'MAE')


