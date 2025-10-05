# 🏦 Web Scraping SUSEP - Corretores de Seguros

Este projeto mostra como **coletar dados públicos de corretores cadastrados na SUSEP** usando Python e Web Scraping. É útil para análises de mercado, inteligência comercial e estudos de dados de seguros.  

---

## 🚀 Funcionalidades

- Coleta dados de **pessoas jurídicas (PJ)** cadastradas na SUSEP
- Extrai informações como:
  - 📇 CNPJ
  - 🏢 Razão social
  - 📜 Situação do cadastro
  - 🔢 Número SUSEP do corretor
  - 💼 Produtos autorizados
- Consulta dados do **responsável técnico**, incluindo nome e número SUSEP
- Salva os dados incrementalmente em:
  - 📄 CSV/Excel

---

## 🛠 Tecnologias

- Python 3.x
- Bibliotecas:
  - `requests`  
  - `pandas`  
  - `openpyxl`  
- Ambiente virtual com `.env` para configuração de diretórios

---

## ⚡ Como usar

1. Clone o repositório:
git clone https://github.com/seu-usuario/Web-Scraping-SUSEP.git
Ative o ambiente virtual
Execute o script:
python extrair_corretores_susep.py

📁 Estrutura do Projeto
Web-Scraping-SUSEP/
│
├─ code/                     # Scripts Python
├─ data/                     # Arquivos CSV/Excel
├─ venv/                     # Ambiente virtual
├─ .env                      # Configurações de diretórios
├─ requirements.txt          # Dependências do projeto
└─ README.md                 # Documentação do projeto

⚖️ Licença
Este projeto está sob a licença MIT.
Sinta-se à vontade para usar e contribuir! 👐

📌 Observações
Este projeto é apenas para uso educacional e pesquisa de dados públicos.

Sempre respeite os Termos de Uso da SUSEP.

---
## 👨‍💻 Desenvolvedor

**Thalles Oliveira**  [![GitHub](https://img.shields.io/badge/-000000?style=flat-square&logo=github)](https://github.com/thallescunhadeoliveira) [![LinkedIn](https://img.shields.io/badge/-in-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/thalles-cunha-de-oliveira/)
