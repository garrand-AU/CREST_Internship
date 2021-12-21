import re
import networkx as nx
import matplotlib.pyplot as plt


class graph():

    nodes = []

    def __inti__(self):
        self.nodes =[]

    def add_vertex(self,name, addr, type):
        v = self.vertex(name, addr, type)
        self.nodes.append(v)

    def add_edge(self, v1, v2):
        for n in self.nodes:
            if v1 == n.get_name():
                n.add_edge(v2)
            if v2 == n.get_name():
                n.add_edge(v1)

    def get_nodes(self, name):
        for n in self.nodes:
            if name == n.get_name():
                return n

    def get_nodes(self):
        return self.nodes

    def get_edge(self, v):
        for n in self.nodes:
            if v == n.get_name():
                return n.get_edge()
        return []

    # def search_vertex():
    #     pass
    def delete_vertex(self, v):
        tmp=self.vertex('','',0)
        # remove edges
        index = 0
        for n in self.nodes:
            # find v vertex

            if v == n.get_name():
                # tmp  = n
                # get v's edges
                edges = n.get_edge()
                # print(edges)
                for e in edges:
                    # delete edges in corresponding vertices
                    for ns in self.nodes:
                        if e == ns.get_name():
                            ns.del_edge(v)
                # remove vertex
                del self.nodes[index]
                # tmp = self.nodes.pop(index)
                print("test point:")
                # tmp.print_vertex()
                return
            index += 1



    def delete_edge(self, v1, v2):
        v1_exist = False
        v2_exist = False
        n_v1 = self.vertex('','',0)
        n_v2 = self.vertex('','',0)

        for n in self.nodes:
            if v1 == n.get_name():
                v1_exist = True
                n_v1 = n
            if v2 == n.get_name():
                v2_exist = True
                n_v2 = n

        # if the edge exists, delete it
        if v1_exist and v2_exist:
            n_v1.del_edge(v2)
            n_v2.del_edge(v1)

        # pass
    # def modify_vertex():
    #     pass
    # def modify_edge():
    #     pass
    def print_graph(self):
        print("Total nodes:" + str(len(self.nodes)))
        for v in self.nodes:
            v.print_vertex()
    class vertex():
        # name = ''
        # addr = ''
        # type = 0
        # edge = []

        def __init__(self, name, addr, type):
            self.name = name    # string name
            self.addr = addr    # address
            self.type = type
            self.edge = []

        def add_edge(self, v):
            # print("adding " + v + " to " + self.name)
            self.edge.append(v)
            # print(len(self.edge))

        def del_edge(self,name):
            # for e in self.edge:
            print(self.edge.index(name))

            self.edge.remove(name)


        # def search_edge():
        #     pass

        def get_name(self):
            return self.name

        def get_edge(self):
            return self.edge

        def get_addr():
            return self.addr

        # def modify_edge():
        #     pass
        def print_vertex(self):
            print(self.name + " "+ self.addr + " "+ str(self.type))
            print("with edges:")
            for e in self.edge:
                print(e)

# find the shortest path

# breath first search algorithm

# width first search algorithm



def main():

    name = ''
    address = ''
    type = 0
    edge =[]
    G = graph()
    # print("test")
    # G.print_graph()
    # exit(0)
    # read file to contruct a graph
    line_is_node = False
    with open("graph.txt", "r") as fin:
        for line in fin:
            line = line.rstrip()
            if "#name" in line:
                line_is_node = True
                continue

            if "#edges" in line:
                line_is_node = False
                continue

            if ',' not in line:
            # if not line:
                # only one column in this line, skip
                continue

            if line_is_node:
                print(line)
                name, address, type = line.split(",")
                G.add_vertex(name, address, type)
            # G.print_graph()
            else:
                v1, v2 = line.split(",")
                G.add_edge(v1,v2)


    # draw net work of nodes in the graph

    # g_net_work = nx.Graph()
    #
    # nodes = G.get_nodes()
    # for v in nodes:
    #     e = v.get_edge()
    #     name = v.get_name()
    #     g_net_work.add_node(name)
    #     for i in e:
    #         g_net_work.add_edge(name,i)
    #
    # nx.draw(g_net_work, with_labels=1)
    # plt.show()

    G.delete_edge('server', 'agent6')

    g_net_work = nx.Graph()

    nodes = G.get_nodes()
    for v in nodes:
        e = v.get_edge()
        name = v.get_name()
        g_net_work.add_node(name)
        for i in e:
            g_net_work.add_edge(name,i)

    nx.draw(g_net_work, with_labels=1)
    plt.show()

    g_net_work = nx.Graph()

    G.delete_vertex('agent5')

    G.print_graph()

    nodes = G.get_nodes()
    for v in nodes:
        e = v.get_edge()
        name = v.get_name()
        g_net_work.add_node(name)
        for i in e:
            g_net_work.add_edge(name,i)

    nx.draw(g_net_work, with_labels=1)
    plt.show()

    # print(f.readline())




# G = nx.Graph()

# G = nx.nodes(R1)

# G = nx.path_graph(10)
# G = nx.complete_graph(10)

# G = nx.gnp_random_graph(10, 0.3)
# node_list = []
#
# def Creating_nodes_list(number):
#     for value in range(number):
#         var1 = "R"+str(value)
#         node_list.append(var1)
#     return node_list
# def Add_nodes(list1):
#     G.add_nodes_from(list1)
#
# def Add_nodes_random():
#     while
#
# node_list = Creating_nodes_list(10)
# Add_nodes(node_list)
#
# print(node_list)

# print(nx.info(G))
#
# nx.draw(G, with_labels=1)
# plt.show()

if __name__ == "__main__":
    main()
