# Amp analyzer v1.0
Tool for creating 3D FFT characteristics vs. gain.
It show how guitar amps behave with different gain level with connection to frequency characteristic.

Before use this tool you should install dependencies:

pip install -r requirements.txt

1. In GUI you can generate test tone, load processed output wav file, choose exponential or linear 3D figure.

![alt](<Docs/Images/gui.png>)
--------------------------------------------------

2. Generated test tone is passing thorough the guitar amplifier (real amp or amp sim), then recorded output should be cutted to the same length as test tone. Also cut should be proper select. To do it you can use Audacity.

![alt](<Docs/Images/audacity.png>)

Output should be save in mono wav file and load into Amp analyzer.


3. After all press "Show 3d figure". In your browser you can see 3D FFT cube figure. It shows how guitar amp behave with different gain vs. frequency characteristics.


   ![alt](<Docs/Images/figure.png>)
