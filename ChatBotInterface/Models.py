from ChatBotInterface import db

class ChatBot():
    __tablename__="chatbots"
    id=0
    chatbot_name=""
    chatbot_version=""
    chatbot_access_code=""
    chatbot_uid=""
    counter=1
    def __init__(self,id=0,chatbot_name="",chatbot_version="",chatbot_access_code="",chatbot_uid=""):
        self.id=id
        self.chatbot_name=chatbot_name
        self.chatbot_version=chatbot_version
        self.chatbot_access_code=chatbot_access_code
        self.chatbot_uid=chatbot_uid
    def selectall():
        try:
            chatbots=db.session.execute("select * from chatbots;")
            cbs=[]
            for i in chatbots:
                cbs.append(ChatBot(i.chatbot_id, i.chatbot_name, i.chatbot_version, i.chatbot_access_code, i.chatbot_uid))
            return cbs
        except Exception as e:
            print(e)
    def select_by_id(id):
        try:
            chatbots=db.session.execute("select * from chatbots where chatbot_id =%s ALLOW FILTERING;",[id])
            cbs=[]
            for i in chatbots:
                cbs.append(ChatBot(i.chatbot_id, i.chatbot_name, i.chatbot_version, i.chatbot_access_code, i.chatbot_uid))
            return cbs
        except Exception as e:
            print(e)
    def insert(self,chatbot_name,chatbot_version,chatbot_access_code,chatbot_uid):
        ChatBot.counter=len(ChatBot.selectall())
        self.id=ChatBot.counter+1
        self.chatbot_name=chatbot_name
        self.chatbot_version=chatbot_version
        self.chatbot_access_code=chatbot_access_code
        self.chatbot_uid=chatbot_uid
        try:
            db.session.execute("INSERT INTO chatbots ( chatbot_id, chatbot_name, chatbot_version, chatbot_access_code, chatbot_uid ) VALUES (%s,%s,%s,%s,%s);",
            [self.id, self.chatbot_name,self.chatbot_version,self.chatbot_access_code,self.chatbot_uid])
            pass
        except Exception as e:
            print(e)
    def __repr__(self):
        return f"{self.chatbot_name} : {self.chatbot_uid}"
class Intent():
    __tablename__="Intents"
    id=0
    intent_name=""
    intent_uid=""
    chatbot_id=""
    counter=1
    intent_response=""
    def __init__(self,id=0,intent_name="",intent_uid="",chatbot_id="",intent_response=""):
        self.id=id
        self.intent_name=intent_name
        self.intent_uid=intent_uid
        self.chatbot_id=chatbot_id
        self.intent_response=intent_response
    def selectall():
        try:
            intents=db.session.execute("select * from intents;")
            INTENTS=[]
            for i in intents:
                INTENTS.append(Intent(i.intent_id,i.intent_name,i.intent_uid,i.chatbot_id,i.intent_response))
            return INTENTS
        except Exception as e:
            print(e)
    def select_by_chatbot_id(id):
        try:
            intents=db.session.execute("select * from intents where chatbot_id =%s ALLOW FILTERING;",[id])
            INTENTS=[]
            for i in intents:
                INTENTS.append(Intent(i.intent_id,i.intent_name,i.intent_uid,i.chatbot_id,i.intent_response))
            return INTENTS
        except Exception as e:
            print(e)
    def insert(self,intent_name,intent_uid,chatbot_id,intent_response):
        Intent.counter=len(Intent.selectall())
        self.id=Intent.counter+1
        self.intent_name=intent_name
        self.intent_uid=intent_uid
        self.chatbot_id=chatbot_id
        self.intent_response=intent_response
        try:
            db.session.execute("INSERT INTO intents ( intent_id, intent_name, intent_uid, chatbot_id, intent_response ) VALUES (%s,%s,%s,%s,%s);",
            [self.id, self.intent_name,self.intent_uid,str(self.chatbot_id),self.intent_response])
            pass
        except Exception as e:
            print(e)
    def __repr__(self):
        return f"{self.intent_name} : {self.intent_uid}"