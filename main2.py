import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate('nomeDaSuaChave.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

# db.collection("products").document("123").set({
#     "nome":"arroz",
#     "codigo":"12371892"
# });

# docs = db.collection("products").get()
# for doc in docs:
#     print("{} => {}".format(doc.id,doc.to_dict()))

dicionario = {}

print("digite o nome do produto")
dicionario["nome"] = input()

print("digite um codigo para o produto")
dicionario["codigo"] = input()

print("digite o preco do produto")
dicionario["preco"] = input()

db.collection("products").document().set(dicionario);