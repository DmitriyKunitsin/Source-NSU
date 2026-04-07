loadXcosLibs();
importXcosDiagram("C:\Users\kun\sourceNSU\2semestr_Теория автоматизированного упраления\lab_2\drive-download-20260319T031919Z-1-001\lab2.zcos");
scs_m.props.context = "k1=" + "7.78" + ";";
sys = lincos(scs_m);
csim('step', 0:1:1, sys)

// частота от 0 до 10000
w = linspace(0, 10000, 500);
H = repfreq(sys, w);
plot(real(H), imag(H));
