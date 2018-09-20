import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate('aula1-c93f4-firebase-adminsdk-ib3cp-82af23ef77.json')
firebase_admin.initialize_app(cred)
db = firestore.client()