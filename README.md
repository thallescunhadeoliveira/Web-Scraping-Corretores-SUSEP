# 🏦 Web Scraping SUSEP - Corretores de Seguros

Este projeto tem como objetivo coletar e estruturar dados públicos de todos os corretores de seguros cadastrados na SUSEP (Superintendência de Seguros Privados), utilizando Python e técnicas de Web Scraping.

A ferramenta automatiza o processo de consulta ao portal oficial da SUSEP — disponível em https://www2.susep.gov.br/safe/Corretores/pesquisa
 — e extrai informações detalhadas sobre cada corretor, seja pessoa física (PF) ou pessoa jurídica (PJ).

Essa base de dados tem como objetivo facilitar o acesso e a consulta de grandes volumes de informações sobre corretores, além de permitir análises de mercado que apoiem a prospecção e a compreensão do setor de corretores de seguros.

---

## 🚀 Funcionalidades

- Coleta dados de **Corretores de Seguros** cadastradas na SUSEP
- Extrai informações como:
  - 📇 CNPJ / CPF
  - 🏢 Razão social / Nome Completo
  - 📜 Situação do Cadastro
  - 🔢 Número SUSEP do Corretor
  - 💼 Produtos Autorizados
  - 👤 Responsável Técnico
  - 🔢 Número SUSEP do Responsável Técnico

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

1. Clone o repositório:<br>
git clone https://github.com/thallescunhadeoliveira/Web-Scraping-SUSEP.git<br>
Ative o ambiente virtual<br>

2. Execute os scripts:<br>
- python extrair_corretores_susep.py<br>
- python extrair_responsavel_susep.py<br>

---

## 📁 Estrutura do Projeto<br>
Web-Scraping-SUSEP/<br>
│<br>
├─ code/                     # Scripts Python<br>
├─ data/                     # Arquivos CSV/Excel<br>
├─ venv/                     # Ambiente virtual<br>
├─ .env                      # Configurações de diretórios<br>
├─ requirements.txt          # Dependências do projeto<br>
└─ README.md                 # Documentação do projeto<br>

⚖️ Licença
Este projeto está sob a licença MIT.
Sinta-se à vontade para usar e contribuir! 👐

📌 Observações
Este projeto é apenas para uso educacional e pesquisa de dados públicos.

Sempre respeite os Termos de Uso da SUSEP.

---
## 👨‍💻 Desenvolvedor

**Thalles Oliveira**  [![GitHub](https://img.shields.io/badge/-000000?style=flat-square&logo=github)](https://github.com/thallescunhadeoliveira) [![LinkedIn](https://img.shields.io/badge/-in-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/thalles-cunha-de-oliveira/)
