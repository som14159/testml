
import pandas as pd
import numpy as np
 
import math

def entropy(y):
    classes = np.unique(y)
    entropy = 0
    for c in classes:
        p = np.sum(y == c) / len(y)
        entropy -= p * math.log(p, 2)
    return entropy

def information_gain(X, y, attribute):
    entropy_before = entropy(y)
    values = np.unique(X[attribute])
    entropy_after = 0
    for value in values:
        subset_y = y[X[attribute] == value]
        entropy_after += (len(subset_y) / len(y)) * entropy(subset_y)
    return entropy_before - entropy_after

class Node:
    def __init__(self, attribute=None, result=None):
        self.attribute = attribute  
        self.result = result       
        self.children = {}          

def build_tree(X, y, attributes):
 
    if len(np.unique(y)) == 1:
        return Node(result=y.iloc[0])
 
    if len(attributes) == 0:
        print(y.value_counts())
        print(y.value_counts().idxmax())
        return Node(result=y.value_counts().idxmax())
 
    max_gain = -float('inf')
    best_attribute = None
    for attribute in attributes:
        gain = information_gain(X, y, attribute)
        if gain > max_gain:
            max_gain = gain
            best_attribute = attribute
    node = Node(attribute=best_attribute)
    values = np.unique(X[best_attribute])
 
    for value in values:
        subset_X = X[X[best_attribute] == value].drop(columns=[best_attribute])
        subset_y = y[X[best_attribute] == value]
        if len(subset_X) == 0:
            node.children[value] = Node(result=y.value_counts().idxmax())
        else:
            node.children[value] = build_tree(subset_X, subset_y, attributes.drop(best_attribute))
 
    return node

def predict(node, instance):
    if node.result is not None:
        return node.result
    else:
        value = instance[node.attribute]
        print(node.attribute)
        print(value)
        return predict(node.children[value[0]], instance)

df = pd.read_csv("PlayTennis.csv")
print(df)
y = df["Play Tennis"]
X = df.drop(columns=["Play Tennis"])

attributes = X.columns
 
print("Attributes : ",attributes)
 
root = build_tree(X, y, attributes)

 
 
import networkx as nx
import matplotlib.pyplot as plt
 
 
# Example usage
# Call print_tree(root) where root is the root node of your decision tree
import random
 
    
def hierarchy_pos(G, root=None, width=3.0, vert_gap = 5.2, vert_loc = 0, xcenter = 0.5):
 
    if not nx.is_tree(G):
        raise TypeError('cannot use hierarchy_pos on a graph that is not a tree')
 
    if root is None:
        if isinstance(G, nx.DiGraph):
            root = next(iter(nx.topological_sort(G)))  #allows back compatibility with nx version 1.11
        else:
            root = random.choice(list(G.nodes))
 
    def _hierarchy_pos(G, root, width=3.0, vert_gap = 5.2, vert_loc = 0, xcenter = 0.5, pos = None, parent = None):
        if pos is None:
            pos = {root:(xcenter,vert_loc)}
        else:
            pos[root] = (xcenter, vert_loc)
        children = list(G.neighbors(root))
        if not isinstance(G, nx.DiGraph) and parent is not None:
            children.remove(parent)  
        if len(children)!=0:
            dx = width/len(children) 
            nextx = xcenter - width/2 - dx/2
            for child in children:
                nextx += dx 
                pos = _hierarchy_pos(G,child, width = dx + 0.3, vert_gap = vert_gap, 
                                    vert_loc = vert_loc-vert_gap, xcenter=nextx,
                                    pos=pos, parent = root)
        return pos
    return _hierarchy_pos(G, root, width, vert_gap, vert_loc, xcenter)
 
valueOf ={}
def visualize_tree(node, G, pos=None, parent=None, x_pos=0, y_pos=0,edge_label="x"):
    if pos is None:
        pos = {}
    pos[node] = (x_pos, y_pos)
    if parent is not None:
        G.add_edge(parent, node)
        if(edge_label!="x"):
            G[parent][node]['label'] = edge_label
    if node.children:
        num_children = len(node.children)
        delta_x = 1 / (num_children + 1)
        x_child = x_pos - 0.5 + delta_x
        y_child = y_pos - 1
        for value, child_node in node.children.items():
            valueOf[child_node]=value
            visualize_tree(child_node, G, pos, node, x_child, y_child,value)
            x_child += delta_x
 
def print_tree(node):
    G = nx.Graph()
    visualize_tree(node, G)
    pos = hierarchy_pos(G, node)
    labels={}
    for node in G.nodes():
        if node.attribute :
            labels[node]=node.attribute
        else:
            labels[node]=node.result
    nx.draw(G, pos=pos, with_labels=True, labels=labels,node_color="white",font_size = 8)
    edge_labels = nx.get_edge_attributes(G, 'label')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels,font_size = 8)
    plt.show()
 
print("Decision Tree:")
 
print_tree(root)

 
outlook = input("Enter Outlook (Sunny/Overcast/Rain): ")
temperature = input("Enter Temperature (Hot/Mild/Cool): ")
humidity = input("Enter Humidity (High/Normal): ")
wind = input("Enter Wind (Weak/Strong): ")
data = {
    'Outlook': [outlook],
    'Temperature': [temperature],
    'Humidity': [humidity],
    'Wind': [wind]
}
instance_df = pd.DataFrame(data)
print("Prediction for : \n",instance_df,"\nis ",predict(root,instance_df));