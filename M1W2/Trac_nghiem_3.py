# câu 3 c) 6
def count_word ( file_path ) :
    # Your Code Here
    counter = {}
    f = open(file_path)
    f = f.read()
    lis = f.lower().split()
    unit = set([str(elem) for elem in lis])
    for i in unit:
        lis.count(i)
        counter[i] = lis.count(i)    
    # End Code Here
    return counter

if __name__ == '__main__':
    file_path = '.\M1W2\P1_data.txt'
    result = count_word ( file_path )
    assert result ['who'] == 3
    print ( result ['man'])