# Câu hỏi 13:(code) c) 24
def my_function ( y ) :
    var = 1
    while ( y > 1) :
    # Your code here
        var = var*y
        y = y-1
    # End Code Here
    return var

if __name__ == '__main__':
    assert my_function (8) == 40320
    print ( my_function (4))