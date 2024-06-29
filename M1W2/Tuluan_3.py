def word_count(file_path):
    f = open(file_path)
    f = f.read()
    lis = f.lower().split()
    unit = set([str(elem) for elem in lis])
    dic = {}
    for i in unit:
        lis.count(i)
        dic[i] = lis.count(i)
    return dic

file_path = '.\M1W2\P1_data.txt'
if __name__ == '__main__':
    dic = word_count(file_path)
    print(dic)
# C:\Users\Admin\OneDrive\Desktop\file code\python\Module1\M1W2\P1_data.txt