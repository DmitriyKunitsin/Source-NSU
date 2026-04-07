// Загружаем модель
loadXcosLibs();
importXcosDiagram("C:\Users\kun\sourceNSU\2semestr_Теория автоматизированного упраления\lab_2\quest4_6.zcos");

k = 4.5;
T_values = [0.3, 0.5, 0.7, 1, 2, 3];

%scicos_context = struct();

// Установим время моделирования (если не задано в модели)
scs_m.props.tf = 50;

clf();
a = gca();
a.auto_clear = "off";

data = list();

for i = 1:length(T_values)
    T = T_values(i);
    %scicos_context.k = k;
    %scicos_context.T = T;
    
    // Запуск
    disp("k : " + string(%scicos_context.k) + " T : " + string(%scicos_context.T));
    scicos_simulate(scs_m, list(), %scicos_context);
    
    // Проверка создания переменной
    if exists('simOut') == 1 then
        disp("T = " + string(T) + ", размер time = " + string(length(simOut.time)));
        if length(simOut.time) > 0 then
            data($+1) = list(simOut.time, simOut.values);
        else
            warning("Для T = " + string(T) + " данные пусты");
        end
    else
        warning("simOut не создана для T = " + string(T));
    end
end


if length(data) > 0 then
    clf();
    for i = 1:length(data)
        plot(data(i)(1), data(i)(2), 'LineWidth', 2);
    end
    xlabel('Время, с');
    ylabel('Выход');
    title('Переходные процессы при разных T');
    legend(string(T_values));
    xgrid();
else
    disp("Нет данных для построения графика.");
end
