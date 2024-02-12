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
import json
from collections import defaultdict
# run these downloads below to be able to use nltk for tokenize/lemmatize
# nltk.download('punkt')
# nltk.download('wordnet')
# nltk.download('stopwords')


class index_constructor():
    index_dict = {}
    FREQUENCY = 0
    HTML_TAG = 1

        
    def __init__(self):
        self.webpages_path = "WEBPAGES_RAW"
        self.block_size = 500
        self.blocks_dir = "blocks"
        if not os.path.exists(self.blocks_dir):
            os.makedirs(self.blocks_dir)
       
    #tokenize text content
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
    
    def process_block(self,documents,block_id):
        block_index = {}
        for doc_id, text in documents:
            tokens = self.tokenize(text)
            lemmatized_tokens = self.lemmatize(tokens)
            #helps avoid duplicates by using a set
            for token in lemmatized_tokens:
                if token in block_index:
                    if doc_id in block_index[token]:
                        block_index[token][doc_id][self.FREQUENCY] += 1
                    else:
                        block_index[token][doc_id] = [1,""]
                else:
                    block_index[token] = {doc_id:[1,""]}
        self.save_block(block_index, block_id)
    
    # saves processed block to its own id
    def save_block(self, block_index, block_id):
        block_file = os.path.join(self.blocks_dir, f"block_{block_id}.json")
        with open(block_file, "w", encoding="utf-8") as file:
            json.dump(block_index, file, indent=4)        
                    
    ## merge blocks at the end into a final          
    def merge_blocks(self, final_index_file="final_index.json"):
        block_files = [os.path.join(self.blocks_dir, f) for f in os.listdir(self.blocks_dir) if f.endswith(".json")]
        final_index = {}
        for block_file in block_files:
            with open(block_file, "r", encoding="utf-8") as file:
                block_index = json.load(file)
            for token, doc_ids in block_index.items():
                if token not in final_index:
                    final_index[token] = doc_ids
                else:
                    final_index[token].extend(doc_ids)
                    final_index[token] = list(set(final_index[token]))  # Remove duplicates
        with open(final_index_file, "w", encoding="utf-8") as file:
            json.dump(final_index, file, indent=4)               
                    
    #creates index with lemmatized_tokens and file_location(Doc ID)
    # def indexing(self,key_list, document_ID):
        # for key in key_list:
        #     if key not in self.index_dict:
        #         self.index_dict[key] = []
        #         self.index_dict[key].append([document_ID,1])
                
        #     else:
        #         doc_id_in_list = False
        #         #check if doc id is already in list
        #         for doc in self.index_dict[key]:
        #             if doc[0] == document_ID:
        #                 doc[1] += 1
        #                 doc_id_in_list = True
        #                 break
        #         if (doc_id_in_list == False):
        #             self.index_dict[key].append([document_ID,1])
    
        
    # def create_index_file(self,file_name = "indexing_report.json"):
    #     # report = self.index_dict
    #     # with open(file_name, "w", encoding='utf-8') as file:
    #     #     for key, value in report.items():
    #     #         file.write(f"{key}: {value}\n\n")
    #     #     file.write("\n")
    #     try:
    #         with open(file_name, "r", encoding='utf-8') as file:
    #             existing_index = json.load(file)
    #     except FileNotFoundError:
    #         existing_index = {}
            
    #     #update index with new data
    #     existing_index.update(self.index_dict)
    #     with open(file_name, "w", encoding='utf-8') as file:
    #         json.dump(existing_index, file, ensure_ascii=False, indent=4)


