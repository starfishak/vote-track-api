from firebase_admin import firestore, App
import firebase_admin


class FirebaseDatastore:

    _connection: App

    def __init__(self):
        self._connection = firebase_admin.initialize_app()
        pass
