import numpy as np

def md_nre_single_sample(y,y_hat,n,p, m=1):
    return np.sum((y**(1/n)-y_hat**(1/n))**p)/m

if __name__ == '__main__':
    print(f'md_nre_single_sample: {md_nre_single_sample( y =100 , y_hat =99.5 , n =2 , p =1)}')