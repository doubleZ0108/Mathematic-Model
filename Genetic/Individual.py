# -*- coding: utf-8 -*-

'''
@program: Individual.py

@description: 

@author: doubleZ

@create: 2020/02/08 
'''

import numpy.random as npr

class Individual:
    eval = 0.0
    chromsome = None

    def __init__(self, n):
        self.chromsome = npr.random(n)

    def __init__(self, popu, dimension, crossoverProb, mutationProb, maxIterTime, evalFunc):
        for _ in range(popu):       # 初始化种群，生成种群中的每个个体
            oneInd = Individual(dimension)
            oneInd.eval = evalFunc(oneInd.chromsome)    # 评估优劣
            self.population.append(oneInd)
        self.crossoverProb = crossoverProb  # 交叉概率
        self.mutationProb = mutationProb    # 变异概率
        self.maxIterTime = maxIterTime      # 最大代数
        self.evalFunc = evalFunc            # 评估函数
        self.popu = popu                    # 种群中个体的数量
        self.dimension = dimension          # 优化参数的个数

    def findBestWorst(self):
        worst = best = self.population[0].eval
        worstPos = bestPos = 0
        for i in range(1, self.popu):
            if best > self.population[i].eval:
                bestPos = i
                best = self.population[i].eval
            if worst < self.population[i].eval:
                worstPos = i
                worst = self.population[i].eval
        self.bestPos = bestPos
        self.worstPos = worstPos

    def mutation(self):
        father = self.population[npr.randint(self.popu)]
        son = Individual(self.dimension)
        son.chromsome = father.chromsome.copy()
        mutationPos = npr.randint(self.dimension)

        temp = npr.random() - 0.5
        son.chromsome[mutationPos] += self.arfa * temp
        son.eval = self.evalFunc(son.chromsome)
        self.findBestWorst()
        if son.eval < self.population[self.worstPos].eval:
            self.population[self.worstPos] = son

    def solve(self):
        shrinkTimes = self.maxIterTime / 10
        oneFold = shrinkTimes
        i = 0
        while i < self.maxIterTime:
            print(i, "---", self.maxIterTime)
            if i == shrinkTimes:
                self.arfa = self.arfa / 2.0
                shrinkTimes += oneFold

                for j in range(self.crossoverProb):
                    self.crossover()
                for j in range(self.mutationProv):
                    self.mutation()

def f1(v):
    f = (v[0] - 4) ** 2 + 2 * (v[1] + 3) ** 2 + (v[2] - 4) ** 2
    return f

if __name__ == '__main__':
    nga = Individual(10, 3, 0, 90, 10000, f1)
    nga.solve()