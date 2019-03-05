import numpy as np
import random


class SubBlock:
    '''
    subBlock : numpy array[3][3]
    get(row, collumn) : subBlock안의 인덱스 위치 숫자 반환
    mutation(helpBlock) : 유전자 알고리즘 변이 연산 수행
    printBlock() : subBlock 출력'''
    def __init__(self, subBlock):            # subBlock : numpy array[3][3]
        self.subBlock = subBlock
        
    def get(self, row, column):
        return self.subBlock[row][column]

    def mutation(self, helpblock):  # helpblock : numpy subBlock[3][3]
        swapCount = random.randrange(1, 6)
        helpBlock = helpblock
        i = 0
        while i < swapCount:
            swapOne = (random.randrange(0, 3), random.randrange(0, 3))
            swapTwo = (random.randrange(0, 3), random.randrange(0, 3))
            if swapOne[0] == swapTwo[0] and swapOne[1] == swapTwo[1]:
                i -= 1
                continue
            if helpBlock.subBlock[swapOne[0]][swapOne[1]] != 0 or helpBlock.subBlock[swapTwo[0]][swapTwo[1]] != 0:
                break
            self.subBlock[swapOne[0]][swapOne[1]], self.subBlock[swapTwo[0]][swapTwo[1]] = self.subBlock[swapTwo[0]][swapTwo[1]], self.subBlock[swapOne[0]][swapOne[1]]
            i += 1

    def printBlock(self):
        '''
        for i in range(1, 4):
            for j in range(0, 3):
                print(self.subBlock[i*j], end='')
            print()
        '''
        print(self.subBlock)


# 테스트용
if __name__ == "__main__":
    test = SubBlock(np.array([x for x in range(1, 10)]).reshape(3, 3))
    #print("test = ", test.subBlock)
    #random.shuffle(test.subBlock)
    test.printBlock()
    helpBlock = np.array([0, 0, 0, 3, 0, 5, 0, 0, 0]).reshape(3, 3)
    print("helpBlock = ", helpBlock)
    test.mutation(helpBlock)
    test.printBlock()

