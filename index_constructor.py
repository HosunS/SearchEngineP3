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
       

    #There are also markup/txt files in the crawled pages, we parse through but will not grab any tag information from these.
    #parse given html/xml file and extract the text content
    def parse_and_extract_text(self, html_file_location):
        try:
            # print(html_file_location)
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
            # text_content = soup.get_text()
            
            # extract anchor text from links and include it as part of the text content
            for a_tag in soup.find_all('a'):
                anchor_text = a_tag.get_text(separator=' ', strip=True)
                text_content += f" {anchor_text}"

            # # creates the list of text with important tagsç
            text_with_tags = {}
            for tag_name in ["title", "strong", "h1", "h2", "h3"]:
                if tag_name  == 'title':
                    titleList = soup.find_all(tag_name)
                if tag_name == 'strong':
                    boldList = soup.find_all(tag_name)
                if tag_name == 'h1':
                    h1List = soup.find_all(tag_name)
                if tag_name == 'h2':
                    h2List= soup.find_all(tag_name)
                if tag_name == 'h3':
                    h3List = soup.find_all(tag_name)


            titleList = " ".join([element.get_text() for element in titleList])
            boldList = " ".join([element.get_text() for element in boldList])
            h1List = " ".join([element.get_text() for element in h1List])
            h2List = " ".join([element.get_text() for element in h2List])
            h3List = " ".join([element.get_text() for element in h3List])


            titleToken = tokenize(titleList)
            boldToken = tokenize(boldList)
            h1Token = tokenize(h1List)
            h2Token = tokenize(h2List)
            h3Token = tokenize(h3List)

            text_with_tags['title'] = lemmatize(titleToken)
            text_with_tags['bold']= lemmatize(boldToken)
            text_with_tags['h1'] = lemmatize(h1Token)
            text_with_tags['h2'] = lemmatize(h2Token)
            text_with_tags['h3'] = lemmatize(h3Token)



        except Exception as e:
            return "", {}
        
        return text_content, text_with_tags
    
    #used to compare current word to lists of words in specific tags and give a score
    def calculateTagImportance(self, token, lemTitle, lemBold,lemH1,lemH2,lemH3):
        score = 0.0
        if token in lemTitle:
            score += .9
        if token in lemH1:
            score += .7
        if token in lemH2:
            score += .5
        if token in lemH3:
            score += .4
        if token in lemBold:
            score += .3
        return score
    

    # calculates the TF
    def calculate_TF(self, FREQUENCY):
            if(FREQUENCY > 0):
                return 1 + math.log10(FREQUENCY)
            else:
                return 0

    def process_block(self,documents,block_id):
        block_index =  defaultdict(lambda: defaultdict(lambda:[0,0]))
        
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
                
                block_index[token][doc_id][self.HTML_TAG] = self.calculateTagImportance(token, tags_with_text['title'], tags_with_text['bold'], tags_with_text['h1'], tags_with_text['h2'], tags_with_text['h3'])
                # relevant_tags = [(tag[0], tag[1]) for tag in tags_with_text if token in tag[1]]
                # if relevant_tags:
                #     block_index[token][doc_id][self.HTML_TAG] = relevant_tags[0][0]

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
            # json.dump(final_index, file, indent=4)
            json.dump(final_index, file)
        
        file_size_bytes = os.path.getsize(final_index_file)
        file_size_kb = file_size_bytes / 1024
        print(f"Index file size: {file_size_kb:.2f} KB\n")     