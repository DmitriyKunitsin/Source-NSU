// Загружаем модель
loadXcosLibs();
importXcosDiagram("C:\Users\kun\sourceNSU\2semestr_Теория автоматизированного упраления\lab_2\drive-download-20260319T031919Z-1-001\lab2.zcos");

// Заданные параметры (константы)
k1 = 2;
k2 = 1;
T2 = 0.1;
k3 = 2;
T3 = 0.8;

// Диапазон значений d для исследования
d_values = [0.15, 0.2, 0.2328, 0.25, 0.3];

// Устанавливаем время моделирования
scs_m.props.tf = 50;

// Подготовка графического окна
scf(0);
clf();
a = gca();
a.auto_clear = "off";

data = list();

// цвета
colors = [2, 3, 5, 6, 9, 1, 4, 7, 8];

for i = 1:length(d_values)
    d = d_values(i); 
    // Формируем строку контекста со всеми переменными
    context_str = "k1=" + string(k1) + ";" + ...
                  "k2=" + string(k2) + ";" + ...
                  "T2=" + string(T2) + ";" + ...
                  "k3=" + string(k3) + ";" + ...
                  "T3=" + string(T3) + ";" + ...
                  "d=" + string(d) + ";";
    scs_m.props.context = context_str;

    // Запуск симуляции
    scicos_simulate(scs_m, list());
    
    if exists('simOut') == 1 then
        // Извлекаем данные
        time = simOut.time;
        values = simOut.values;

        // Проверяем, что данные не пусты
        if length(time) > 0 then
            // Сохраняем в список
            data($+1) = list(time, values);
        else
            warning("Для d = " + string(d) + " данные пусты");
        end
    else
        warning("simOut не создана для d = " + string(d));
    end
end

// Построение графиков
if length(data) > 0 then
    clf(); // очищаем окно перед финальным построением
    for i = 1:length(data)
        plot(data(i)(1), data(i)(2), 'LineWidth', 2);
    end

    // Оформление
    xlabel('Время, с');
    ylabel('Выходной сигнал');
    title('Переходные процессы при разных d');
    legend(string(d_values));  // легенда из значений d
    xgrid();
else
    disp("Нет данных для построения графика.");
end
