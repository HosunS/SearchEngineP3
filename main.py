import os
import json
from index_constructor import index_constructor

def read_files(index):
    
    with open(os.path.join(index.webpages_path, "bookkeeping.json")) as f:
        file_dict = json.load(f)

    documents = []
    block_id = 0
    for file_location in file_dict.keys():
        folder, file_name = file_location.split("/")
        html_file_path = os.path.join(index.webpages_path, folder, file_name)
        html_text,tags_with_text = index.parse_and_extract_text(html_file_path)

        #have text to process
        if html_text:
            documents.append((file_location, html_text, tags_with_text))

        # check if current block is full
        if len(documents) >= index.block_size:  
            index.process_block(documents, block_id)

            #reset documents for the next block
            documents = []  
            block_id += 1

    # process the last block if there are any documents left
    if documents:
        index.process_block(documents, block_id)

    # blocks are processed merge them into the final index
    #index.merge_blocks()
    

if __name__ == "__main__":
    test = index_constructor()
    read_files(test)
