from Sudoku import Sudoku
from SubBlock import SubBlock
import random
import copy
import numpy as np
import math


class Manager:
    '''
    printAll : 유전자 풀에 있는 모든 솔루션 출력
    GACrossOver : 두 부모로부터 자식 생성
    GAMutateSudoku : 자식 변이
    GASelectSudoku : 두 부모 선택
    nextGeneration : 다음 세대로 진행
    '''
    def __init__(self, sudoku):    # sudoku : numpy array[81]
        self.helpArray = sudoku  # helpArray: Sudoku
        self.sudokuPool = []  # sudokuPool: Sudoku[21]
        self.generation = 0  # generation: default 0 int
        self.fmin = 1000  # fmin: default 1000 int
        self.K = 0  # K : 상수

        standard = np.array([x for x in range(1, 10)])
        
        for i in range(0, 21):
            tmp_sudoku = copy.deepcopy(self.helpArray)
            tmp_sudoku.sudoku = tmp_sudoku.sudoku.reshape(1, 9)
            for j in range(9):
                sub_cell = tmp_sudoku.sudoku[0, j]
                sub_cell.subBlock = sub_cell.subBlock.reshape(1, 9)
                cell = np.setdiff1d(standard, sub_cell.subBlock)
                random.shuffle(cell)
                cell = cell.tolist()
                for k in range(9):
                    if sub_cell.subBlock[0, k] == 0:
                        sub_cell.subBlock[0, k] = cell.pop()
                sub_cell.subBlock = sub_cell.subBlock.reshape(3, 3)
                tmp_sudoku.sudoku[0, j] = sub_cell
            tmp_sudoku.sudoku = tmp_sudoku.sudoku.reshape(3, 3)
            self.sudokuPool.append(tmp_sudoku)
            

    def printAll(self):
        print("실행중...")
        print()
        print("세대수 : ", self.generation)
        for i in range(0, 21):
            print("번호 : ", i)
            print("fitness value : ", self.sudokuPool[i].fitnessValue)
            self.sudokuPool[i].printSudoku()
            print("----------------------------------")
        return

    def GACrossOver(self, x1, x2, target):    # x1, x2, target : int
        child = copy.deepcopy(self.helpArray)
        for r in range(0, 3):
            for c in range(0, 3):
                if random.random() < 0.5:
                    child.sudoku[r, c] = self.sudokuPool[x1].sudoku[r, c]
                else:
                    child.sudoku[r, c] = self.sudokuPool[x2].sudoku[r, c]

        self.sudokuPool[target] = child
        return

    def GASelectSudoku(self):  # 논문의 알고리즘 구현.
        for i in range(21, 1, -1):
            x1 = math.floor(i * random.random())
            x2 = math.floor(i * random.random())

            self.GACrossOver(x1, x2, i-1)

        return

    def GAMutateSudoku(self):  # 스도쿠 변이
        
        tmp_sudoku = copy.deepcopy(self.sudokuPool[0])
        for i in range(1, 21):
            self.sudokuPool[i].mutateSubBlock(self.helpArray.sudoku)
        self.sudokuPool[0] = tmp_sudoku
        return

    def nextGeneration(self):  # 다음 세대로 넘어가기 : return boolean
        self.generation += 1
        old = self.sudokuPool[0].fitnessValue
        fmin_index = 0
        minValue = 1000
        # 21개 f구하기 (sudoku의 calcFitness)
        # { sudokuPool에 fitness가 0인게 있으면 return True }
        for i in range(0, 21):
            self.sudokuPool[i].calcFitness()
            if self.sudokuPool[i].fitnessValue == 0:
                tmp1 = self.sudokuPool[i]
                self.sudokuPool[i] = self.sudokuPool[0]
                self.sudokuPool[0] = tmp1
                return True
            if i == 0:
                minValue = self.sudokuPool[i].fitnessValue
            elif self.sudokuPool[i].fitnessValue < minValue:
                fmin_index = i
                minValue = self.sudokuPool[i].fitnessValue


        # 제일 작은 값을 0번째에 저장.
        tmp = self.sudokuPool[0]
        self.sudokuPool[0] = self.sudokuPool[fmin_index]
        self.sudokuPool[fmin_index] = tmp
        # 02.26 시환) self.sudokuPool[0], self.sudokuPool[fmax_index] = self.sudokuPool[fmax_index], self.sudokuPool[0] 로 변경가능

        # best value가 이전 세대거랑 같으면 패널티값 1추가
        #if self.sudokuPool[0] == old:
        #    self.sudokuPool[0].fitnessValue += 1

        self.fmin = self.sudokuPool[0].fitnessValue
        # self.printAll()

        # 21개 교차연산으로 자식세대 구하기(구한다음 fitness값이 초기값임)
        self.GASelectSudoku()
        # print("[fitness test]")
        # for i in range(0,21):
        #     print(self.sudokuPool[i].fitnessValue)
        # print("[END test]")

        # 자식 유전자 변이
        self.GAMutateSudoku()

        return False
