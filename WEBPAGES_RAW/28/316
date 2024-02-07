#strict on __init__ must have/not have node/edge else exception
class Graph:
    """
    Implements a Graph data type: it can manipulate nodes and
      edges and provides many iterators
    """
    def __init__(self,strict=False,initial_graph=None):
        """
        Graph is constructed to store all the nodes and values in initial_graph
          (if it is present) otherwise no nodes and edges; a strict graph does not
          allow re-adding edges or values (they must be removed before re-adding);
          it will raise more exceptions
        """
        self._nodes = dict()
        self._edges = dict()
        self._strict = strict
        if initial_graph != None:
            assert type(initial_graph) is Graph, 'Graph:__init__ initial_graph not a Graph'
            for n in initial_graph._nodes:
                self.add_node(n)
            for e in initial_graph._edges:
                self.add_edge(e,initial_graph._edges[e])
                
                
    class NodeInfo:
        """
        NodeInfo stores the set of incoming and outgoing edges for every node
        """
        def __init__(self):
            self._in_edges  = set()
            self._out_edges = set()
            
            
    def add_node(self,n):
        """
        Add a node to the graph
        In a strict graph, it must not already be present
        """
        assert not self._strict or not self.has_node(n), 'Graph:add_node strict and re-adding node n('+str(n)+')'
        if not self.has_node(n):
            self._nodes[n] = Graph.NodeInfo()

    
    def add_edge(self,e,value):
        """
        Add an edge to the graph
        In a strict graph, the node must be in the graph and edge must not be in the graph
        """
        assert type(e) is tuple and len(e) == 2, 'Graph:add_edge invalid edge e('+ str(e)+' with value '+str(value)+')'
        assert not self._strict or not self.has_edge(e), 'Graph:add_edge strict and re-adding edge e('+str(e)+' with value '+str(value)+')'
        o,d = e[0],e[1]
        assert not self._strict or self.has_node(o), 'Graph:add_edge strict and origin node ('+ str(o)+') not in graph'
        assert not self._strict or self.has_node(d), 'Graph:add_edge strict and destination node ('+ str(d)+') not in graph'
        if not self._strict:
            self.add_node(o)
            self.add_node(d)
        self._edges[e] = value
        self._nodes[o]._out_edges.add(e)
        self._nodes[d]._in_edges.add(e)
        
        
    def remove_node(self,n):
        """
        Remove a node from the graph
        In a strict graph, the node must be in the graph
        """
        assert not self._strict or self.has_node(n), 'Graph:remove_node strict and node n('+str(n)+') not in graph'
        if not self.has_node(n):
            return
        # use an extra list because removing from iterable
        ni = self._nodes[n]
        for e in tuple(ni._in_edges):
            self.remove_edge(e)
        for e in tuple(ni._out_edges):
            self.remove_edge(e)
        del self._nodes[n]
    
    
    def remove_edge(self,e):
        """
        Remove an edge from the graph
        In a strict graph, both nodes and the edge must be in the graph
        """
        assert type(e) is tuple and len(e) == 2, "Graph:remove_edge invalid edge"
        o,d = e[0],e[1]
        assert not self._strict or self.has_node(o), 'Graph:remove_edge strict and origin node ('+ str(o)+') not in graph'
        assert not self._strict or self.has_node(d), 'Graph:remove_edge strict and destination node ('+ str(d)+') not in graph'
        assert not self._stric or self.has_edge(e), 'Graph:remove_edge strict and edge e('+str(e)+') not in graph'
        if not self.has_edge(e):
            return
        del self._edges[e]
        self._nodes[o]._out_edges.remove(e)
        self._nodes[d]._in_edges.remove(e)
 
        
    def clear(self):
        """
        Clear the graph of any nodes and values
        """
        self._nodes = dict()
        self._edges = dict()
  
        
    def read(self,file,conv=(lambda x : x),sep=' '):
        """
        Read a graph from a text file; assume sep is separating the nodes and edge values
        conv converts the string value of an edge into the appropriate type of value
        Graphs written by write should be readable by read
        """
        nodes_only = True
        for line in file:
            if line == 'NODESABOVEEDGESBELOW\n':
                nodes_only = False
                continue
            if nodes_only:
                self.add_node(line.strip())
            else:
                e = line.strip().split(sep)
                self.add_edge((e[0],e[1]),conv(e[2]))
        
    
    def write(self,file,conv=str,sep=' '):
        """
        Write a graph into a text file; use sep to separate the nodes and edge values
        conv converts the value of an edge into the appropriate string (with str the default)
        Graphs written by write should be readable by read
        """
        for n in sorted(self._nodes):
            file.write(str(n)+'\n')
        file.write('NODESABOVEEDGESBELOW\n')
        for e in sorted(self._edges.items()):
            file.write(str(e[0][0])+sep+str(e[0][1])+sep+str(e[1])+'\n')
        file.close()    
    
    
    def node_count(self):
        """
        Return the number of nodes in the graph
        """
        return len(self._nodes)
    
    
    def edge_count(self):
        """
        Return the number of edges in the graph
        """
        return len(self._edges)
    
    
    def is_empty(self):
        """
        Return whether the graph is empty (of nodes)
        """
        return self.node_count() == 0
    
    
    def has_node(self,n):
        """
        Return whether the graph stores a node
        """
        return n in self._nodes
    
    
    def has_edge(self,e):
        """
        Return whether the graph stores an edge
        """
        return e in self._edges
    
    
    def edge_value(self,e):
        """
        Return the value of an edge in the graph
        In a strict graph,  both nodes and the edge must be in the graph
        """
        assert type(e) is tuple and len(e) == 2, "Graph:edge_value invalid edge"
        o,d = e[0],e[1]
        assert not self._strict or self.has_node(o), 'Graph:edge_value strict and origin node ('+ str(o)+') not in graph'
        assert not self._strict or self.has_node(d), 'Graph:edge_value strict and destination node ('+ str(d)+') not in graph'
        assert not self._strict or self.has_edge(e), 'Graph:edge_value strict and edge e('+str(e)+') not in graph'
        return self._edges[e]

    
    def in_degree(self,n):
        """
        Return the in-degree (number of edges with this node as their destination) of a node
        In a strict graph, the node must be in the graph
        """
        assert not self._strict or self.has_node(n), 'Graph:in_degree strict and node n('+str(n)+') not in graph'
        return len(self._nodes[n]._in_edges) if n in self._nodes else 0
   
            
    def out_degree(self,n):
        """
        Return the out-degree (number of edges with this node as their origin) of a node
        In a strict graph, the node must be in the graph
        """
        assert not self._strict or self.has_node(n), 'Graph:out_degree strict and node n('+str(n)+') not in graph'
        return len(self._nodes[n]._out_edges) if n in self._nodes else 0
    
            
    def degree(self,n):
        """
        Return the degree (number of edges with this node as their origin or destination) of a node
        In a strict graph, the node must be in the graph
        """
        assert not self._strict or self.has_node(n), 'Graph:degree strict and node n('+str(n)+') not in graph'
        return self.in_degree(n) + self.out_degree(n)
    
    
    def nodes(self):
        """
        Return an iterator for a copy of all nodes in the graph (in no special order)
        """
        return iter(tuple(self._nodes))
    
    
    def edges(self):
        """
        Return an iterator for a copy of all edges in the graph (in no special order)
        """
        return iter(tuple(self._edges))
    
   
    def in_nodes(self,n):
        """
        Return an iterator for a copy of all in nodes that have an edge with this node as its destination
        In a strict graph, the node must be in the graph
        """
        assert not self._strict or self.has_node(n), 'Graph:in_nodes strict and node n('+str(n)+') not in graph'
        return iter((e[0] for e in self._nodes[n]._in_edges)) if n in self._nodes else iter([])
    
    
    def out_nodes(self,n):
        """
        Return an iterator for a copy of all in nodes that have an edge with this node as its origin
        In a strict graph, the node must be in the graph
        """
        assert not self._strict or self.has_node(n), 'Graph:out_nodes strict and node n('+str(n)+') not in graph'
        return iter((e[0] for e in self._nodes[n]._out_edges)) if n in self._nodes else iter([])
    
   
    def in_edges(self,n):
        """
        Return an iterator for a copy of all in edges with this node as its destination
        In a strict graph, the node must be in the graph
        """
        assert not self._strict or self.has_node(n), 'Graph:in_edges strict and node n('+str(n)+') not in graph'
        return iter(tuple(self._nodes[n]._in_edges)) if n in self._nodes else iter([])
   
    def out_edges(self,n):
        """
        Return an iterator for a copy of all in edges with this node as its origin
        In a strict graph, the node must be in the graph
        """
        assert not self._strict or self.has_node(n), 'Graph:out_edges strict and node n('+str(n)+') not in graph'
        return iter(tuple(self._nodes[n]._out_edges)) if n in self._nodes else iter([])
    
    
    def __str__(self):
        if self.is_empty():
            return 'Empty (no nodes or edges)'
        s = ""
        for n in sorted(self._nodes):
            s += 'Node ' + str(n) + ':\n  Out edges:'
            for e in sorted(self.out_edges(n),key=lambda e : e[1]):
                s += '  ' + str(e[0]) + '-(' + str(self.edge_value(e)) + ')->' + str(e[1])
            s += '\n  In  edges:'
            for e in sorted(self.in_edges(n),key=lambda e : e[0]):
                s +=  '  ' + str(e[0]) + '-(' + str(self.edge_value(e)) + ')->' + str(e[1])
            s += '\n\n'
        return s


    def __bool__(self):
        """
        Determine the truth of a graph: non-empty graphs are True
        """
        return not self.is_empty()





