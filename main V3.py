import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import openpyxl
import datetime

# ==========================
# CONFIGURAÇÃO DOS MERCADOS
# ==========================
mercados = {
    "Amigão": {
        "urls": [
    "https://www.amigao.com/s/?q=leite&sort=score_desc&page=0",
    "https://www.amigao.com/s/?q=ovos+de+galinha&sort=score_desc&page=0",
    "https://www.amigao.com/s/?q=p%C3%A3o+de+forma&sort=score_desc&page=0",
    "https://www.amigao.com/s/?q=Arroz+1kg&sort=score_desc&page=0",
    "https://www.amigao.com/s/?q=Arroz+5kg&sort=score_desc&page=0",
    "https://www.amigao.com/s/?q=feij%C3%A3o&sort=score_desc&page=0",
    "https://www.amigao.com/s/?q=macarr%C3%A3o+espaguete&sort=score_desc&page=0",
    "https://www.amigao.com/s/?q=carne+bovina&sort=score_desc&page=0",
    "https://www.amigao.com/s/?q=a%C3%A7ougue+para&category-3=aves&facets=category-3&sort=score_desc&page=0",
    "https://www.amigao.com/hortifruti/?category-1=alimentos&category-2=hortifruti&category-3=verduras&facets=category-1%2Ccategory-2%2Ccategory-3&sort=score_desc&page=0",
    "https://www.amigao.com/hortifruti/?category-1=alimentos&category-2=hortifruti&category-3=legumes-e-vegetais&facets=category-1%2Ccategory-2%2Ccategory-3&sort=score_desc&page=0",
    "https://www.amigao.com/hortifruti/?category-1=alimentos&category-2=hortifruti&category-3=frutas&facets=category-1%2Ccategory-2%2Ccategory-3&sort=score_desc&page=0",
    "https://www.amigao.com/s/?q=queijo&sort=score_desc&page=0",
    "https://www.amigao.com/s/?q=iogurte&sort=score_desc&page=0",
    "https://www.amigao.com/s/?q=a%C3%A7ucar+1kg&sort=score_desc&page=0",
    "https://www.amigao.com/s/?q=a%C3%A7ucar+5kg&sort=score_desc&page=0",
    "https://www.amigao.com/s/?q=sal+1kg&sort=score_desc&page=0",
    "https://www.amigao.com/s/?q=%C3%B3leo+de+soja&sort=score_desc&page=0",
    "https://www.amigao.com/s/?q=caf%C3%A9+500g&sort=score_desc&page=0",
    "https://www.amigao.com/s/?q=cerveja+lata+350ml&sort=score_desc&page=0",
    "https://www.amigao.com/s/?q=sorvete&sort=score_desc&page=0",
    "https://www.amigao.com/s/?q=%C3%A1gua+mineral+com+g%C3%A1s&sort=score_desc&page=0",
    "https://www.amigao.com/s/?q=refrigerante+2+litros&sort=score_desc&page=0",
    "https://www.amigao.com/s/?q=salada+org%C3%A2nica&sort=score_desc&page=0",
    "https://www.amigao.com/s/?q=vinho+tinto&sort=score_desc&page=0",
    "https://www.amigao.com/s/?q=chocolate+barra&sort=score_desc&page=0",
    "http://amigao.com/s/?q=sopa&sort=score_desc&page=0",
    "https://www.amigao.com/s/?q=ch%C3%A1&sort=score_desc&page=0"
            # ... adicione mais links do Amigão
        ],
        "nome_selector": "p.product-card-name",
        "preco_selector": "p.product-card-new-price",
        "preco_attr": "text",   # usa texto normal
    },
    "São_Judas_Tadeu": {
        "urls": [
            "https://compreonline.supersaojudas.com.br/loja6/busca/?q=Leite",
            "https://compreonline.supersaojudas.com.br/loja6/busca/?q=Ovos",
            "https://compreonline.supersaojudas.com.br/loja6/busca/?q=p%C3%A3o+forma",
            "https://compreonline.supersaojudas.com.br/loja6/busca/?q=arroz+1kg",
            "https://compreonline.supersaojudas.com.br/loja6/busca/?q=arroz+5kg",
            "https://compreonline.supersaojudas.com.br/loja6/busca/?q=feij%C3%A3o",
            "https://compreonline.supersaojudas.com.br/loja6/busca/?q=macarr%C3%A3o",
            "https://compreonline.supersaojudas.com.br/loja6/busca/?q=carne",
            "https://compreonline.supersaojudas.com.br/loja6/busca/?q=frango",
            "https://compreonline.supersaojudas.com.br/loja6/verduras-40/",
            "https://compreonline.supersaojudas.com.br/loja6/legumes-62/",
            "https://compreonline.supersaojudas.com.br/loja6/frutas-18/",
            "https://compreonline.supersaojudas.com.br/loja6/busca/?q=queijo",
            "https://compreonline.supersaojudas.com.br/loja6/busca/?q=iogurte",
            "https://compreonline.supersaojudas.com.br/loja6/busca/?q=a%C3%A7ucar+1kg",
            "https://compreonline.supersaojudas.com.br/loja6/busca/?q=a%C3%A7ucar+5kg",
            "https://compreonline.supersaojudas.com.br/loja6/busca/?q=sal+1kg",
            "https://compreonline.supersaojudas.com.br/loja6/busca/?q=%C3%B3leo+soja",
            "https://compreonline.supersaojudas.com.br/loja6/busca/?q=caf%C3%A9+500g",
            "https://compreonline.supersaojudas.com.br/loja6/busca/?q=cerveja",
            "https://compreonline.supersaojudas.com.br/loja6/busca/?q=Sorvete",
            "https://compreonline.supersaojudas.com.br/loja6/busca/?q=agua+mineral+c+gas",
            "https://compreonline.supersaojudas.com.br/loja6/busca/?q=refrigerante+2l",
            "https://compreonline.supersaojudas.com.br/loja6/busca/?q=vinho+tinto",
            "https://compreonline.supersaojudas.com.br/loja6/busca/?q=chocolate+80g",
            "https://compreonline.supersaojudas.com.br/loja6/busca/?q=sopa",
            "https://compreonline.supersaojudas.com.br/loja6/busca/?q=ch%C3%A1"
            # ... adicione links do outro mercado
        ],
        "nome_selector": "span.nome.ellipsis-2",
        "preco_selector": "input.valor-produto-peso",
        "preco_attr": "value",  # pega do atributo "value"
    },
     "Pão_de_açúcar": {
        "urls": [
            "https://www.paodeacucar.com/busca?terms=leite%201l",
            "https://www.paodeacucar.com/busca?terms=ovos",
            "https://www.paodeacucar.com/busca?terms=P%C3%A3o%20de%20forma",
            "https://www.paodeacucar.com/busca?terms=arroz%201kg",
            "https://www.paodeacucar.com/busca?terms=arroz%205kg",
            "https://www.paodeacucar.com/busca?terms=feij%C3%A3o",
            "https://www.paodeacucar.com/busca?terms=macarr%C3%A3o&p=2",
            "https://www.paodeacucar.com/categoria/alimentos/acougue/carnes/carne-bovina?s=relevance&p=1",
            "https://www.paodeacucar.com/categoria/alimentos/acougue/carnes/carne-aves?s=relevance&p=2",
            "https://www.paodeacucar.com/categoria/alimentos/hortifruti/legumes-e-verduras/hortalicas?s=relevance&p=3",
            "https://www.paodeacucar.com/categoria/alimentos/hortifruti/legumes-e-verduras/legumes?s=relevance&p=1",
            "https://www.paodeacucar.com/categoria/alimentos/hortifruti/frutas?s=relevance&p=1",
            "https://www.paodeacucar.com/busca?terms=queijo&p=3",
            "https://www.paodeacucar.com/busca?terms=Iogurte",
            "https://www.paodeacucar.com/busca?terms=a%C3%A7ucar%201kg",
            "https://www.paodeacucar.com/busca?terms=a%C3%A7ucar%205kg",
            "https://www.paodeacucar.com/busca?terms=sal",
            "https://www.paodeacucar.com/busca?terms=%C3%93leo%20de%20soja",
            "https://www.paodeacucar.com/busca?terms=Caf%C3%A9%20500g",
            "https://www.paodeacucar.com/busca?terms=Cerveja%20Lata%20350ml",
            "https://www.paodeacucar.com/busca?terms=sorvete&p=3",
            "https://www.paodeacucar.com/busca?terms=%C3%81gua%20mineral%20com%20g%C3%A1s",
            "https://www.paodeacucar.com/categoria/bebidas/nao-alcoolicas/refrigerantes?s=relevance&p=3",
            "https://www.paodeacucar.com/busca?terms=Salada%20&p=2",
            "https://www.paodeacucar.com/especial/tinto-app?p=4",
            "https://www.paodeacucar.com/busca?terms=Chocolate%20&p=3",
            "https://www.paodeacucar.com/busca?terms=sopa",
            "https://www.paodeacucar.com/busca?terms=ch%C3%A1"
        ],
        "nome_selector": "a[aria-label]",
        "nome_attr": "text",
        "preco_selector": "p[class^='PriceValue']",
        "preco_attr": "text"
,
    },
}

