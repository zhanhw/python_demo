class randomMachine(object):
    import random as rd
    def setWeight(self, weight):
        self.weight = weight
        WEIGHT = {}
        weightLength = len(self.weight)  # 权重个数
        valueCount = 0  # 权重合计
        for v in self.weight.values():
            valueCount += v
        for k, v in self.weight.items():
            WEIGHT[k] = 1000000 * v / valueCount  # 一百万乘以权重所占百分比
            # 区间 [1,400000,400000+600000]
        self.compare = {"FIRST_PART": 0}
        tmp = 0
        for k, v in WEIGHT.items():
            tmp += v
            self.compare[k] = tmp

    def drawing(self):
        r = self.rd.randrange(1, 1000001)  # 随机数
        tmp = 0
        name = ''
        for k, v in self.compare.items():
            if r <= v:
                if tmp == 0:  # 第一次判断
                    tmp = v
                    name = k
                if v < tmp:
                    tmp = v
                    name = k

        print(name)
        self.weight[k] -= 1  # 每次执行少一次奖励

    def graphicsUI(self):
        pass

    def start(self):
        pass


if __name__ == "__main__":
    test = randomMachine()
    test.setWeight({"一等奖": 1, "二等奖": 1, "三等奖": 1, "安慰奖": 6})
    for i in range(9):
        test.drawing()