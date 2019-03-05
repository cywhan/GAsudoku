from Manager import Manager
from Sudoku import Sudoku
from SubBlock import SubBlock
import numpy as np


class Menu:
    def __init__(self):
        self.gaCount = 1
        self.end = False

    def run(self, problem):
        print("초기 시작")
        print("스도쿠 문제번호 : ")
        print("스도쿠 난이도 : ")
        temp = np.array(list(map(int, list(problem)))).reshape(3, 3, 3, 3)
        self.helpArray = Sudoku(np.array([[SubBlock(subblock) for subblock in subblocks] for subblocks in temp]))
        print("helpArray: ")
        self.helpArray.printSudoku()
        self.manager = Manager(self.helpArray)
        count = self.gaCount
        while not self.end: # and self.gaCount < 3:
            print("세대 : ", self.gaCount)
            print("fitness : ", self.manager.fmin)
            print("best solution: ")
            self.manager.sudokuPool[0].printSudoku()

            if count > 2000:
                self.restart()
                count = 1
            self.end = self.manager.nextGeneration()
            self.gaCount = self.gaCount + 1
            count += 1
            
        self.print()

    def restart(self):
        self.manager = Manager(self.helpArray)

    def print(self):  
        print("정답이 나왔습니다!")
        print("총 세대수 : ", self.gaCount)
        print("fitness value : ", self.manager.sudokuPool[0].fitnessValue)
        print("스도쿠 : ")
        self.manager.sudokuPool[0].printSudoku()


# 테스트용
if __name__ == "__main__":
    test = Menu()
        
    #test.run('090504731703091025016273094058103927000250316021967458319075286462089507005032109')
    #test.run('869000070147690008000017040450030090000050000090070065010520000800073421020000756')
    test.run('802060701003091000510003894608000920004258310021060400000005200402089007780000100')

# figure 6. test.run('050089000003000020900060040540000300001000207089000006000931020819000004030850700')

# fig7. test.run('790000801000000004003060002005300040000100006000000209200030000030605000006421000')