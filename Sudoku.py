
import numpy as np
import collections
from SubBlock import SubBlock


class Sudoku:
    '''
    sudoku : numpy subBlock[3][3]
    fitnessValue : 적합도 값
    helpTableRow/Column : 같은수가 4개이상인지 체크용(mutateSubBlock에서 구현해야함)
    calcFitness : 스도쿠 전체의 fitness 값 구하기
    calcRow/ColumnFitness : 한 행/열 의 fitness 값 구하기
    mutateSubBlock : 스도쿠 전체 변이 실행
    '''
    def __init__(self, sudoku):
        self.sudoku = sudoku            # numpy subBlock[3][3]
        self.fitnessValue = -1
        self.helpTableRow = np.zeros(9)
        self.helpTableColumn = np.zeros(9)

    def calcFitness(self):
        result = 0
        for i in range(0, 9):
            result += self.calcRowFitness(i)
            result += self.calcColumnFitness(i)
        if self.fitnessValue != -1:
            self.fitnessValue = self.fitnessValue + 1        #기존 result -> + self.fitnessvalue+ 1
        else:
            self.fitnessValue = result
        #print("fitness : ", self.fitnessValue)

    def testFunction(self):
        print(self.sudoku.shape)
        print(self.sudoku[0][0].printBlock())
        print(self.sudoku[0][0].get(0, 0))

    def calcRowFitness(self, row):
        A = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
        sudokuRow = row // 3
        subBlockRow = row % 3
        for i in range(0, 3):
            for j in range(0, 3):
                A = A - set([self.sudoku[sudokuRow][i].get(subBlockRow, j)])
        return len(A) * 2

    def calcColumnFitness(self, column):
        A = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
        sudokuColumn = column // 3
        subBlockColumn = column % 3
        for i in range(0, 3):
            for j in range(0, 3):
                A = A - set([self.sudoku[i][sudokuColumn].get(j, subBlockColumn)])
        return len(A) * 2

    def mutateSubBlock(self, helpArray):
        for i in range(0, 3):
            for j in range(0, 3):
                oldBlock = self.sudoku[i][j].subBlock
                self.sudoku[i][j].mutation(helpArray[i][j])
                for k in range(0, 3):
                    if self.rowCheckCounter(int(3*i+k)):
                        self.sudoku[i, j].subBlock = oldBlock
                        print("rowCheckCounter executed")
                        break
                    if self.columnCheckCounter(int(3*j+k)):
                        self.sudoku[i, j].subBlock = oldBlock
                        print("ColumnCheckCounter executed")
                        break
        
    # 스도쿠의 row 행의 숫자들을 checkRow라는 하나의 긴 np.array로 만들고
    # checkRow를 값: 개수인 collection으로 만들고 체크
    def rowCheckCounter(self, row):
        sudokuRow = row // 3
        subBlockRow = row % 3
        
        checkRow = np.hstack((self.sudoku[sudokuRow, 0].subBlock[subBlockRow], self.sudoku[sudokuRow, 1].subBlock[subBlockRow]))
        checkRow = np.hstack((checkRow, self.sudoku[sudokuRow, 2].subBlock[subBlockRow]))                    
        counter = collections.Counter(checkRow)
        
        for key in counter:
            if counter[key] > 3:
                return True
        return False

    def columnCheckCounter(self, column):
        sudokuColumn = column // 3
        subBlockColumn = column % 3
        checkColumn = np.hstack((self.sudoku[0, sudokuColumn].subBlock[:,subBlockColumn], self.sudoku[1, sudokuColumn].subBlock[:,subBlockColumn]))
        checkColumn = np.hstack((checkColumn, self.sudoku[2, sudokuColumn].subBlock[:,subBlockColumn]))
        
        counter = collections.Counter(checkColumn)
        
        for key in counter:
            if counter[key] > 3:
                return True
        return False
        

    def printSudoku(self):
        '''
        for i in range(0, 3):
            for j in range(0, 3):
                for k in range(0, 3):
                    for l in range(0, 3):
                        print(self.sudoku[i][k][j][l], end='')
                    print(' ', end='')
                print()
            print()
        
        for i in range(0, 3):
            for j in range(0, 3):
                self.sudoku[i][j].printBlock()
        '''
        for i in range(0, 9):
            self.printRow(i)
                
    def printRow(self, row):
        sudokuRow = row // 3
        subBlockRow = row % 3
        
        checkRow = np.hstack((self.sudoku[sudokuRow, 0].subBlock[subBlockRow], self.sudoku[sudokuRow, 1].subBlock[subBlockRow]))
        checkRow = np.hstack((checkRow, self.sudoku[sudokuRow, 2].subBlock[subBlockRow]))                    
        print(checkRow)

                
                
