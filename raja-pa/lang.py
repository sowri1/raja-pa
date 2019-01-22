import speech
from chatterbot import ChatBot
import detector
chatbot = ChatBot(
 'RAJA',
 trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
)
#chatbot.train("chatterbot.corpus.english.conversations")
def reply(text):
	rp=chatbot.get_response(text)
	print(rp)
	speech.say(rp)