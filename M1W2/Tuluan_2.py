def count_chars (string):
    unit = set([str(elem) for elem in string])
    dic = {}
    for i in unit:
        string.count(i)
        dic[i] = string.count(i)
    return dic
string1 = 'Happiness'
string2 = 'smiles'

if __name__ == '__main__':
    print(count_chars(string1))
    print(count_chars(string2))