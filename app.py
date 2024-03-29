import requests
from bs4 import BeautifulSoup

class WebBot:
    def __init__(self):
        self.qa_dict = self.load_qa_from_file("cevaplar.txt")
    
    def load_qa_from_file(self, filename):
        qa_dict = {}
        with open(filename, "r", encoding="utf-8") as file:
            lines = file.readlines()
            for line in lines:
                parts = line.strip().split(":")
                question = parts[0].strip()
                answer = ":".join(parts[1:]).strip()
                qa_dict[question] = answer
        return qa_dict
    
    def get_wikipedia_summary(self, query):
        url = "https://tr.wikipedia.org/wiki/" + query.replace(" ", "_")
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        summary = soup.find("p")
        if summary:
            return summary.text
        else:
            return "Vikipedi'de bu isimde bir madde bulunmamaktadır."
    
    def google_search_summary(self, query):
        url = "https://www.google.com/search?q=" + query.replace(" ", "+")
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        summary = soup.find("div", class_="BNeawe").text
        return summary
    
    def respond_to_message(self, message):
        words = message.split()
        if len(words) > 1:
            return self.google_search_summary(message)
        elif message in self.qa_dict:
            return self.qa_dict[message]
        else:
            return self.get_wikipedia_summary(message)

web_bot = WebBot()

while True:
    user_input = input("Sen : ")
    response = web_bot.respond_to_message(user_input)
    print(response)




















































































































































































































































































































































































































































































