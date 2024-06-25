import streamlit as st


def load_vocad(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    words = [line.strip().split('\t') for line in lines]
    return words


def levenshtein_distance(token1, token2):
    distances = [[0 for _ in range(len(token2) + 1)]
                 for _ in range(len(token1) + 1)]
    for i in range(len(token1) + 1):
        distances[i][0] = i
    for j in range(len(token2) + 1):
        distances[0][j] = j

    a = 0
    b = 0
    c = 0

    for i in range(1, len(token1) + 1):
        for j in range(1, len(token2) + 1):
            if token1[i - 1] == token2[j - 1]:
                distances[i][j] = distances[i - 1][j - 1]
            else:
                a = distances[i][j - 1]
                b = distances[i - 1][j]
                c = distances[i - 1][j - 1]
                if a <= b and a <= c:
                    distances[i][j] = a+1
                elif b <= a and b <= c:
                    distances[i][j] = b+1
                else:
                    distances[i][j] = c+1
    return distances[len(token1)][len(token2)]


def main():
    st . title("Word Correction using Levenshtein Distance")
    word = st . text_input('Word :')
    if st . button(" Compute"):
        # compute levenshtein distance
        leven_distances = dict()
        for vocab in vocabs:
            leven_distances[vocab[0]] = levenshtein_distance(word, vocab[0])
        # sorted by distance
        sorted_distences = dict(
            sorted(leven_distances . items(), key=lambda item: item[1]))
        correct_word = list(sorted_distences . keys())[0]
        st . write('Correct word :', correct_word)
        col1, col2 = st . columns(2)
        col1 . write('Vocabulary :')
        col1 . write(vocabs)
        col2 . write('Distances :')
        col2 . write(sorted_distences)


vocabs = load_vocad('./vocab.txt')


#  streamlit run task_1.py
if __name__ == "__main__":
    main()
