# câu 8 c) -1
def my_function ( n ) :
    # Your code here
    min = 1e10
    for i in range(len(n)):
        if min > n[i]:
            min = n[i]
    return min

if __name__ == '__main__':
    my_list = [1 , 22 , 93 , -100]
    assert my_function ( my_list ) == -100
    my_list = [1 , 2 , 3 , -1]
    print ( my_function ( my_list ) )