# Trabalho I - Controle Avançado de Processos (2026/1)
## Engenharia de Controle e Automação - UFRGS

Este repositório contém o desenvolvimento do **Trabalho I** da disciplina de Controle Avançado de Processos. O objetivo principal é o projeto, sintonia e comparação de estratégias de controle (SISO vs. Cascata) para um sistema térmico com atraso de transporte: o **Chuveiro Turbinado**.

---

## 1. Descrição do Processo: Chuveiro Turbinado
O sistema é composto por três estágios dinâmicos:
1.  **Boiler (Aquecedor):** Sistema de aquecimento de água com dinâmica de primeira ordem.
2.  **Tanque de Mistura:** Onde ocorre o balanço de massa e energia, com volume variável e múltiplas entradas (vazão fria, quente e distúrbio).
3.  **Tubulação Longa:** Responsável por introduzir um **Atraso de Transporte (Tempo Morto)** significativo e perdas térmicas para o ambiente antes de atingir o ponto de consumo ($T_1$).

---

## 2. Roteiro de Execução (Ordem das Atividades)

Para a conclusão do trabalho, seguiremos rigorosamente a seguinte sequência técnica:

### Passo 1: Configuração do Ambiente 🟢 (Concluído)
- Instalação do VS Code e extensões (Python, Jupyter).
- Criação de ambiente virtual isolado (`.venv`).
- Instalação de bibliotecas matemáticas: `numpy`, `scipy`, `control`, `matplotlib` e `plotly`.

### Passo 2: Identificação do Sistema (Malha Aberta) 🟡 (Próxima Atividade)
- Execução de **Testes de Degrau** para levantar a curva de reação do processo.
- Obtenção dos parâmetros **FOPTD** (First-Order Plus Dead Time):
  - Ganho do Processo ($K_p$)
  - Constante de Tempo ($\tau$)
  - Tempo Morto ($\theta$)
- Identificação realizada para as duas variáveis controladas: $T_f$ (Saída do Tanque) e $T_1$ (Ponta da Tubulação).

### Passo 3: Projeto de Sintonia SISO ($T_f$)
- Projeto de controlador PID para a malha de temperatura do tanque.
- Foco: Rapidez de resposta e estabilidade em uma malha sem atraso dominante.

### Passo 4: Projeto de Sintonia SISO ($T_1$)
- Projeto de controlador PID para a malha final com atraso de transporte.
- Aplicação de métodos específicos para tempo morto (IMC, Skogestad ou Cohen-Coon).
- Análise da degradação de performance causada pelo atraso $\theta$.

### Passo 5: Projeto de Controle em Cascata
- Implementação da estrutura **Mestre-Escravo**:
  - **Mestre (Outer Loop):** Controla $T_1$ (temperatura de consumo).
  - **Escravo (Inner Loop):** Controla $T_f$ (temperatura do tanque).
- Objetivo: Corrigir distúrbios no tanque antes que eles se propaguem pela tubulação.

### Passo 6: Análise Comparativa e Relatório
- Simulações de rejeição de distúrbio (ex: variação na temperatura de entrada fria $T_f$).
- Comparação de métricas de desempenho (ISE, IAE, Sobressinal e Tempo de Acomodação).
- Exportação dos resultados para PDF via WebPDF.

### Passo 7: Validação em Modelica
- Transposição do modelo físico para o ambiente Modelica para validação final baseada em componentes.

---

## 3. Estrutura do Repositório
- `00_Introdução.ipynb`: Caderno inicial com as rotinas básicas de simulação do professor.
- `ChuveiroTurbinado_Final.ipynb`: Ambiente principal de desenvolvimento dos controladores e integrações de EDO.
- `.venv/`: Ambiente virtual de execução (não versionado).
- `Apostila_Parte_V.pdf`: Referência teórica sobre métodos de sintonia.

---

## 4. Como Executar
1. Certifique-se de ter o Python 3.10+ instalado.
2. Ative o ambiente virtual: `.\\.venv\\Scripts\\activate` (Windows).
3. Selecione o Kernel `.venv` no VS Code.
4. Execute as células sequencialmente.

---
**Desenvolvido por:** Bruno Richwicki
**Professor:** Jorge Otávio Trierweiler