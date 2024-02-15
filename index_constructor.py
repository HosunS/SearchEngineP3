#creating inverted index

#use lmxl to parse html and extract text + handle broken html
#use nltk for tokenization and lemmatization

# import json
from bs4 import BeautifulSoup
from lxml import html
import lxml
import os
import os.path
import json
from collections import defaultdict
from format_text import tokenize, lemmatize
import math
import warnings

#ignore bs4 warnings
warnings.filterwarnings("ignore", category=UserWarning, module='bs4')
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
        self.unique_docids = set()
        self.unique_words = set()
       
    # #tokenize text content
    # def tokenize(self, text):
    #     text = text.lower()
    #     tokens = word_tokenize(text)
    #     tokens = [word for word in tokens if word.isalpha() and word not in stopwords.words('english')]
    #     return tokens
        

    # #apply lemmatization on input
    # def lemmatize(self,tokens):
    #     lemmatizer = WordNetLemmatizer()
    #     lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]
    #     return lemmatized_tokens

    

    # #parse given html file and extract the text content
    # def parse_and_extract_text(self, html_file_location):
    #     #skip non html file
    #     try:
    #         #get file
    #         f = open(html_file_location, "r")

    #         page = f.read()
    #         f.close()

    #         #parse html
    #         html_page = html.fromstring(page)
            
    #         text_content = html_page.text_content()

    #         #creates the list of text with important tags 
    #         text_with_tags = []
    #         for element in html_page.iter():
    #             if element.tag in ["title", "strong","h1", "h2", "h3"]:
    #                 #needed to tokenize/lemmatize the tag_content we extracted first
    #                 tag_text = element.text_content().lower() 
    #                 tag_tokens = tokenize(tag_text)
    #                 tag_lemmas = lemmatize(tag_tokens)
    #                 text_with_tags.append((element.tag, " ".join(tag_lemmas)))
    #                 # print(element.text_content())

    #     except:
    #         return "", []
    #     return text_content,text_with_tags

    #There are also markup/txt files in the crawled pages, we parse through but will not grab any tag information from these.
    #parse given html/xml file and extract the text content
    def parse_and_extract_text(self, html_file_location):
        try:
             # determine the file type based on its extension
            _, file_extension = os.path.splitext(html_file_location)
            is_xml = file_extension.lower() in ['.xml']
            parser_type = "lxml-xml" if is_xml else "lxml"
            
            #open and read 
            with open(html_file_location, "r", encoding="utf-8") as f:
                page = f.read()

            #parse using lxml-xml for xml , or lxml for html
            soup = BeautifulSoup(page, parser_type)  

            # extract text content
            text_content = soup.get_text(separator=' ', strip=True)

            # creates the list of text with important tags
            text_with_tags = []
            for tag_name in ["title", "strong", "h1", "h2", "h3"]:
                for element in soup.find_all(tag_name):
                    tag_text = element.get_text().lower()
                    tag_tokens = tokenize(tag_text)
                    tag_lemmas = lemmatize(tag_tokens)
                    text_with_tags.append((tag_name, " ".join(tag_lemmas)))

        except Exception as e:
            return "", []
        
        return text_content, text_with_tags
    
    # calculates the TF
    def calculate_TF(self, FREQUENCY):
            if(FREQUENCY > 0):
                return 1 + math.log10(FREQUENCY)
            else:
                return 0

    def process_block(self,documents,block_id):
        block_index =  defaultdict(lambda: defaultdict(lambda:[0,""]))
        
        for doc_id, text, tags_with_text in documents:
            tokens = tokenize(text)
            lemmatized_tokens = lemmatize(tokens)
            
            # #count total words in doc
            # total_words = len(lemmatized_tokens)
            
            #counter for each document and also adds unique tokens for final analytic
            term_frequencies = defaultdict(int)
            for token in lemmatized_tokens:
                term_frequencies[token] += 1
                self.unique_words.add(token)
            
            #helps avoid duplicates by using a set
            for token , freq in term_frequencies.items():
                #calculate TF here
                tf = self.calculate_TF(freq)
                #if document is associated with the token
                if doc_id in block_index[token]:
                    block_index[token][doc_id][self.FREQUENCY] = tf
                else:
                    block_index[token][doc_id] = [tf,""]
                    self.unique_docids.add(doc_id)
                
                relevant_tags = [(tag[0], tag[1]) for tag in tags_with_text if token in tag[1]]
                if relevant_tags:
                    block_index[token][doc_id][self.HTML_TAG] = relevant_tags[0][0]

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
                    final_index[token].update(doc_ids)
                    #final_index[token] = list(set(final_index[token]))  # Remove duplicates
        with open(final_index_file, "w", encoding="utf-8") as file:
            json.dump(final_index, file, indent=4)
        
        file_size_bytes = os.path.getsize(final_index_file)
        file_size_kb = file_size_bytes / 1024
        print(f"Index file size: {file_size_kb:.2f} KB\n")     
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
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


