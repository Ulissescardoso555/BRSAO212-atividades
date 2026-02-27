import sys
import subprocess

# Tenta importar o pandas, instala se não encontrar
try:
    import pandas as pd
except ModuleNotFoundError:
    print("Biblioteca 'pandas' não encontrada. Instalando automaticamente...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pandas"])
    print("Instalação concluída!\n")
    import pandas as pd

print("--- Análise de Logs de Treinamento ---")
nome_arquivo = input("Digite o nome do arquivo CSV de logs (ex: logs.csv): ")

try:
    # O pandas lê o CSV e transforma em um DataFrame (tabela)
    df = pd.read_csv(nome_arquivo)
    
    # Verifica se a coluna existe antes de tentar calcular
    if 'tempo_execucao' not in df.columns:
        print("Erro: A coluna 'tempo_execucao' não foi encontrada no arquivo.")
    else:
        media = df['tempo_execucao'].mean()
        desvio_padrao = df['tempo_execucao'].std()
        
        print("\n--- Resultados Estatísticos ---")
        print(f"Média de Tempo: {media:.2f}")
        print(f"Desvio Padrão: {desvio_padrao:.2f}")

except FileNotFoundError:
    print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado no diretório atual.")
except pd.errors.EmptyDataError:
    print("Erro: O arquivo CSV está vazio.")
except Exception as erro:
    print(f"Erro inesperado ao ler o arquivo: {erro}")