import sys
import requests

def brute(url, wordlist):
  for word in wordlist:
    try:
      url_final = "{}/{}".format(url, word.strip())
      response = requests.get(url_final)
      code = response.status_code(0)
      if code == 404:
        print("{} -- {}".format(url_final, code))
      except keyboardInterrupt :
        sys.exit(0)
      except Excepition as error:
        print(error)
        pass
      
      if __name__ == "__main__":
        url = sys.argv[1]
        wordlist = sys.argv[2]
        
         with open(wordlist, "r") as file:
            wordlist = file.readlines()
            brute(url, wordlist)
