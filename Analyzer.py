import soundfile as sf
import numpy as np
import plotly.graph_objects as go

# global parameters
fftLength = 2048
startIdx = 1000
endIdx = startIdx + fftLength

class Analyzer:
    def __init__(self):
        pass

    def loadFile(self, filePath):
        self.filePath = filePath
        self.inputData, self.sampleRate = sf.read(self.filePath)
        
    def prepareFigure(self, fs, time, gainStep):
        nSamples = int(fs * time)
        nGainStep = int(1/gainStep)
        self.gainTab = np.linspace(gainStep, 1.0, nGainStep)

        # prepare freq axis
        self.freqAxis = np.fft.fftfreq(fftLength, 1/fs)
        self.freqAxis = self.freqAxis[:fftLength//2]

        # select clip data to fft
        self.inputData = np.reshape(self.inputData, (nGainStep, nSamples))
        self.inputData = self.inputData[:, startIdx:endIdx]

        self.fftMag = np.empty((nGainStep, fftLength//2))
        window = np.hanning(fftLength)

        for i in range(len(self.gainTab)):
            # normalise
            self.inputData[i] /= self.gainTab[i]
            # windowing
            self.inputData[i] *= window
            # FFT
            fft = np.fft.fft(self.inputData[i])
            self.fftMag[i] = np.abs(fft[:fftLength//2])
            # to dB
            self.fftMag[i] = 20 * np.log10(self.fftMag[i])

    def showFigure(self, type):
        fig = go.Figure(data=[go.Surface(z=self.fftMag, x=self.freqAxis, y=self.gainTab*100, colorscale='portland')])
        if type == "exp":
            fig.update_scenes(xaxis_type="log")
        elif type == "lin":
            fig.update_scenes(xaxis_type="linear")
        fig.update_layout(title="3D frequency characteristics", autosize=True,
            scene_aspectmode="cube", scene=dict(xaxis_title="frequency [Hz]", yaxis_title="gain [%]", zaxis_title="amplitude [dB]"))
        fig.show()
