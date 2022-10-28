import requests
from bs4 import BeautifulSoup

# ---------------------------------------------------------------- Magalu
url_magalu = "https://www.magazinevoce.com.br/magazinenatalchegando/celulares-e-smartphones/l/28/"

magalu = requests.get(url_magalu)

html_magalu = BeautifulSoup(magalu.content, "html.parser")

produtos = html_magalu.find_all("div", attrs={"class": "g-desc"})

magalu = []

for div in produtos:
    fone = div.find_all("h3")
    valor = div.find_all("strong")
    magalu.append({"celular": fone[0].text.strip(), "preco": valor[0].text.strip()})

# ------------------------------------------------------------- Mercado Livre
url_ml = "https://celulares.mercadolivre.com.br/#menu=categories"

ml = requests.get(url_ml)

html_ml = BeautifulSoup(ml.content, "html.parser")

produtos = html_ml.find_all("div", attrs={"class": "andes-card andes-card--flat andes-card--default ui-search-result ui-search-result--core andes-card--padding-default"})

ml = []
# print(produto)
for produto in produtos:
    titulo = produto.find("h2", attrs={"class": "ui-search-item__title"})

    # print(titulo.text)

    real = produto.find("span", attrs={"class": "price-tag-fraction"})
    centavos = produto.find("span", attrs={"class": "price-tag-cents"})

    # print(real.text + ',' + centavos.text)

    if (centavos):
        ml.append({"celular": titulo.text.strip(), "preco": real.text.strip() + ',' + centavos.text.strip()})
    else:
        ml.append({"celular": titulo.text.strip(), "preco": real.text.strip()})


    # print(ml)

# ---------------------------------------------------------------- Programa Principal

def cab(texto, sublinhado="-"):
    print()
    print(texto)
    print(sublinhado*100)

    
def produtos_magalu():
    cab("Lista de Smartphones", "=")

    print("\nSmartphones.......................................................................................................: Preço.....:")
    print("-------------------------------------------------------------------------------------------------------------------------------")

    for smart in magalu:
        print(
            f"{smart['celular']:115s} {smart['preco']}")


def produtos_ml():
    cab("Lista de Smartphones", "=")

    print("\nSmartphones...............................................................: Preço.....:")
    print("---------------------------------------------------------------------------------------")


    for smart in ml:
        print(
            f"{smart['celular']:75s} R$ {smart['preco']}")


def todos_telefones():
   # declara um conjunto (não aceita duplicações)
    todos = set()     

    for smart in magalu:
        todos.add(smart['celular'])

    for smart in ml:
        todos.add(smart['celular'])

    # print(todos)
    
    # converte set (que não mantém ordem) em lista (que mantém)
    lista = list(todos)

    # classifica em ordem a lista
    lista2 = sorted(lista)

    cab("Todos os Smartphones")

    for smart in lista2:
        print(smart)


def apenas_magalu():
    # declara dos conjuntos (para obter diferença)
    set_magalu = set()     
    set_ml = set()

    for smart in magalu:
        set_magalu.add(smart['celular'])

    for smart in ml:
        set_ml.add(smart['celular'])

    smarts_em_magalu = set_magalu.difference(set_ml)

    cab("Smartphones: Apenas na Magazine Luiza")

    if len(smarts_em_magalu) == 0:
        print("Obs.: * Não há smartphones na magalu")
    else:
        for smart in smarts_em_magalu:
            print(smart)


def apenas_ml():
    # declara dos conjuntos (para obter diferença)
    set_magalu = set()     
    set_ml = set()

    for smart in magalu:
        set_magalu.add(smart['celular'])

    for smart in ml:
        set_ml.add(smart['celular'])

    smarts_em_ml = set_ml.difference(set_magalu)

    cab("Smartphones: Apenas no Mercado Livre")

    if len(smarts_em_ml) == 0:
        print("Obs.: * Não há smartphones no ML")
    else:
        for smart in smarts_em_ml:
            print(smart)

def lista_comuns():
    # declara dos conjuntos (para obter diferença)
    set_magalu = set()     
    set_ml = set()

    for smart in magalu:
        set_magalu.add(smart['celular'])

    for smart in ml:
        set_ml.add(smart['celular'])

    smarts_comuns = set_magalu.intersection(set_ml)

    cab("Smartphones em Ambos os Sites")

    if len(smarts_comuns) == 0:
        print("Obs.: * Não há smartphones Comuns em ambos os sites")
    else:
        for smart in smarts_comuns:
            print(smart)


def pesq_fone():
    cab("Pesquisa Por Smartphone")

    pesq = input("Nome do Smartphone: ")

    print("\nSmartphones.......................................................................................................: Preço.....:")
    print("-------------------------------------------------------------------------------------------------------------------------------")
    existe = False

    for smart in ml:
        if pesq.upper() in smart["celular"].upper():
            print(f"{smart['celular']:115s} R$ {smart['preco']}")
            existe = True

    for smart in magalu:
        if pesq.upper() in smart["celular"].upper():
            print(f"{smart['celular']:115s} {smart['preco']}")
            existe = True

    if not existe:
        print(f"\nObs.: * Não há celular com o nome '{pesq}'.")


def estatistica():
    cab("Estatística Smartphones")

    num = len(magalu)
    num2 = len(ml)
    total = num + num2


    print(f"Nº de Smartphones Magalu........: {num} un.")
    print(f"Nº de Smartphones Mercado Livre.: {num2} un.")
    print(f"Nº Total de Smartphones.........: {total} un.")

    


while True:
    cab("Smartphones na Magalu e Mercado Livre", "=")
    print("1. Smartphones Magazine Luiza")
    print("2. Smartphones Mercado Livre")
    print("3. Pesquisa por Celulares")
    print("4. Só Magalu tem")
    print("5. Só Mercado Livre tem")
    print("6. Todos Smartphones dos 2 Sites (ORDENADA)")
    print("7. Comuns nos 2 Sites")
    print("8. Estatística")
    print("9. Finalizar")
    opcao = int(input("Opção: "))
    if opcao == 1:
        produtos_magalu()
    elif opcao == 2:
        produtos_ml()
    elif opcao == 3:
        pesq_fone()
    elif opcao == 4:
        apenas_magalu()
    elif opcao == 5:
        apenas_ml()
    elif opcao == 6:
        todos_telefones()
    elif opcao == 7:
        lista_comuns()
    elif opcao == 8:
        estatistica()
    else:
        break