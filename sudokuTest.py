from Sudoku import Sudoku
from SubBlock import SubBlock
import numpy as np
import random

# test용


def makeSubBlock():
    test = SubBlock(np.array([x for x in range(1, 10)]).reshape(3, 3))
    # 무작위 섞기
    for i in range(3):
        random.shuffle(test.subBlock[i])
    # test.printBlock()
    return test


subBlockList = np.array([makeSubBlock() for _ in range(9)]).reshape(3, 3)

sudoku = Sudoku(subBlockList)
print(sudoku.testFunction())
