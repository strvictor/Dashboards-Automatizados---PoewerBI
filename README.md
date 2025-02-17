Integração de Logs do Active Directory com Power BI
Este projeto automatiza a extração de dados do Active Directory, gerando um arquivo CSV que serve como fonte de dados para o Power BI. Com essa solução, suas informações estarão sempre atualizadas, permitindo análises em tempo real e uma visualização clara dos dados organizacionais.

Funcionalidades
Extração Automatizada: Utiliza um script em PowerShell para coletar os logs do Active Directory.
Processamento de Dados: Um script Python processa o log, filtrando e formatando somente os dados relevantes.
Integração com Power BI: O arquivo CSV gerado é ideal para ser utilizado como fonte de dados em dashboards interativos no Power BI.
Pré-requisitos
Acesso ao Active Directory.
Sistema operacional Windows (acesso à unidade C:).
PowerShell instalado.
Python 3.x instalado.
Power BI Desktop para a criação dos dashboards.
Instruções de Uso
Criação da Pasta de Logs

Crie uma pasta chamada Logs na raiz da unidade C:

makefile
Copiar
Editar
C:\Logs
Extração do Log do Active Directory

Execute o script script_log_impressao.ps1 no Active Directory.
O script salvará automaticamente o arquivo de log na pasta C:\Logs.
Processamento dos Dados

Após a geração do log, execute o script executalve.py.
O Python irá extrair apenas os dados importantes do log e criar um novo arquivo:
makefile
Copiar
Editar
C:\Logs\LogsImpressoesFormatado.csv
Criação do Dashboard no Power BI

Abra o Power BI Desktop.
Importe o arquivo LogsImpressoesFormatado.csv como fonte de dados.
Crie dashboards interativos para visualizar e analisar os dados em tempo real.
Considerações Finais
Esta integração foi desenvolvida para facilitar o monitoramento do consumo de impressões e melhorar a gestão dos recursos de TI. Ao manter os dados sempre atualizados, a solução permite decisões mais ágeis e informadas. Se tiver dúvidas ou sugestões, sinta-se à vontade para entrar em contato!
