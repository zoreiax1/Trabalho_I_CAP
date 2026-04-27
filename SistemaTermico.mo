package SistemaTermico
  model TanqueAquecimentoTubulacao
    // PARÂMETROS FÍSICOS (Conforme modelo Python do professor)
    parameter Integer n = 5 "Número de segmentos para discretização da tubulação";
    parameter Real V = 20 "Volume do tanque (m3)";
    parameter Real Vt = 5 "Volume total da tubulação (m3)";
    parameter Real Qmax = 16000 "Potência nominal de aquecimento (800 * V)";
    parameter Real UA = 200 "Coeficiente de perda térmica do tanque";
    parameter Real UAt = 0.0 "Coeficiente de perda térmica da tubulação (ajustável)";
    
    // VARIÁVEIS DE ESTADO
    // T[1] é o tanque, T[2] em diante é a tubulação
    Real T[n+1](each start = 25) "Vetor de temperaturas (°C)";
    
    // ENTRADAS (Distúrbios e Controle)
    // No Modelica, se você quer que sejam fixos para teste, use 'parameter' 
    // ou atribua os valores na seção 'equation'.
    input Real z = 70 "Sinal de controle do aquecedor (0-100%)";
    input Real Fin = 10 "Vazão de entrada (m3/s)";
    input Real Tin = 25 "Temperatura do fluido na entrada (°C)";
    input Real Tinf = 25 "Temperatura ambiente (°C)";

  equation
    // 1. EQUAÇÃO DIFERENCIAL DO TANQUE (T[1])
    der(T[1]) = (Fin/V)*(Tin - T[1]) + (Qmax/V)*(z/100) - (UA/V)*(T[1] - Tinf);

    // 2. EQUAÇÕES DIFERENCIAIS DA TUBULAÇÃO (T[2] até T[n+1])
    // CORREÇÃO: Uso de ':' em vez de '..'
    for i in 2 : n+1 loop
      der(T[i]) = (n/Vt) * (Fin * (T[i-1] - T[i]) - UAt * (T[i] - Tinf));
    end for;

  end TanqueAquecimentoTubulacao;
end SistemaTermico;
