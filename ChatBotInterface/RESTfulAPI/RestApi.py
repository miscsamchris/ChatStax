from flask_restful import Resource
from ChatBotInterface.Models import ChatBot,Intent
class ChatBotIntentsRest(Resource):
    def get(self,id):
        chatbot=ChatBot.select_by_id(id)[0]
        if chatbot!= None:
            intents=Intent.select_by_chatbot_id(str(chatbot.id))
            return {"code":200,"Chatbot ID":chatbot.id,"Chatbot Name":chatbot.chatbot_name, "Chatbot version":chatbot.chatbot_version, "Chatbot Access Code":chatbot.chatbot_access_code,"Intents":[{"Intent ID":i.id,"Intent Name":i.intent_name,"Intent Response":i.intent_response}  for i in intents]}
        return {"code":404,"Message":"No Data Found"},404