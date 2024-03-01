import os
import json
from index_constructor import index_constructor
from basic_query import basic_query
from math import log10

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
    print(f"# of documents: {len(index.unique_docids)}\n")
    print(f"Index file size: {len(index.unique_words)}\n")
    print(len(index.unique_docids))
    print(len(index.unique_words))


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

def calculate_idf():
    index_dict = {}
    file_path = "final_index.json"
    with open(file_path, "r", encoding="utf-8") as file:
       index_dict = json.load(file)
    file.close()
    for token in index_dict:
        for doc in index_dict[token]:
            index_dict[token][doc][0] = index_dict[token][doc][0]*log10(36614/len(index_dict[token]))
            

    with open(file_path, "w", encoding="utf-8") as file:
       index_dict = json.dump(index_dict, file, indent=4)
    file.close()



if __name__ == "__main__":

    #only create index if it doesn't exist in the directory
    if os.path.isfile("final_index.json") == False:
        index = index_constructor()
        read_files(index)
        calculate_idf()
    
    #uncomment if the index on your computer doesn't have idf calculated
    #calculate_idf
        
    enter_search_query()
        
