import tkinter as tk
import webbrowser
from basic_query import basic_query

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
        
        for link in links:
            self.insert_clickable_link(link)
        self.results_text.config(state='disabled')

        self.results_canvas.update_idletasks()
        self.on_canvas_configure(None)
    #inserting 'hyperlink'
    def insert_clickable_link(self, link):
        self.link_count += 1
        tag_name = f"link{self.link_count}"
        self.results_text.insert(tk.END, link + "\n", tag_name)
        self.results_text.tag_config(tag_name, foreground="blue", underline=True)
        self.results_text.tag_bind(tag_name, "<Button-1>", lambda event, url=link: self.on_url_click(url))

    def on_url_click(self, url):
        webbrowser.open(url)

if __name__ == "__main__":
    root = tk.Tk()
    gui = SearchEngineGUI(root)
    root.mainloop()