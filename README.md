# Supermarket-Data-Lake-

# 🛒 Coletor de Preços de Supermercados

Este projeto faz a coleta automatizada de preços de diferentes supermercados usando **Python + Selenium**, salvando os resultados em um arquivo Excel (`mercados.xlsx`).  

Foi desenvolvido de forma modular, permitindo adicionar novos mercados facilmente apenas configurando os seletores no dicionário `mercados`.

---

## 🚀 Tecnologias utilizadas
- [Python 3.x](https://www.python.org/)
- [Selenium](https://selenium-python.readthedocs.io/)
- [pandas](https://pandas.pydata.org/)
- [openpyxl](https://openpyxl.readthedocs.io/)
- [webdriver-manager](https://github.com/SergeyPirogov/webdriver_manager)

---

## 📦 Instalação

Clone o repositório:
```bash
git clone https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git
cd SEU_REPOSITORIO

## Crie um ambiente virtual (recomendado):
python -m venv venv

## Ative o ambiente virtual:

## Windows (PowerShell):

venv\Scripts\Activate


## Linux / Mac:

source venv/bin/activate


## Instale as dependências:

pip install -r requirements.txt

▶️ Uso

## Execute o script principal:

python main.py


## Ao final, será gerado o arquivo mercados.xlsx com os preços coletados (ou adicionado novos produtos).