import numpy as np


def BYtrain(trainY=None, trainX=None):
   
    N, M = np.shape(trainX, )  # M为输入样本特征数,N为样本数，获取行列数，N行M列。
    afa = M / np.var(trainY, 1)

    beta = (np.var(trainY, 1))**(-1)

    W = np.zeros((M, 1))

    updatetimes = 30

    for i in np.range(1, updatetimes+1):
        gamu = 0

        Sn = np.linalg.pinv(
            np.dot(afa, (np.eye(M))) +
            np.dot(np.dot(beta, trainX.T), trainX))

        Mn = np.dot(np.dot(np.dot(beta, Sn), trainX.T), trainY)

        V, lamd = np.linalg.eig(np.dot(np.dot(beta, trainX.T), trainX))

        for j in np.range(1, M+1):
            gamu = gamu + lamd(j, j) / (afa + lamd(j, j))
            afa = gamu / (np.dot(Mn.T, Mn))
            beta = (N - gamu) / (
                np.sum(trainY - np.power(np.dot(trainX, Mn), 2))
            )  # np.sum输出为标量，np.power按元素求幂

    W = Mn.copy()