# ==========================
# INICIAR DRIVER
# ==========================
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # roda sem abrir janela
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# ==========================
# LOOP EM TODOS OS MERCADOS
# ==========================
for mercado, config in mercados.items():
    produtos = []

    for url in config["urls"]:
        print(f"🔎 Coletando {mercado} -> {url}")
        driver.get(url)
        time.sleep(3)

        # Rolagem até o final para carregar tudo
        ultima_altura = driver.execute_script("return document.body.scrollHeight")
        while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
            nova_altura = driver.execute_script("return document.body.scrollHeight")
            if nova_altura == ultima_altura:
                break
            ultima_altura = nova_altura

        print(f"✅ Todos os produtos carregados ({mercado}).")

        # Coleta os elementos
        nomes = driver.find_elements(By.CSS_SELECTOR, config["nome_selector"])
        precos = driver.find_elements(By.CSS_SELECTOR, config["preco_selector"])

        for nome, preco in zip(nomes, precos):
            preco_valor = (
                preco.text.strip()
                if config["preco_attr"] == "text"
                else preco.get_attribute(config["preco_attr"]).strip()
            )
            produtos.append({
                "Produto": nome.text.strip(),
                "Preço": preco_valor,
                "Categoria": url
            })

    # Salvar no Excel (aba por mercado)
    df = pd.DataFrame(produtos)
    df['Data da Coleta'] = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    arquivo = "mercados.xlsx"
    try:
        df_existente = pd.read_excel(arquivo, sheet_name=mercado)
        df_final = pd.concat([df_existente, df], ignore_index=True)
    except Exception:
        df_final = df

    with pd.ExcelWriter(arquivo, engine="openpyxl", mode="a", if_sheet_exists="replace") as writer:
        df_final.to_excel(writer, sheet_name=mercado, index=False)

    print(f"💾 {len(df_final)} produtos salvos na aba '{mercado}'.")

driver.quit()
print("🎉 Coleta finalizada para todos os mercados!")
