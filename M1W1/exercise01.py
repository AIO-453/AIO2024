import math
import numpy as np

def Precision(TP,FP):
    return TP/(TP+FP)

def Recall(TP,FN):
    return TP/(TP+FN)

def F1_score(TP,FP,FN):
    return 2*TP/(2*TP+FP+FN)

def exercise(TP,FP,FN):
    seed = [[TP,FP,FN],
            ['TP','FP','FN'],
            ["","",""],  # int
            ["","",""],] # x<=0
    for i in range(3):
      if not isinstance(seed[0][i], int):
        seed[2][i] = seed[1][i]
      if seed[0][i]<=0:
        seed[3][i]= seed[1][i]
    if seed[2] == ["","",""] and seed[3] == ["","",""]:
      return print(f'Precision is {Precision(TP,FP)} \nrecall is {Recall(TP,FN)} \nF1-score is {F1_score(TP,FP,FN)}\n')
    else:
      if seed[2] != ["","",""]:
        try:
          seed[2].pop(seed[2].index(""))
          string1 = ', '.join([str(elem) for elem in seed[2]])
          string1 = string1[2:] if string1[0] == ',' else string1
          string1 = string1[:-2] if string1[-2] == ',' else string1
          print(f"{string1} must be int \n")
        except:
          string1 = ', '.join([str(elem) for elem in seed[2]])
          string1 = string1[2:] if string1[0] == ',' else string1
          string1 = string1[:-2] if string1[-2] == ',' else string1
          print(f"{string1} must be int \n")
      if seed[3] != ["","",""]:
        try:
          seed[3].pop(seed[3].index(""))
          string2 = ', '.join([str(elem) for elem in seed[3]])
          string2 = string2[2:] if string2[0] == ',' else string2
          string2 = string2[:-2] if string2[-2] == ',' else string2
          print(f"{string2} must be great than zero \n")
        except:
          string2 = ', '.join([str(elem) for elem in seed[3]])
          string2 = string2[2:] if string2[0] == ',' else string2
          string2 = string2[:-2] if string2[-2] == ',' else string2
          print(f"{string2} must be great than zero \n")


if __name__ == '__main__':
    print('----------------------------------------')
    exercise(TP=1,FP=2,FN=3)
    print('----------------------------------------')
    exercise(TP=0,FP=2,FN=0.22)
    print('----------------------------------------')
    exercise(TP=0,FP=0,FN=0)
    print('----------------------------------------')
    exercise(TP=0.1,FP=0.2,FN=0.22)
    print('----------------------------------------')


