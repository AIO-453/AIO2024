# câu 10 c) True
def My_function ( integers , number = 1) :
    return any([i==number for i in integers])

if __name__ == '__main__':
    my_list = [1 , 3 , 9 , 4]
    assert My_function ( my_list , -1) == False
    my_list = [1 , 2 , 3 , 4]
    print ( My_function ( my_list , 2) )