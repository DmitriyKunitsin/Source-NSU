loadXcosLibs();

// правильный путь!
importXcosDiagram("C:\Users\kun\sourceNSU\2semestr_Теория автоматизированного упраления\lab_2\drive-download-20260319T031919Z-1-001\lab2.zcos");

// значения k1 (включая малые)
k1_values = [0.5, 1, 2, 5, 10, 0.3, 0.1, 0.05, 0.01];

// окно
scf(0);
clf();

// частоты
w = logspace(-2, 3, 500);

// цвета
colors = [2, 3, 5, 6, 9, 1, 4, 7, 8];

for i = 1:length(k1_values)
    k1 = k1_values(i);
    
    // добавляем параметр в контекст (ВАЖНО)
    scs_m.props.context = "k1=" + string(k1) + ";";
    
    // линеаризация
    sys = lincos(scs_m);
    
    // частотная характеристика
    H = repfreq(sys, w);
    
    // построение
    plot(real(H), imag(H), "color", colors(i));
    
end

// оформление
a = gca();
a.x_location = "origin";
a.y_location = "origin";
a.grid = [1,1];
a.title.text = "Годографы Найквиста при разных k1 (включая малые)";
a.x_label.text = "Re";
a.y_label.text = "Im";

// точка (-1,0)
plot(-1, 0, 'ro');

// легенда
legend("k1=0.5","k1=1","k1=2","k1=5","k1=10","k1=0.3","k1=0.1","k1=0.05","k1=0.01");
