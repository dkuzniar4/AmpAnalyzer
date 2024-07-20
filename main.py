import tkinter as tk
import os
from tkinter import filedialog
from Analyzer import Analyzer
from Generator import Generator

# global parameters
fs = 48000
time = 0.1
gainStep = 0.05


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.gen = Generator()
        self.an = Analyzer()
        self.createGUI()

    def createGUI(self):
        self.title("Amp analyzer v1.0")
        self.geometry("340x370")
        self.resizable(False, False)
        self.configure(bg="black")

        self.step1Label = tk.Label(self, text="Step 1: Generate test tone, put it through amp and record output. Cut recording to the same length as test tone and save it in wav file", wraplength=320, bg="black", fg="white")
        self.step1Label.place(x= 10, y=10)

        # generate button
        self.generateButton = tk.Button(self, text="Generate test tone", bg="orange", fg="black", command=self.chooseFileToSave)
        self.generateButton.place(x=10, y=70)

        self.step2Label = tk.Label(self, text="Step 2: Load output wav", wraplength=320, bg="black", fg="white")
        self.step2Label.place(x= 10, y=120)
        
        self.loadFileButton = tk.Button(self, text="Load file", bg="orange", fg="black", command=self.chooseFileToLoad)
        self.loadFileButton.place(x=10, y=150)
        
        self.fileInfoText = tk.Text(self, height=2, width=30)
        self.fileInfoText.place(x=10, y=190)

        self.step3Label = tk.Label(self, text="Step 3: Show 3D FFT figure of frequency vs gain", wraplength=320, bg="black", fg="white")
        self.step3Label.place(x=10, y=260)

        # type axix radio (exp, lin)
        self.typeLabel = tk.Label(self, text="Freq axis:", bg="black", fg="white")
        self.typeLabel.place(x=10, y=290)
        self.typeVar = tk.StringVar(value="exp")
        self.typeRadio1 = tk.Radiobutton(self, text="exp", variable=self.typeVar, value="exp", command=self.updateAxis)
        self.typeRadio1.place(x=100, y=290)
        self.typeRadio2 = tk.Radiobutton(self, text="lin", variable=self.typeVar, value="lin", command=self.updateAxis)
        self.typeRadio2.place(x=170, y=290)
        self.updateAxis()

        # show figure button
        self.showFigureButton = tk.Button(self, text="Show 3D figure", bg="orange", fg="black", command=self.showFigure)
        self.showFigureButton.place(x=10, y=320)


    def chooseFileToLoad(self):
        filePath = filedialog.askopenfilename(
            title="Load WAV file",
            filetypes=(("Wav files", "*.wav"),)
        )
        self.an.loadFile(filePath)
        self.fileInfoText.delete("1.0", tk.END)
        self.fileInfoText.insert(tk.END,
        f"File: {os.path.basename(filePath)}\n"
        f"Sample rate: {self.an.sampleRate} Hz\n")
        self.an.prepareFigure(fs, time, gainStep)

    def chooseFileToSave(self):
        filePath = filedialog.asksaveasfilename(
            title="Save testTone",
            filetypes=(("Wav files", "*.wav"),)
        )
        self.gen.generateTestTone(fs, time, gainStep)
        self.gen.saveFile(filePath, fs)

    def updateAxis(self):
        self.type = self.typeVar.get()

    def showFigure(self):
        self.an.showFigure(self.type)



if __name__ == "__main__":
    app = App()
    app.mainloop()
