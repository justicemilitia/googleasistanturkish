# importing speech recognition package from google api 
import speech_recognition as sr 
import playsound # to play saved mp3 file 
from gtts import gTTS # google text to speech 
import os # to save/open files 
import wolframalpha # to calculate strings into formula 
import time
from selenium import webdriver # to control browser operations 

num = 1
def assistant_speaks(output): 
	global num 

	# num to rename every audio file 
	# with different name to remove ambiguity 
	num += 1
	print("Asistan : ", output) 

	toSpeak = gTTS(text = output, lang ='tr', slow = False) 
	# saving the audio file given by google text to speech 
	file = 'C:\\Projects\\asistant\\'+str(num)+".mp3"
	toSpeak.save(file) 
	
	# playsound package is used to play the same file. 
	playsound.playsound(file, True) 
	os.remove(file) 



def get_audio(): 

	rObject = sr.Recognizer() 
	audio = '' 

	with sr.Microphone() as source: 
		print("Konuşun...") 
		
		# recording the audio using speech recognition 
		audio = rObject.listen(source, phrase_time_limit = 5) 
	print("Durdu.") # limit 5 secs 

	try: 

		text = rObject.recognize_google(audio, language ='tr-TR') 
		print("You : ", text) 
		return text 

	except: 

		assistant_speaks("Anlaşılamadı lütfen tekrar edebilir misin? !") 
		return ''


# Driver Code 
if __name__ == "__main__": 
	assistant_speaks("Merhaba size hitap edebilmek için adınızı öğrenebilir miyim?") 
	# name ='Baran'
	name = get_audio() 
	assistant_speaks("Merhaba, " + name + '.') 
	
	while(1): 

		assistant_speaks("Senin için ne yapabilirim?") 
		text = get_audio().lower() 

		if text == '': 
			continue

		if "hiçbir şey" in str(text) or "güle güle" in str(text) or "çık" in str(text): 
			assistant_speaks("Tamamdır "+ name+' görüşmek üzere.') 
			break

		elif "google'da ara" in str(text) or "bir kelimeyi ara" in str(text) or "google'da bir kelime ara" in str(text):
			assistant_speaks('google da bir kelimenin aranmasını mı istiyorsunuz?')
			text=get_audio().lower()

			if "evet" in str(text):
				assistant_speaks('aratmak istediğiniz kelimeyi söyleyin.')
				text=get_audio().lower()
				driver = webdriver.Chrome()  # Optional argument, if not specified will search path.
				driver.get('http://www.google.com/')
				time.sleep(5) # Let the user actually see something!
				search_box = driver.find_element_by_name('q')
				search_box.send_keys(text)
				search_box.submit()
				time.sleep(5) # Let the user actually see something!
				driver.quit()
				assistant_speaks(text +" kelimesi goggle'da açıldı.") 
			else:
				continue
		else:
			assistant_speaks("Anlaşılamadı lütfen tekrar edebilir misin? !") 
			continue

