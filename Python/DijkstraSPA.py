import json
from pprint import pprint

def process(graph):
    #pprint(graph)
    shortest_tree = [] 

def run(path):
    graph = read(path)
    process(graph)

def read(path):
    with open(path) as jf:
        graph = json.load(jf)
    return graph

run('./ShortestPathGraph.json')