import os
import json
from index_constructor import index_constructor
from basic_query import basic_query

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
    index.merge_blocks()
    print(len(index.unique_docids))


def enter_search_query():
    query = basic_query()
    while(True):
        query.get_query()
        docID_list = query.search_query_term_from_index()
        link_list = query.get_link_from_docID_list(docID_list)
        query.print_out_20_query_links(link_list)

        cont = input("Search again? y/n: ")
        while(cont.lower() != "y" and cont.lower() != "n"):
            cont = input("Invalid input. Search again? y/n: ")
        if cont.lower() == "n":
            break



if __name__ == "__main__":

    #only create index if it doesn't exist in the directory
    if os.path.isfile("final_index.json") == False:
        index = index_constructor()
        read_files(index)
        
    enter_search_query()
        
