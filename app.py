from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer

chatbot = ChatBot("MTBot")

trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english")

# trainer = ListTrainer("MTBot")
# trainer.train(['How are you?', 'I am good.', 'That is good to hear.', 'Thank you', 'You are welcome.'])

response = chatbot.get_response("Hello, how are you doing?")

from flask import Flask, render_template, request
app = Flask(__name__)
@app.route("/")
def home():
	return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(chatbot.get_response(userText))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)