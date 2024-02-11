#creating inverted index

#use lmxl to parse html and extract text + handle broken html
#use nltk for tokenization and lemmatization

# import json
from lxml import html
import os.path
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
# run these downloads below to be able to use nltk for tokenize/lemmatize
# nltk.download('punkt')
# nltk.download('wordnet')
# nltk.download('stopwords')


class index_constructor():
    webpages_path = "WEBPAGES_RAW"
    index_dict = {}
        
    def __init__(self):
        pass

    #tokenize text content
    #also remove stop words here??
    def tokenize(self, text):
        text = text.lower()
        tokens = word_tokenize(text)
        tokens = [word for word in tokens if word.isalpha() and word not in stopwords.words('english')]
        return tokens
        

    #apply lemmatization on input
    def lemmatize(self,tokens):
        lemmatizer = WordNetLemmatizer()
        lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]
        return lemmatized_tokens

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
    
    #creates index with lemmatized_tokens and file_location(Doc ID)
    def indexing(self,key_list, document_ID):
        for key in key_list:
            if key not in self.index_dict:
                self.index_dict[key] = []
                self.index_dict[key].append(document_ID)
                
            else:
                #check if doc id is already in list 
                if document_ID in self.index_dict[key]:
                    pass
                else:
                  self.index_dict[key].append(document_ID)
        
    def create_index_file(index_dictionary):
        return 




