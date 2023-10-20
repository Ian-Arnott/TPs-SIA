import numpy as np
import matplotlib.pyplot as plt
from letters import C, J, X, Z

class Hopfield:

    def __init__(self, size=5):
        self.weights = np.zeros((size * size, size * size))
        self.size = size


    def train(self, patterns, epochs=1):
        for _ in range(epochs):
            for i in range(self.size * self.size):
                for j in range(i + 1, self.size * self.size):  # i+1 para evitar autopesos
                    self.weights[i, j] += np.sum([p[i] * p[j] for p in patterns])
                    self.weights[j, i] = self.weights[i, j]  # la matriz de pesos es simétrica

        self.weights /= len(patterns)


    def recall(self, pattern, epochs = 10):
        s = np.array(pattern)
        for _ in range(epochs):
            s = np.sign(np.dot(self.weights, s))
            for indx in range(len(s)):
                if (s[indx]==0):
                    s[indx]=pattern[indx]
        return s.tolist()

    def addNoise(self, pattern, noiseLevel=0.2):
        length = len(pattern)
        noisy = pattern.copy()
        for i in range(length):
            if np.random.rand() < noiseLevel:
                noisy[i] = -noisy[i]
        return noisy

def exportPatterns(noisyPattern, recalledPattern, title=""):
    dim = int(np.sqrt(len(noisyPattern)))
    fig, axs = plt.subplots(1, 2, figsize=(dim, dim))
    
    axs[0].imshow(np.array(noisyPattern).reshape((dim, dim)), cmap='gray_r')
    axs[0].set_title('Noisy Pattern')
    axs[0].axis('off')

    axs[1].imshow(np.array(recalledPattern).reshape((dim, dim)), cmap='gray_r')
    axs[1].set_title('Recalled Pattern')
    axs[1].axis('off')

    if title:
        plt.suptitle(title)

    plt.show()

def displayPatterns(patternList, titles):
    dim = int(np.sqrt(len(patternList[0])))
    fig, axs = plt.subplots(1, len(patternList), figsize=(len(patternList) * dim, dim+1))
    
    for i in range(len(patternList)):
        axs[i].imshow(np.array(patternList[i]).reshape((dim, dim)), cmap='gray_r')
        axs[i].set_title(titles[i])
        axs[i].axis('off')
    
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    patterns = [C, J, X, Z]
    
    model = Hopfield(size=16)
    model.train(patterns, epochs=50)

    displayPatterns(patterns,["Letra C","Letra J","Letra X","Letra Z"])
    
    noisyC = model.addNoise(C, ttfMode=True)
    resultC = model.recall(noisyC, epochs=50)
    exportPatterns(noisyC, resultC, title="Letter C. noise level = 0.2")
    noisyC = model.addNoise(C,noiseLevel=0.1, ttfMode=True)
    resultC = model.recall(noisyC, epochs=50)
    exportPatterns(noisyC, resultC, title="Letter C. noise level = 0.1")

    noisyJ = model.addNoise(J, ttfMode=True)
    resultJ = model.recall(noisyJ, epochs=50)
    exportPatterns(noisyJ, resultJ, title="Letter J. noise level = 0.2")
    noisyJ = model.addNoise(J,noiseLevel=0.1, ttfMode=True)
    resultJ = model.recall(noisyJ, epochs=50)
    exportPatterns(noisyJ, resultJ, title="Letter J. noise level = 0.1")

    noisyX = model.addNoise(X, ttfMode=True)
    resultX = model.recall(noisyX, epochs=50)
    exportPatterns(noisyX, resultX, title="Letter X. noise level = 0.2")
    noisyX = model.addNoise(X,noiseLevel=0.1, ttfMode=True)
    resultX = model.recall(noisyX, epochs=50)
    exportPatterns(noisyX, resultX, title="Letter X. noise level = 0.1")

    noisyZ = model.addNoise(Z, ttfMode=True)
    resultZ = model.recall(noisyZ, epochs=50)
    exportPatterns(noisyZ, resultZ, title="Letter Z. noise level = 0.2")
    noisyZ = model.addNoise(Z,noiseLevel=0.1, ttfMode=True)
    resultZ = model.recall(noisyZ, epochs=50)
    exportPatterns(noisyZ, resultZ, title="Letter Z. noise level = 0.1")