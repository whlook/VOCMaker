# coding:utf-8

import os
if __name__ == '__main__':
    path = os.getcwd()
    dataAnnotated = os.listdir(path + '\\Annotations')
    dataNum = len(dataAnnotated)  # 数据集数量

    ftest = open('ImageSets/Main/test.txt', 'w')  # 测试集
    ftrain = open('ImageSets/Main/train.txt', 'w')  # 训练集
    ftrainval = open('ImageSets/Main/trainval.txt', 'w')  # 训练验证集
    fval = open('ImageSets/Main/val.txt', 'w')  # 验证集
    testScale = 0.5  # 测试集占总数据集的比例
    trainScale = 0.5  # 训练集占训练验证集的比例

    i = 1
    testNum = int(dataNum * testScale)  # 测试集的数量
    trainNum = int((dataNum - testNum) * trainScale)  # 训练集的数量

    for name in dataAnnotated:
        if i <= testNum:
            print>>ftest, name[0:6]
        elif i <= testNum + trainNum:
            print>>ftrain, name[0:6]
            print>>ftrainval, name[0:6]
        else:
            print>>fval, name[0:6]
            print>>ftrainval, name[0:6]
        i += 1
    ftrain.close
    ftrainval.close
    fval.close
    ftest.close
    print 'done!'
