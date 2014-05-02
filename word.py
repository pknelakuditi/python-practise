from wordnik import *
apiUrl = 'http://api.wordnik.com/v4'
apiKey = 'e1a170a59a2e51ca5aa370af2aa012a0237bf057ea00b4665'
client = swagger.ApiClient(apiKey, apiUrl)

def app():
 	 f=open('words.txt','r+')
	 words=[i for  i in f.read().split("\n")]
	 
 	 f.close()
	 return words
		

def main():
	words=app()
	print words
        wordApi = WordApi.WordApi(client)
        for i in range(len(words)):
		try:
		 example = wordApi.getTopExample(words[i])
		 print example.text
		except ValueError:
 			pass
	
	

if __name__ == '__main__':
  main()
