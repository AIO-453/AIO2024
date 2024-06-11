# Câu 2 a) 's': 2, 'm': 1, 'i': 1, 'l': 1, 'e': 1
def character_count ( word ) :
    character_statistic = {}
    # Your Code Here
    unit = set([str(elem) for elem in word])
    character_statistic = {}
    for i in unit:
        word.count(i)
        character_statistic[i] = word.count(i)
    # End Code Here
    return character_statistic

if __name__ == '__main__':
    assert character_count ("Baby") == {'B': 1 , 'a': 1 , 'b': 1 , 'y': 1}
    print ( character_count ('smiles') )