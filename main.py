import os
import json
from index_constructor import index_constructor

def read_files(index):
    f = open(os.path.join(index.webpages_path, "bookkeeping.json"))
    file_dict = json.load(f)
    f.close()
    for file_location in file_dict.keys():
        folder, file_name = file_location.split("/")
        html_text = index.parse_and_extract_text(os.path.join(index.webpages_path, folder, file_name))
        # do tokenization and lemmatization on text next
        tokens = index.tokenize(html_text)
        lemmatized_tokens = index.lemmatize(tokens)
        index.indexing(lemmatized_tokens, file_location)
        #print(tokens)
        #print(lemmatized_tokens)
        #print(file_location)
        #print(index.index_dict)
        index.create_index_file()

if __name__ == "__main__":
    test = index_constructor()
    read_files(test)
