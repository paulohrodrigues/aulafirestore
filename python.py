# import firebase_admin
# from firebase_admin import credentials
# from firebase_admin import firestore

# cred = credentials.Certificate('aula1-c93f4-firebase-adminsdk-ib3cp-82af23ef77.json')
# firebase_admin.initialize_app(cred)
# db = firestore.client()

# doc_ref = db.collection(u'usuarios').document()
# doc_ref.set({
#     u'nome': u'Paulo',
#     u'idade': 15
# })

# users_ref = db.collection(u'usuarios').where("nome","==","paulo")
# docs = users_ref.get()

# for doc in docs:
#     print(doc.to_dict()["nome"])


# Unicode é um padrão que permite aos computadores representar e manipular, de forma consistente, texto de qualquer sistema de escrita existente.