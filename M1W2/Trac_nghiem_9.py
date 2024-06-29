# câu 9 d) 9
def my_function ( n ) :
    # Your code here
    max = -1e10
    for i in range(len(n)):
        if max < n[i]:
            max = n[i]
    return max
my_list = [1001 , 9 , 100 , 0]

if __name__ == '__main__':
    assert my_function ( my_list ) == 1001
    my_list = [1 , 9 , 9 , 0]
    print ( my_function ( my_list ) )