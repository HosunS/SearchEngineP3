#query the index and find results
import json
import os

class basic_query():


#returns list of doc id from final_index
  def search_query_term_from_index(self, search_query):
    docID_list = []
    temp_list = []
    file_path = "final_index.json"
    with open(file_path, "r", encoding="utf-8") as file:
       index_dict = json.load(file)
    
    for index in index_dict.keys():
      if index == search_query:
        temp_list = index_dict[index]
    
    for dict in temp_list:
      docID_list.append(dict)
    print("from search query function: ")
    print(len(docID_list))
    # print(docID_list)
    # print()
    # self.write_ouput_file(docID_list)
    return docID_list
      
  
#returns list of links from docID_list
  def get_link_from_docID_list(self, docID_list):
    link_list = []
    file_path = "WEBPAGES_RAW"
    with open(os.path.join(file_path, "bookkeeping.json")) as f:
        file_dict = json.load(f)
    
    for file_location in file_dict.keys():
      for doc_id in docID_list:
        if(file_location == doc_id):
          link_list.append(file_dict[doc_id])
    
    self.write_ouput_file(link_list)
    return link_list

#prints out related links for search query 
  def print_out_query_links(self, search_query, link_list):
    print(search_query)
    for link in link_list:
      print(link + "\n")
    
# write output into file (I just use it to see return value for each function)  
  def write_ouput_file(self,list):
    file_name = "search_query.txt"
    length = 0
    with open(file_name, "w", encoding='utf-8') as file:

      for dict in list:
          file.write(f"{dict}\n\n")
          length+=1
      file.write("\n")
    print("from ouput file funtion: ")
    print( length)

test = basic_query()
DocID = test.search_query_term_from_index("informatics")
links = test.get_link_from_docID_list(DocID)
# test.print_out_query_links("uci", links)
