# câu 5 a) True
def check_the_number ( N ) :
    list_of_numbers = []
    result = ""
    for i in range (1 , 5) :
        # Your code here
        list_of_numbers.append(i)
        #Su dung append them i vao trong list_of_number
    if N in list_of_numbers :
        results = "True"
    if N not in list_of_numbers :
        results = "False"
    return results

if __name__ == '__main__':
    N = 7
    assert check_the_number ( N ) == "False"
    N = 2
    results = check_the_number ( N )
    print ( results )