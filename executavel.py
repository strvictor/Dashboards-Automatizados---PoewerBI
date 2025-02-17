import subprocess
import time
import pandas as pd


def FormataDados(caminho_do_csv_antigo, saida_do_csv_novo):
    # Configurações de exibição
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)

    arquivo_csv = str(caminho_do_csv_antigo)
    arquivo_saida_csv = str(saida_do_csv_novo)

    data_frame = pd.read_csv(arquivo_csv)

    # Função para extrair informações de cada linha
    def extrair_info(linha):
        try:
            # Extrair a coluna de data e hora diretamente do DataFrame
            data_e_hora = linha['TimeCreated']
            status = linha['OpcodeDisplayName']
            
            # Ajustar a extração de informações da mensagem
            mensagem = linha['Message']
            partes = mensagem.split(' ')
            
            usuario = partes[6]
            maquina_usuario = partes[8]
            impressora = partes[12]
            
            # Logica pra capturar o nome completo da impressora
            if str(partes[13]) == '(L375)':
                impressora = impressora + ' (L375)'
                
            elif str(partes[13]) == 'FISCAL-RECEPCAO':
                impressora = impressora + ' FISCAL-RECEPCAO'
                
            elif str(partes[13]) == '(XPS-CARD)':
                impressora = impressora + ' (XPS-CARD)'
            
            else:
                pass
            
        except (IndexError, ValueError, KeyError):
            usuario, maquina_usuario, impressora, status, data_e_hora = 'N/A', 'N/A', 'N/A', 'N/A', 'N/A'
        return usuario, maquina_usuario, impressora, status, data_e_hora

    info = [extrair_info(linha) for _, linha in data_frame.iterrows()]

    # Criar novo DataFrame com as informações extraídas
    df_info = pd.DataFrame(info, columns=['Usuario', 'Maquina do Usuario', 'Impressora', 'Status', 'Data e Hora'])

    # Exibir resultado sem índices
    print(df_info.to_string(index=False))

    # Salvar DataFrame em um novo arquivo CSV
    df_info.to_csv(arquivo_saida_csv, index=False)
    

# Caminho para o script PowerShell no AD
script_path = 'C:\\Users\\Administrator\\Documents\\script_log_impresao.ps1'
c = 0
while True:
    c +=1
    # Comando para executar o script PowerShell
    ps_command = f'powershell.exe -ExecutionPolicy Bypass -File "{script_path}"'
    
    # Executa o comando PowerShell
    result = subprocess.run(ps_command, capture_output=True, text=True, shell=True)
    
    
    # Aguarda 10 minutos (600 segundos) antes de executar novamente
    print(f'Rodei {c} vezes')
    time.sleep(10)
    FormataDados('C:\Logs\LogsImpressoes.csv', 'C:\Logs\LogsImpressoesFormatado.csv')
    time.sleep(600)
