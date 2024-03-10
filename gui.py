import tkinter as tk
import webbrowser
from basic_query import basic_query
from bs4 import BeautifulSoup
from lxml import html
import lxml
import os
import os.path
import json
from collections import defaultdict
from format_text import tokenize, lemmatize

class SearchEngineGUI:
    def __init__(self, master):
        self.master = master
        master.title("Search Engine")
        #search label
        self.label = tk.Label(master, text='What would you like to search?:')
        self.label.pack()
        #entry widget for input
        self.entry = tk.Entry(master)
        self.entry.pack()
        #search button to trigger search
        self.button = tk.Button(master, text="Search", command=self.perform_search)
        self.button.pack()
        #frame to contain results
        self.results_frame = tk.Frame(master)
        self.results_frame.pack(fill=tk.BOTH, expand=True)
        #pack within the frame
        self.results_canvas = tk.Canvas(self.results_frame)
        self.results_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        #scrollbar
        self.scroll = tk.Scrollbar(self.results_frame, orient="vertical", command=self.results_canvas.yview)
        self.scroll.pack(side=tk.RIGHT, fill='y')
        #allow results canvas to work with scrollbar
        self.results_canvas.configure(yscrollcommand=self.scroll.set)
        self.results_canvas.bind('<Configure>', self.on_canvas_configure)
        
        #create text widget inside canvas to display our links
        self.results_text = tk.Text(self.results_canvas, wrap=tk.WORD, state='normal', cursor='arrow')
        self.results_window = self.results_canvas.create_window((0,0), window=self.results_text, anchor='nw')
        
        #initialize the search query
        self.query_processor = basic_query()  
        self.link_count = 0 
    
    # adjusting our canvas based on its size
    def on_canvas_configure(self, event):
        self.results_canvas.configure(scrollregion=self.results_canvas.bbox("all"))
        if event:
            self.results_canvas.itemconfig(self.results_window, width=event.width)

    #handles search
    def perform_search(self):
        self.results_text.config(state='normal')
        self.results_text.delete(1.0, tk.END)

        search_query = self.entry.get()
        self.query_processor.original_query = search_query
        self.query_processor.search_query = self.query_processor.tokenize_and_lemmatize_search_query()
        docIDs = self.query_processor.search_query_term_from_index()
        links = self.query_processor.get_link_from_docID_list(docIDs)

        for link in range(0,min(len(links),20)):
            self.insert_clickable_link(links[link], docIDs[link])
        self.link_count = 0
        self.results_text.config(state='disabled')

        self.results_canvas.update_idletasks()
        self.on_canvas_configure(None)

    #get title for page
    def extract_title_and_description(self, html_file_location):
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

            title_text = ""

            for title in soup.find_all('title'):
                title_text += title.get_text()
            
            description = ""
            description_tag = soup.find('meta', attrs={'name': 'description'})
            if not description_tag:
                description_tag = soup.find('meta', attrs={'property': 'og:description'})

            if description_tag:
                description = description_tag.get('content')

            if description:
                description = description.strip()
            else:
                description = "N/A"



        except Exception as e:
            print(e)
            return ""
        
        return title_text,description

    #inserting 'hyperlink'
    def insert_clickable_link(self, link, docID):
        self.link_count += 1
        tag_name = f"link{self.link_count}"

        folder, file_name = docID.split("/")
        html_file_path = os.path.join("WEBPAGES_RAW", folder, file_name)

        title, description = self.extract_title_and_description(html_file_path)

        #no title found
        if (title == ""):
            self.results_text.insert(tk.END, str(self.link_count) + ". " + link + "\n", tag_name)
        #title found
        else:
            self.results_text.insert(tk.END, str(self.link_count) + ". " + title + "\n", tag_name)

            if description:
                self.results_text.insert(tk.END, "   Description: " + description + "\n")
        self.results_text.tag_config(tag_name, foreground="blue", underline=True)
        self.results_text.tag_bind(tag_name, "<Button-1>", lambda event, url=link: self.on_url_click(url))
        

    def on_url_click(self, url):
        webbrowser.open(url)

if __name__ == "__main__":
    root = tk.Tk()
    gui = SearchEngineGUI(root)
    root.mainloop()