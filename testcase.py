from Sudoku import Sudoku
from SubBlock import SubBlock
#from Menu import Menu
import numpy as np
import random

# test용


def makeSubBlock():
    #print("makeSubBlock test")
    test = SubBlock(np.array([x for x in range(1, 10)]).reshape(3, 3))
    # 무작위 섞기
    for i in range(3):
        random.shuffle(test.subBlock[i])
    # test.printBlock()
    return test


subBlockList = np.array([makeSubBlock() for _ in range(9)]).reshape(3, 3)
# fitness function 테스트
print("##### fitness test #####")
for subBlock in subBlockList:
    for sub in subBlock:
        sub.printBlock()
    print('===============')

sudoku = Sudoku(subBlockList)
print(sudoku.calcFitness())

sudoku.printSudoku()

# 변이 테스트
print("###### mutation test #####")
problem = '007000098200604150000870002200000400005401900004000006500084000048506002690000500'
temp = np.array(list(map(int, list(problem)))).reshape(3, 3, 3, 3)
helpArray = Sudoku(np.array([[SubBlock(subblock) for subblock in subblocks] for subblocks in temp]))

sudoku.mutateSubBlock(helpArray.sudoku)
sudoku.printSudoku()
