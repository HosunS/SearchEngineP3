#query the index and find results
import json
import os
from format_text import tokenize, lemmatize
from collections import defaultdict
from math import log10
import math


class basic_query():

  def __init__(self):
    #input given by user
    self.original_query = ""

    #tokenized input
    self.search_query = []

    #query_index
    self.query_tfidf_scores = []

    #index
    file_path = "final_index.json"
    with open(file_path, "r", encoding="utf-8") as file:
       self.index_dict = json.load(file)
    file.close()


  #get search query from user
  def get_query(self):
    self.original_query = input("Enter: ")
    self.search_query = self.tokenize_and_lemmatize_search_query()

  #returns list of doc id from final_index
  def tokenize_and_lemmatize_search_query(self):
    tokens = tokenize(self.original_query)
    lemmatized_tokens = lemmatize(tokens)
    return lemmatized_tokens


  def search_query_term_from_index(self):
    docID_dict = defaultdict(int)
    temp_list = []
    
    

    #create list of list, where each inner list is the urls for 1 word in the query
    for search_query_token in self.search_query:
      temp_list.append([])
      for index in self.index_dict.keys():
        if index == search_query_token:
          temp_list[-1] = self.index_dict[index]

    #add tf idf and html tag score for each token
    for docList in temp_list:
      for doc in docList.keys():
        docID_dict[doc] += docList[doc][0] + docList[doc][1]
        
    
    # #if search query was only 1 word long
    # if len(temp_list) == 1:
    #   for dict in temp_list[0]:
    #     docID_list.append(dict)

    # #if search query was more than 1 word
    # #find token that had the most urls by sorting
    # elif len(temp_list) > 1:
    #   temp_list.sort(key=lambda x: len(x), reverse=True)
    #   #iterate over the urls in the longest url list
    #   for url in temp_list[0]:
    #     in_all_dicts = True
    #     #check that url is in other url list for other tokens in search query as well
    #     for dict in temp_list[1:]:
    #       if url not in dict:
    #         in_all_dicts = False
    #         break
    #     if (in_all_dicts):
    #       docID_list.append(url)
    
        


    #print(docID_dict)

    #sort docs by score
    sorted_docs = [i[0] for i in sorted(docID_dict.items(), key=lambda x:x[1], reverse=True)]

    #print(sorted_docs[0:21])

    print("from search query function: ")
    print(f"total urls found for {self.original_query}: {len(sorted_docs)}")


    return sorted_docs
      
  
#returns list of links from docID_list
  def get_link_from_docID_list(self, docID_list):
    link_list = []
    file_path = "WEBPAGES_RAW"
    with open(os.path.join(file_path, "bookkeeping.json")) as f:
        file_dict = json.load(f)
    
    # for file_location in file_dict.keys():
    #   for doc_id in docID_list:
    #     if(file_location == doc_id):
    #       link_list.append(file_dict[doc_id])
        
    for doc in docID_list:
      link_list.append(file_dict[doc])
    
    self.write_ouput_file(link_list)
    return link_list
  
  # calculate query tf-dif score
  def calculate_query_tfidf(self):
      scores = []
      for term in self.search_query:
        tf= self.search_query.count(term) / len(self.search_query)
        idf = log10(36614/ len(self.index_dict[term]))
        scores.append(tf*idf)

      self.query_tfidf_scores = scores

  # calcualte cosine similarity between query and doc
  def calculate_cosine_similarity(self):
    similarity_scores = {}

    return similarity_scores


#prints out related links for search query 
  def print_out_query_links(self, link_list):
    print(self.original_query)
    for link in link_list:
      print(link + "\n")


#print out first 20 links for search query
  def print_out_20_query_links(self, link_list):
    print(self.original_query)
    print("First 20 (or less) links: ")
    for link in range(0,min(len(link_list),21)):
      print(link_list[link] + "\n")
    
# write output into file (I just use it to see return value for each function)  
  def write_ouput_file(self,list):
    file_name = "search_query.txt"
    # length = 0
    with open(file_name, "w", encoding='utf-8') as file:
      file.write(f"Number of List: {len(list)}\n\n")

      for dict in list:
          file.write(f"{dict}\n\n")
          # length+=1
      file.write("\n")
      
    # print("from ouput file funtion: ")
    # print( length)

# test = basic_query()
# DocID = test.search_query_term_from_index("informatics")
# links = test.get_link_from_docID_list(DocID)
# test.print_out_query_links("uci", links)
