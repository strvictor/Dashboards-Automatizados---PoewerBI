


# 📊 Integração de Logs do Active Directory com Power BI

Este projeto automatiza a extração de dados do **Active Directory**, gerando um arquivo **CSV** que serve como fonte de dados para o **Power BI**. Com essa solução, as informações estarão sempre atualizadas, permitindo análises em tempo real e uma visualização clara dos dados organizacionais.

---

## 🚀 Funcionalidades

✅ **Extração Automatizada:** Script em PowerShell para coletar os logs do Active Directory.  
✅ **Processamento de Dados:** Script Python para filtrar e formatar apenas os dados relevantes.  
✅ **Integração com Power BI:** O arquivo gerado é utilizado como fonte de dados em dashboards interativos.  

---

## 🔧 Pré-requisitos

- Acesso ao Active Directory.
- Sistema operacional Windows (acesso à unidade `C:`).
- PowerShell instalado.
- Python 3.10 instalado.
- Power BI Desktop para criar os dashboards.

---

## 📌 Instruções de Uso

### 1️⃣ Criar a Pasta de Logs

Crie uma pasta chamada `Logs` na raiz da unidade C:
```bash
C:\Logs
```

### 2️⃣ Extração do Log do Active Directory
- Execute o script script_log_impressao.ps1 no Active Directory.
- O script salvará automaticamente o arquivo de log na pasta `C:\Logs`.

### 3️⃣ Processamento dos Dados
- Após a geração do log, execute o script Python `executavel.py`:
```bash
python executavel.py
```
- O Python irá extrair apenas os dados relevantes e criar um novo arquivo formatado:
```bash
C:\Logs\LogsImpressoesFormatado.csv
```

### 4️⃣ Criar o Dashboard no Power BI
- Abra o Power BI Desktop.
- Importe o arquivo LogsImpressoesFormatado.csv como fonte de dados no modelo `Dashboard Impressoes.pbix`.
- Visualize e analise os dados em tempo real.

-> Exemplo:
¹
![image](https://github.com/user-attachments/assets/2bb95129-dd75-4f88-be39-0b35e11550c4)
²
![image](https://github.com/user-attachments/assets/03827121-1f65-40a6-aeb4-b66f8b220c3f)

### 📢 Considerações Finais
Esta solução foi desenvolvida para otimizar o monitoramento do consumo de impressões, facilitando a gestão de recursos de TI. Com dados sempre atualizados, é possível tomar decisões mais estratégicas e reduzir desperdícios.
