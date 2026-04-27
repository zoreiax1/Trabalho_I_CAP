import os
import matplotlib.pyplot as plt

# 1. Configuração de Infraestrutura e Rotas (Específico para o seu ambiente)
caminho_custom = r'C:\Users\1304566\Bruno_Local\Program Files User\OpenModelica1.26.3-64bit'
os.environ['OPENMODELICAHOME'] = caminho_custom
os.environ['PATH'] = os.path.join(caminho_custom, 'bin') + os.pathsep + os.environ.get('PATH', '')

# 2. Importação da API após injeção das variáveis de ambiente
try:
    from OMPython import ModelicaSystem
except ImportError:
    print("ERRO Crítico: OMPython não instalado no ambiente ativo. Execute: pip install OMPython")
    exit()

def executar_simulacao():
    arquivo_mo = "SistemaTermico.mo"
    nome_modelo = "SistemaTermico.TanqueAquecimentoTubulacao"
    
    if not os.path.exists(arquivo_mo):
        print(f"ERRO: Arquivo '{arquivo_mo}' não encontrado no diretório atual: {os.getcwd()}")
        return

    print("Estabelecendo conexão via ZeroMQ com o OpenModelica Compiler...")
    try:
        # Compilação do modelo (gera AST e binários executáveis em background)
        modelo = ModelicaSystem(arquivo_mo, nome_modelo)

        # Adicione esta linha:
        print(f"DIRETÓRIO DE COMPILAÇÃO DO OMC: {modelo.getWorkDirectory()}")   
        
        # --- INÍCIO DA SEQUÊNCIA DE CONFIGURAÇÃO ESTRITA ---
        
        # PASSO A: Definir a janela temporal PRIMEIRO.
        # Isso garante que a matriz temporal gerada para os inputs tenha o comprimento correto.
        modelo.setSimulationOptions({
            "startTime": 0.0,
            "stopTime": 10.0,   # Reduzido de 500 para 2
            "stepSize": 0.01   # Força o solver a capturar mais pontos na subida
        })

        # PASSO B: Injetar os Inputs (Variáveis contínuas de entrada).
        # O OMC agora sabe que deve manter esses valores constantes do startTime até o stopTime.
        modelo.setInputs({
            "z": 70.0,
            "Fin": 5.0
        })
        
        # PASSO C: Definir Parâmetros Físicos/Estruturais (Constantes do modelo).
        modelo.setParameters({
            "V": 20.0
        })
        
        # --- FIM DA SEQUÊNCIA ---

        print("Iniciando integração numérica...")
        modelo.simulate() 
        print("Simulação concluída. Extraindo matrizes de dados...")
        
        # 3. Extração e Tratamento de Dados (.mat para NumPy arrays 1D)
        tempo = modelo.getSolutions("time").flatten()
        t_tanque = modelo.getSolutions("T[1]").flatten()
        t_saida = modelo.getSolutions("T[6]").flatten()
        
        # 4. Renderização do Gráfico
        plt.figure(figsize=(10, 5))
        plt.plot(tempo, t_tanque, label="Temperatura Tanque (T1)", linewidth=2, color="#1f77b4")
        plt.plot(tempo, t_saida, label="Temperatura Saída (T6)", linestyle='--', linewidth=2, color="#ff7f0e")
        
        plt.title("Dinâmica do Sistema Térmico (Tanque + Tubulação)", fontweight='bold')
        plt.xlabel("Tempo (s)")
        plt.ylabel("Temperatura (°C)")
        plt.legend(loc="lower right")
        plt.grid(True, linestyle=':', alpha=0.7)
        
        # Otimiza o layout para evitar cortes nas bordas
        plt.tight_layout()
        plt.show()
        
    except Exception as e:
        print(f"Falha na execução ou integração. Detalhes técnicos: {e}")

if __name__ == "__main__":
    executar_simulacao()