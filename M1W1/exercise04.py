# 4. Viết 4 functions để ước lượng các hàm số sau.
def fact(n):
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    return fact

def approx_sin(x , n):
    sin = 0
    for i in range(n):
        sin += ((-1)**i)*(x**(2*i+1))/(fact(2*i+1))
    return sin

def approx_cos(x , n):
    cos = 0
    for i in range(n):
        cos += ((-1)**i)*(x**(2*i))/(fact(2*i))
    return cos

def approx_sinh(x , n):
    sinh = 0
    for i in range(n):
        sinh += (x**(2*i+1))/(fact(2*i+1))
    return sinh

def approx_cosh(x , n):
    cosh = 0
    for i in range(n):
        cosh += (x**(2*i))/(fact(2*i))
    return cosh

if __name__ == '__main__':
    print(f'approx_sin:{approx_sin( x =3.14 , n =10) }')
    print(f'approx_cos:{approx_cos( x =3.14 , n =10)}')
    print(f'approx_sinh:{approx_sinh( x =3.14 , n =10)}')
    print(f'approx_cosh:{approx_cosh( x =3.14 , n =10)}')