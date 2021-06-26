from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,validators

class AddChatBot(FlaskForm):
    chatbot_name=StringField("ChatBot Name",validators=[validators.required()])
    submit=SubmitField("Create Chatbot")
    
class AddIntent(FlaskForm):
    intent_name=StringField("Intent Name",validators=[validators.required()])
    intent_response=StringField("Intent Response",validators=[validators.required()])
    submit=SubmitField("Add Intent")
