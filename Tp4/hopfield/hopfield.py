import numpy as np
import matplotlib.pyplot as plt
from letters import C, J, X, Z

class Hopfield:

    def __init__(self, size=5):
        self.weights = np.zeros((size * size, size * size))
        self.size = size
        self.patterns = []


    def train(self, patterns, epochs=1):
        self.patterns = patterns
        for _ in range(epochs):
            for i in range(self.size * self.size):
                for j in range(i + 1, self.size * self.size):  # i+1 para evitar autopesos
                    self.weights[i, j] += np.sum([p[i] * p[j] for p in patterns])
                    self.weights[j, i] = self.weights[i, j]  # la matriz de pesos es simétrica

        self.weights /= len(patterns)

    def calculateEnergy(self, pattern):
        energy = 0
        for i in range(self.size * self.size):
            for j in range(self.size * self.size):
                if i != j:
                    energy -= self.weights[i, j] * pattern[i] * pattern[j]
        return energy


    def recall(self, pattern, maxEpochs=10, tolerance=1e-5):
        s = np.array(pattern)
        previousEnergy = float('inf')

        for epoch in range(maxEpochs):

            currentEnergy = self.calculateEnergy(s)
            if abs(currentEnergy - previousEnergy) < tolerance:
                break

            previousEnergy = currentEnergy

            s = np.sign(np.dot(self.weights, s))
            for indx in range(len(s)):
                if s[indx] == 0:
                    s[indx] = pattern[indx]

        return s.tolist()


    def addNoise(self, pattern, noiseLevel=0.3):
        length = len(pattern)
        noisy = pattern.copy()
        for i in range(length):
            if np.random.rand() < noiseLevel:
                noisy[i] = -noisy[i]
        return noisy
    
    def plotRecallProgression(self, pattern, maxEpochs=10, tolerance=1e-5, title=""):
        s = np.array(pattern)
        previousEnergy = float('inf')
        initialEnergy = self.calculateEnergy(s)
        
        recallProgress = []
        # recallProgress = [(s.copy(), initialEnergy)]

        for epoch in range(maxEpochs):

            currentEnergy = self.calculateEnergy(s)
            if abs(currentEnergy - previousEnergy) < tolerance:
                break

            previousEnergy = currentEnergy
            recallProgress.append((s.copy(), currentEnergy))

            s = np.sign(np.dot(self.weights, s))
            for indx in range(len(s)):
                if s[indx] == 0:
                    s[indx] = pattern[indx]
        
        # Dibujar solo los subplots necesarios
        dim = int(np.sqrt(len(pattern)))
        fig, axs = plt.subplots(1, len(recallProgress), figsize=(len(recallProgress) * dim, dim))

        if len(recallProgress) == 1:
            axs = [axs]  # Para manejar el caso en que axs no sea una lista
        
        for idx, (state, energy) in enumerate(recallProgress):
            axs[idx].imshow(state.reshape((dim, dim)), cmap='gray_r')
            titleText = 'Initial' if idx == 0 else f'Epoch {idx}'
            axs[idx].set_title(f'{titleText}\nEnergy: {energy}')
            axs[idx].axis('off')

        if title:
            plt.suptitle(title + f". tolerance = {tolerance}")

        plt.tight_layout(rect=[0, 0, 1, 0.96])
        plt.show()

    def plotEnergyVsEpoch(self, pattern, maxEpochs=10, tolerance=1e-5, noiseLevel=0.2, title=""):
        noisyPattern = self.addNoise(pattern, noiseLevel)
        s = np.array(noisyPattern)
        previousEnergy = float('inf')
        
        energyList = []
        epochList = []

        for epoch in range(maxEpochs):

            currentEnergy = self.calculateEnergy(s)
            if abs(currentEnergy - previousEnergy) < tolerance:
                break

            previousEnergy = currentEnergy
            energyList.append(currentEnergy)
            epochList.append(epoch)

            s = np.sign(np.dot(self.weights, s))
            for indx in range(len(s)):
                if s[indx] == 0:
                    s[indx] = pattern[indx]

        plt.figure(figsize=(10, 5))
        plt.plot(epochList, energyList, marker='o')
        plt.xlabel("Epoch")
        plt.ylabel("Energy")
        plt.title(f"{title}")
        plt.grid(True)
        plt.show()

    def noiseEffectOnClassification(self, pattern, noiseLevels=np.linspace(0, 1, 11), maxEpochs=10, tolerance=1e-5, runsPerNoise=100):
        positives = []
        fakePositives = []
        negatives = []

        width = 0.25  # ancho de las barras
        spacing = 0.05  # espacio entre barras

        for noise in noiseLevels:
            positiveCount, fakePositiveCount, negativeCount = 0, 0, 0
            for _ in range(runsPerNoise):
                noisyPattern = self.addNoise(pattern, noise)
                recalledPattern = self.recall(noisyPattern, maxEpochs, tolerance)

                if np.array_equal(recalledPattern, pattern):
                    positiveCount += 1
                elif recalledPattern in self.patterns:
                    fakePositiveCount += 1
                else:
                    negativeCount += 1

            positives.append(positiveCount)
            fakePositives.append(fakePositiveCount)
            negatives.append(negativeCount)

        x = np.arange(len(noiseLevels))  # posiciones de las barras
        plt.figure(figsize=(12, 6))
        
        plt.bar(x - width, positives, width, label="Positive", color='g')
        plt.bar(x, fakePositives, width, label="Fake Positive", color='orange')
        plt.bar(x + width, negatives, width, label="Negative", color='r')
        
        plt.xlabel("Noise level")
        plt.ylabel("Cantidad de casos")
        plt.title("El efecto del nivel de ruido en los resultados")
        plt.xticks(x, labels=[str(round(noise, 2)) for noise in noiseLevels])
        plt.legend()
        plt.grid(True, axis='y')
        plt.tight_layout()
        plt.show()







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