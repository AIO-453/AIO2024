# Câu hỏi 15:(code) c) [’T’, ’T’, ’T’, ’N’]
def function_helper ( x ) :
    # Your code here
    # Neu x >0 tra ve 'T ', nguoc lai tra ve 'N'
    if x > 0:
        return 'T'
    else:
        return 'N'
    # End Code Here
def my_function ( data ) :
    res = [ function_helper ( x ) for x in data ]
    return res

if __name__ == '__main__':
    data = [10 , 0 , -10 , -1]
    assert my_function ( data ) == ['T', 'N', 'N', 'N']
    data = [2 , 3 , 5 , -1]
    print ( my_function ( data ) )