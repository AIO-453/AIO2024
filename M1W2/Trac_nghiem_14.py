# Câu hỏi 14:(code) b) tocirpa
def my_function ( x ) :
    # your code here
    x_1 = x[::-1]
    return x_1
    # end code here

if __name__ == '__main__':
    x = 'I can do it'
    assert my_function (x ) =="ti od nac I"
    x = 'apricot'
    print ( my_function ( x ) )