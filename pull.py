from xml.dom.pulldom import *


# Abre um arquivo na pasta atual
doc = parse("ptwiki-20110617-pages-articles.xml")


# Percorre cada tupla (event, node) do doc, verificando se o evento atual
# é o evento de início de elemento DOM e se o nome do elemento é 'page'.
# Em caso positivo, expande o elemento e escreve seu conteúdo em um arquivo 
# na pasta atual cujo nome é um número e a extensão é .xml .

arquivo = 1

for event, node in doc:
    
    if (event == START_ELEMENT and node.localName == "page"):
        doc.expandNode(node)
        
        #print(str(dir(node)))
        open(str(arquivo) + ".xml", "w").write(node.toxml())
        arquivo += 1
    
