import os
import sys
from flask import Flask,render_template, redirect,url_for
from flask_restful import Api
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider


direc=os.path.abspath(os.path.dirname(__file__))
app=Flask(__name__)
app.config["CREDENTIALS"]="\\static\\creds.zip"
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
api=Api(app=app)

class Connection:
    def __init__(self):
        SECURE_CONNECT_BUNDLE = direc+app.config["CREDENTIALS"]
        client_id = "LspfEiFAJHUjewLodgXSntNB"
        client_secret = "bcPNtrbuSOgJTXkDAt9pWMyN_jBHIXf+cX6m,dCSq.SeWmYFXs1rd4oZTD58nsWramYd6bci4nvmI1XA8OAx3ar_Uq,kU76p-LwfyYHfcQvKBqeulK8e+kuIf4DsCtWG"
        KEYSPACE = "chatbotengine"
        self.secure_connect_bundle=SECURE_CONNECT_BUNDLE
        self.path_to_creds=''
        self.cluster = Cluster(
            cloud={
                'secure_connect_bundle': self.secure_connect_bundle
            },
            auth_provider=PlainTextAuthProvider(client_id, client_secret)
        )
        self.session = self.cluster.connect(KEYSPACE)
    def close(self):
        self.cluster.shutdown()
        self.session.shutdown()
db=Connection()

from ChatBotInterface.RESTfulAPI.RestApi import ChatBotIntentsRest
api.add_resource(ChatBotIntentsRest,"/rest/chatbot/<int:id>/")