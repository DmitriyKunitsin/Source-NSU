# Архитектура сквозного тракта обработки данных

Ниже представлена структурная схема прохождения и обработки данных от АЦП до персонального компьютера.

```mermaid
graph TD
    %% Определение узлов
    ADC([Внешний АЦП <br> <i>реальный или TPG</i>])
    
    subgraph PL [FPGA Programmable Logic]
        style PL fill:#f5faff,stroke:#0066cc,stroke-width:2px
        RX[Модуль приёма данных <br> <i>десериализация, буферизация</i>]
        DSP[Конвейер обработки <br> <i>накопление, усреднение, фильтрация</i>]
        FIFO[FIFO буфер <br> <i>согласование скоростей</i>]
    end

    DMA[AXI DMA <br> <i>передача блоками по прерыванию</i>]

    subgraph PS [Processing System ARM]
        style PS fill:#fffdeb,stroke:#cc9900,stroke-width:2px
        CPU[Обработка данных <br> <i>C-код на ARM Core</i>]
    end

    USB[Интерфейс USB <br> <i>виртуальный COM-порт</i>]
    PC([ПК <br> <i>Верхний уровень / ПО</i>])

    %% Связи и направления
    ADC --> |Данные на PL-пины или интерфейс| RX
    RX --> DSP
    DSP --> FIFO
    FIFO --> |PL &rarr; PS| DMA
    DMA --> CPU
    CPU --> |PS &rarr; ПК| USB
    USB --> PC
```
