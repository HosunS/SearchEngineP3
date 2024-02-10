#creating inverted index

#use lmxl to parse html and extract text + handle broken html
#use nltk for tokenization and lemmatization

import json
from lxml import html
import os.path

class index_constructor():
    webpages_path = "WEBPAGES_RAW"
    index_dict = {}

    def __init__(self):
        pass

    #tokenize text content
    #also remove stop words here??
    def tokenize(self):
        pass

    #apply lemmatization on input
    def lemmatize(self):
        pass

    #parse given html file and extract the text content
    def parse_and_extract_text(self, html_file_location):

        #skip non html file
        try:
            #get file
            f = open(html_file_location, "r")

            page = f.read()
            f.close()

            #parse html
            html_page = html.fromstring(page)
            
            text_content = html_page.text_content()
        except:
            return ""
        return text_content

    #maybe should be moved to main.py???
    #go through bookkeeping.json and extract text from each html file for now
    def read_files(self):
        f = open(os.path.join(self.webpages_path,"bookkeeping.json"))
        file_dict = json.load(f)
        f.close()
        for file_location in file_dict.keys():
            folder,file_name = file_location.split("/")
            html_text = self.parse_and_extract_text(os.path.join(self.webpages_path,folder,file_name))
            #do tokenization and lemmatization on text next

        


test = index_constructor()
test.read_files()






