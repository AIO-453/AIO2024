# câu 12 a) [3, 6]
def my_function ( data ) :
    var = []
    for i in data :
    # Your code here
    # Neu i chia het cho 3 thi them i vao list var
        if i % 3 == 0:
            var.append(i)
    # Neu i chia het cho 3 thi them i vao list var
    return var




if __name__ == '__main__':
    assert my_function ([3 , 9 , 4 , 5]) == [3 , 9]
    print ( my_function ([1 , 2 , 3 , 5 , 6]) )