def random_graph(nodes,percent):
    from goody import irange
    from random import random,randint
    g = Graph()
    for i in irange(nodes):
        g.add_node(str(i))
    for i in irange(nodes):
        for j in irange(nodes):
            if 100*random() <= percent:
                g.add_edge((str(i),str(j)),randint(0,100))
    return g
   
   
def make_symmetric(g):
    for e in g.edges():
        if not g.has_edge((e[1],e[0])):
            g.add_edge((e[1],e[0]),g.edge_value(e))    
        
    
def connected_components(g):
    from equivalence import EquivalenceClass as EC
    ec = EC(g.nodes())
    for e in g.edges():
        ec.merge_classes_containing(e[0],e[1]) 
    return ec.all_classes()
    

def minimum_spanning_tree(g):
    from priorityqueue import PriorityQueue as PQ
    from equivalence   import EquivalenceClass as EC
    answer = Graph()
    ec = EC(g.nodes())
    # Smaller edge values have higher priority
    for e in PQ(g.edges(),key=(lambda e : g.edge_value(e)),reverse=True):
        if not ec.in_same_class(e[0],e[1]):
            ec.merge_classes_containing(e[0],e[1]) 
            answer.add_edge(e,g.edge_value(e))
        if answer.edge_count() == g.node_count()-1:
            break
    else: return None
    return answer
    

