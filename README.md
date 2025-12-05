# Análise de Preços de Supermercados (ETL & Analytics)

Este projeto consiste em um pipeline de dados completo (ETL) e análise exploratória para monitorar, comparar e visualizar preços de produtos em diferentes supermercados (Amigão, São Judas Tadeu, Pão de Açúcar).

O objetivo é transformar dados brutos de coleta (web scraping ou arquivos Excel) em insights acionáveis, permitindo identificar a variação histórica de preços e simular a "Cesta de Compras Ideal" (Melhor Compra).

## Funcionalidades
* **ETL (Extração, Transformação e Carga):**
    * Limpeza robusta de dados brutos (remoção de URLs em nomes de categorias, padronização de acentos e textos).
    * Tratamento de dados monetários e conversão de datas.
    * Normalização de categorias de produtos (ex: agrupar "leite uht" e "leite 1l" na categoria "leite").
    * Exportação dos dados limpos para formato **Parquet** (alta performance).
* **Análise de Dados com DuckDB:**
    * Utilização de SQL via DuckDB para agregações rápidas em memória.
    * Cálculo de preço médio por categoria e por supermercado.
* **Visualização de Dados:**
    * Comparativo de custo total da cesta entre mercados.
    * Simulação da economia máxima possível comprando sempre o item mais barato ("MelhorCompra").

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3.12+
* **Manipulação de Dados:** Pandas, NumPy
* **Banco de Dados OLAP:** DuckDB
* **Visualização:** Matplotlib, Seaborn
* **Armazenamento:** Parquet (via PyArrow)
* **Processamento de Texto:** Regex, Unicodedata
