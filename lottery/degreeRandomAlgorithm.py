# 抽奖一次少一个名额

class randomMachine(object):
    import random as rd
    def setWeight(self, weight):
        self.weight = weight
        self.chanceList = []
        for k, v in self.weight.items():
            for t in range(v):
                self.chanceList.append(k)

    def drawing(self):
        r = self.rd.randrange(0, len(self.chanceList))  # 随机数
        print(self.chanceList.pop(r))

    def graphicsUI(self):
        pass

    def start(self):
        pass


if __name__ == "__main__":
    test = randomMachine()
    test.setWeight({"一等奖": 3, "二等奖": 1, "三等奖": 1, "安慰奖": 6})
    for i in range(9):
        test.drawing()