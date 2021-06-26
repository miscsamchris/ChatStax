from ChatBotInterface import db,app
import json
from ChatBotInterface.Models import ChatBot,Intent
import requests
from ChatBotInterface.forms import AddChatBot,AddIntent
from flask import render_template,redirect,url_for,request
@app.route("/")
def home():
    return redirect(url_for("addcb"))
@app.route("/addChatbot/", methods=["POST","GET"])
def addcb():
    form = AddChatBot()
    if form.is_submitted():
        chatbot_name=form.chatbot_name.data
        url = "https://api.wit.ai/apps?v=20210606"
        payload = '{"name": "'+chatbot_name+'", "lang": "en", "private": true,"timezone": "Europe/Brussels"}'
        headers = {
        'Authorization': 'Bearer OD7JXPJYFHFAK3QFVDJA3NH7ZDV4EEHB',
        'Content-Type': 'application/json'
        }
        response = requests.request("POST", url, headers=headers, data = payload)
        res=json.loads(response.text)
        chatbot_uid=res["app_id"]
        chatbot_access_code=res["access_token"]
        cb=ChatBot()
        cb.insert(chatbot_name,"20210606",chatbot_access_code,chatbot_uid)
        return redirect(url_for("addintent",cbid=cb.id))
    return render_template("addchatbot.html",form=form)
@app.route("/addIntent/<int:cbid>/", methods=["POST","GET"])
def addintent(cbid):
    form = AddIntent()
    if form.is_submitted():
        intent_name=form.intent_name.data.replace(" ","_")
        intent_response=form.intent_response.data
        chatbot=ChatBot.select_by_id(cbid)[0]
        access_code=chatbot.chatbot_access_code
        version=chatbot.chatbot_version
        url = "https://api.wit.ai/intents?v="+version
        payload = '{"name": "'+intent_name+'"}'
        headers = {
        'Authorization': 'Bearer '+access_code,
        'Content-Type': 'application/json'
        }
        response = requests.request("POST", url, headers=headers, data = payload)
        res=json.loads(response.text)
        intent_uid=res["id"]
        if request.method=="POST" and len(list(request.form.keys())) > 0:
            keys=list(request.form.keys())
            trainingdata=[request.form[x] for x in keys if "data_query" in x]
            if len(trainingdata)>0:
                url = "https://api.wit.ai/utterances?v="+version
                headers = {
                'Authorization': 'Bearer '+access_code,
                'Content-Type': 'application/json'
                }
                payload=[{"text": x,"intent": intent_name,"entities": [],"traits": []} for x in trainingdata]
                pl="["
                for i in payload:
                    pl+=str(i)+","
                pl+="]"
                response = requests.request("POST", url, headers=headers, data = pl)
                intent=Intent()
                intent.insert(intent_name,intent_uid,cbid,intent_response)
            return redirect(url_for("addintent",cbid=cbid))
    return render_template("addintent.html",form=form)
if __name__=="__main__":
    app.run(host="localhost",port="80")