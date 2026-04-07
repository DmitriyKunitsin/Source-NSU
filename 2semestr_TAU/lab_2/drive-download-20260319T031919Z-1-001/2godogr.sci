loadXcosLibs();
importXcosDiagram("C:\Users\Murav\Downloads\lab2\lab2.zcos");

// значения коэффициента
k_values = [2 5 7.78 10 15];

// частотный диапазон
w = logspace(-2, 2, 500);

// --- ГОДОГРАФ НАЙКВИСТА ---
scf(0); clf();
for k1 = k_values
    
    scs_m.props.context = "k1=" + string(k1) + ";";
    
    sys = lincos(scs_m);
    H = sys(2); // передаточная функция
    
    // частотная характеристика
    [re, im] = nyquist(H, w);
    
    plot(re, im);
    xtitle("Годограф Найквиста");
    xlabel("Re");
    ylabel("Im");
    
    // подписи
    xstring(re($), im($), "k1=" + string(k1));
end


// --- ГОДОГРАФ МИХАЙЛОВА ---
scf(1); clf();
for k1 = k_values
    
    scs_m.props.context = "k1=" + string(k1) + ";";
    
    sys = lincos(scs_m);
    H = sys(2);
    
    // знаменатель (характеристический полином)
    [num, den] = tf2ss(H);
    p = poly(den, "s");
    
    // вычисление значений полинома на jω
    s = %i * w;
    P = horner(p, s);
    
    plot(real(P), imag(P));
    xtitle("Годограф Михайлова");
    xlabel("Re");
    ylabel("Im");
    
    xstring(real(P($)), imag(P($)), "k1=" + string(k1));
end