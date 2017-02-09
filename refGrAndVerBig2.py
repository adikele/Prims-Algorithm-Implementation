#refVr


#imp deductions:
#'nbr' in the addNeighbor method refers to a vertex object.
#keys of connectedTo are vertex objects

#who can use vertex? a vertex id fellow or a real vertex fellow?
class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}

    #what could be the pros and cons: for 'nbr' in the following, using vertex's id or the object itself?
    def addNeighbor(self,nbr,weight=0): #right now we don't know whether 'nbr' refers to another vertex's id or the object itself but katso *1
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self,nbrMalegaon): #needs parameter -- key of connectedTo, which is a vertex object
        return self.connectedTo[nbrMalegaon]

#imp deductions:
#vertList (key, vaule): key has the id of the vertex and value points to the vertex object (and can be used to refer to the vertex object's methods)

#2.2.2017 -- so you can initialize a graph without any parameters!                                                                                        
class Graph:
    def __init__(self):
        self.vertList = {}
        #adi: vertList (key, vaule): key has the id of the vertex and value points to the vertex object (and can be used to refer to the vertex object's methods) 
        self.numVertices = 0

    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.vertList
        #adi: apparently this method does nothing -- program works the same


    def addEdge(self,f,t,cost=0): #takes the ids of two vertices and the cost of the link between them
        if f not in self.vertList:
            nv = self.addVertex(f) #here 'nv' has no importance
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost) # *1katso! because vertList[t] points to the vertex object, we know that addNeighbor takes a vertex object
        #and not a vertex object's id. So 'nbr' in the addNeighbor method refers to a vertex object.

    def getVertices(self):
        return self.vertList.keys()

    #checks whether given two vertices, a and b, are connected or not
    #connection means a to b or b to a
    #if a or b or both are not vertices, returns false
    #need to add code for reverse direction
    def NeighboursJoo (self, a, b):
        if a not in self.vertList:
            return false
        if b not in self.vertList:
            return false
        #if a and b both in self.vertList
        #self.vertList[a] this will give us access to the vertex object "a"
        #keys of connectedTo are vertex objects
        #getConnections() returns self.connectedTo.keys()

        #for i in self.vertList[a].getConnections().id == b:
            #return true

        #testo1 = self.vertList[a].connectedTo.keys()

        #testo1 = self.vertList[a].connectedTo.keys()
        #print (testo1) 

        for i in self.vertList[a].connectedTo.keys():
            #print (i.id)
            if i.id == b: #test that a and b are connected
                costo = self.vertList[a].connectedTo[i]
                if costo < 6:
                    return True
                
        
    def __iter__(self):
        return iter(self.vertList.values())

    
    def connectedOrNot(self, a, b):
        if a not in self.vertList:
            return false
        if b not in self.vertList:
            return false
        #if a and b both in self.vertList
        #self.vertList[a] this will give us access to the vertex object "a"
        #keys of connectedTo are vertex objects
        #values of connectedTo are coss between the two vertices
        
        #getConnections() returns self.connectedTo.keys()

        #testo1 = self.vertList[a].connectedTo.keys()

        #testo1 = self.vertList[a].connectedTo.keys()
        #print (testo1) 

        for i in self.vertList[a].connectedTo.keys():
            #print (i.id)
            if i.id == b:
                return True
                #break

    def LagiWalaCostDivpi(self, a):
        if a not in self.vertList:
             return false
        
        #if a and b both in self.vertList
        #self.vertList[a] this will give us access to the vertex object "a"
        #keys of connectedTo are vertex objects
        #values of connectedTo are costs between the two vertices
        
        #getConnections() returns self.connectedTo.keys()

        #testo1 = self.vertList[a].connectedTo.keys()

        #testo1 = self.vertList[a].connectedTo.keys()
        #print (testo1)
        listo = []

         #print (i.id)
        for i in self.vertList[a].connectedTo.keys(): #i is a vertex object that a is connected to
             tmp = self.vertList[a].getWeight(i)
             listo.append(tmp)
             #print (listo) #test

        final = min (listo) # final has the least cost
        return final

    def LagiWalaIdDivpi(self, a):
        if a not in self.vertList:
             return false
    
        listo = []
        #pakad = 1000
        #print (i.id)
        for i in self.vertList[a].connectedTo.keys(): #i is a vertex object that a is connected to
             tmp = self.vertList[a].getWeight(i) #tmp is a cost
             listo.append(tmp)
             if min (listo) == tmp:
                 pakad = i.id
              #test

        final = pakad # final has the least cost
        return final

    def getWeight(self, a, b):
        if a not in self.vertList:
             return false
        if b not in self.vertList:
             return false
    
        #cost = self.vertList[a].getWeight(self.vertList[b])
        cost = self.vertList[a].connectedTo[self.vertList[b]] 
        return cost
                
