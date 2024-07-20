import numpy as np
import soundfile as sf

class Generator:
    def __init__(self):
        pass

    def generateTestTone(self, fs, time, gainStep):
        nSamples = int(fs * time)
        nGainStep = int(1/gainStep)
        
        gainTab = np.linspace(gainStep, 1.0, nGainStep)

        length = int(nSamples * nGainStep)
        # mean = 0, sigma = 1
        self.testTone = np.random.normal(0, 1, length)

        # normalise white noise
        maxVal = np.max(np.abs(self.testTone))
        self.testTone /= maxVal

        idx = 0
        for i in range(nGainStep):
            for j in range(nSamples):
                # apply gain tab
                self.testTone[idx] *= gainTab[i]
                idx += 1

    def saveFile(self, filePath, fs):
        sf.write(filePath, self.testTone, fs)
