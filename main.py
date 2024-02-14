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


def enter_search_query(basic_query):
    search_query = input("Enter:") #gets search query from input ( not sure this is the right way to implemet this )
    docID_list = basic_query.search_query_term_from_index(search_query)
    link_list = basic_query.get_link_from_docID_list(docID_list)
    basic_query.print_out_query_links(search_query,link_list)




    return

if __name__ == "__main__":
    index = index_constructor()
    read_files(index)

    # query = basic_query()
    # enter_search_query(query)
