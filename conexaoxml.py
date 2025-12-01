import xml.etree.ElementTree as ET
import psycopg2
import os
path = "/home/usuarios/Documentos/neo4j_projeto/Fornecimento.xml"
print("Existe?", os.path.exists(path))
print("É arquivo?", os.path.isfile(path))


#acessa o arquivo xml e atribui a estrutura (arvore) a variável root
#faz conexão com postgresql
conn = psycopg2.connect(
    database="XMLBanco",
    host="localhost",
    user="postgres",
    password="unochapeco",
    port="5432")
sqlpeca = "select * from peca"
cursor = conn.cursor()
cursor.execute(sqlpeca)
rows = cursor.fetchall()

for row in rows:
    codigo = str(row[0])
    pnome = str(row[1])
    cor = str(row[2])
    peso = str(row[3])
    cidade = str(row[4])
    preco = str(row[5])
    print(codigo + " " + pnome + " " + cor + " " + peso + " " + cidade + " " + preco)

#imprimindo os valores do arquivo
tree = ET.parse("fornecimento.xml")
root = tree.getroot()
for f in root.findall("row"):
  cod = f.find("codigo").text.strip()
  codf = f.find("cod_fornec").text.strip()
  codp = f.find("cod_peca").text.strip()
  codj = f.find("cod_proj").text.strip()
  qtde = f.find("quantidade").text.strip()
  val = f.find("valor").text.strip()
  print(str(codf) + " " + str(codp) + " " + str(codj) + " " + str(qtde) + " " + str(val))