if __name__ == '__main__': 
    import prompt,predicate
    from   goody import safe_open
    
    def prompt_edge(description):
        print(description)
        i = prompt.for_string('  Origin      node')
        o = prompt.for_string('  Destination node')
        return (i,o)
    
    print('Begin testing Graph') 
    command_prompt = \
"""\nTesting Graph:
Commands           Queries               Other                          Graph Algorithms
  an - add_node      nc - node_count       . - exec(...)                  rg  - random graph
  ae - add_edge      ec - edge_count       in  - iterator node            cc  - connected components
  rn - remove_node   mt - is_empty         ie  - iterator edges           mst - minimum spanning tree
  re - remove_edge   hn - has_node         iin - iterator in_node         sym - make symmetric
  c  - clear         he - has_edge         ion - iterator out_nodes
                     e  - edge_value       iie - iterator in_edges
                     id - in_degree        ion - iterator out_edges
                     od - out_degree       r   - read
                     d  - degree           w   - write
                     _  - str              q   - quit
                     
               
Command""" 
    g = eval('Graph('+input('g = Graph('))
    while True:
        action = prompt.for_string(command_prompt, is_legal= \
                 lambda x : x in 'an ae rn re c nc ec mt hn he e id od d _ . in ie iin ion iie ion r w q rg cc mst sym'.split(' '))
        try:
            if   action == 'an': g.add_node(prompt.for_string('  Enter node to add'))
            elif action == 'ae': g.add_edge(prompt_edge('  Enter edge to add'),prompt.for_int('  Value (int) for edge',is_legal=predicate.is_non_negative))
            elif action == 'rn': g.remove_node(prompt.for_string('  Enter node to remove'))
            elif action == 're': g.remove_edge(prompt_edge('  Enter edge to remove'))
            elif action == 'c' : g.clear()
            
            elif action == 'nc': print('  node_count =',g.node_count())
            elif action == 'ec': print('  edge_count =',g.edge_count())
            elif action == 'mt' : print('  is_empty =',g.is_empty())
            elif action == 'hn':
                n = prompt.for_string('  Enter node to check')
                print('  has_node =',g.has_node(n))
            elif action == 'he':
                e = prompt_edge('  Enter edge to check')
                print('  has_edge =',g.has_edge(e))
            elif action == 'e' :
                e = prompt_edge('  Enter edge to get value')
                print('  edge_value =',g.edge_value(e))
            elif action == 'id':
                n = prompt.for_string('  Enter node to check')
                print('  in_degree =',g.in_degree(n))
            elif action == 'od':
                n = prompt.for_string('  Enter node to check')
                print('  out_degree =',g.out_degree(n))
            elif action == 'd' :
                n = prompt.for_string('  Enter node to check')
                print('  degree =',g.degree(n))
            elif action == '_': print('  str =\n',g,sep='')
            
            elif action == '.'  : exec(prompt.for_string('  Enter command to exec (instance=g)'))
            elif action == 'in' : print('  iteration order =',[i for i in g.nodes()])
            elif action == 'ie' : print('  iteration order =',[i for i in g.edges()])
            elif action == 'iin':
                n = prompt.for_string('  Enter node to check')
                print('  iteration order =',[i for i in g.in_nodes(n)])
            elif action == 'iie':
                n = prompt.for_string('  Enter node to check')
                print('  iteration order =',[i for i in g.in_edges(n)])
            elif action == 'ion':
                n = prompt.for_string('  Enter node to check')
                print('  iteration order =',[i for i in g.out_nodes(n)])
            elif action == 'ioe':
                n = prompt.for_string('  Enter node to check')
                print('  iteration order =',[i for i in g.out_edges(n)])
            elif action == 'q'  : break
            elif action == 'r'  : g.read(safe_open('  Enter file name to read','r','Could not find this file',default=None),conv=int,sep=';')
            elif action == 'w'  : g.write(safe_open('  Enter file name to write','w','Could not open this file for writing',default=None),sep=';')
            elif action == 'q'  : break
            
            elif action == 'rg'  : g = random_graph(prompt.for_int('  Enter number of nodes in graph',is_legal=predicate.is_non_negative), prompt.for_int_between('  Enter connectivity percentage',0,100))
            elif action == 'cc'  : print(connected_components(g))
            elif action == 'mst' : print(minimum_spanning_tree(g))
            elif action == 'sym' : make_symmetric(g)
            else: print('  Unknown command')
        except AssertionError as report:
            print('  AssertionError exception caught:', report)
        except Exception as report:
            import traceback
            traceback.print_exc()
    print('\nFinished testing Graph')