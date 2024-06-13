# Câu 11 a) 1.0
def my_function ( list_nums = [0 , 1 , 2]) :
    var = 0
    for i in list_nums :
        var += i
    return var/len(list_nums)# Your code here : Tra ve gia tri trung binh cua list bang cach chia var cho luong phan tu trong list_mums

if __name__ == '__main__':
    assert my_function ([4 , 6 , 8]) == 6
    print ( my_function ())
