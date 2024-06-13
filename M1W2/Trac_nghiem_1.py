# Câu 1 a) [5, 5, 5, 5, 10, 12, 33, 33]
def max_kernel ( num_list , k ) :
    # Your Code Here
    result = []
    max = 1e-5
    for i in range(len(num_list)-k+1): # sliding window -k+1 phần quá biên
        for j in range(k):               # duyệt từng phần tử trong sliding window
            if max < num_list[i:i+k][j]:   # so sánh max với phần tử trong sliding window
                max = num_list[i:i+k][j]     # chọn giá trị lớn nhất
        result.append(max)
    # End Code Here
    return result

def devide(a/b):
    return a/b

if __name__ == '__main__':
    assert max_kernel ([3 , 4 , 5 , 1 , -44] , 3) == [5 , 5 , 5]
    num_list = [3 , 4 , 5 , 1 , -44 , 5 ,10 , 12 ,33 , 1]
    k = 3
    print ( max_kernel ( num_list , k ) )