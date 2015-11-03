
# coding: utf-8

# In[1]:

from rdflib import Graph, Namespace, RDF, Literal, RDFS
import csv, os

g = Graph()

HISCO = Namespace('http://qber.data2semantics.org/vocab/ocs/hisco/')
MAJOR = Namespace('http://qber.data2semantics.org/vocab/ocs/hisco/majorGroup/')
SKOS  = Namespace('http://www.w3.org/2004/02/skos/core#')    
    
g.bind('hisco', HISCO)
g.bind('major', MAJOR)
g.bind('skos', SKOS)

default_path = "/Users/RichardZ/Dropbox/II/projects/clariah/sdh/basecamp/Files/Files attached directly to project/Files attached directly to project (1)/"
os.chdir(default_path)
hdf = open('./data2rdf/hisco/hisco_1.csv')
hisco = csv.reader(hdf)

next(hisco)

g.add((HISCO[''], RDF.type, SKOS['Collection']))

variable_name = 'majorGroup'
g.add((HISCO[variable_name], RDF.type, SKOS['ConceptScheme']))
g.add((HISCO[variable_name], SKOS.prefLabel, Literal('major group','en')))
g.add((HISCO[variable_name], SKOS.editorialNote, 
       Literal("For consistency with categories, unit groups and minor groups, the major groups '0/1' and '7/8/9' are split and treated as seperate major groups: 0,1,7,8,9",'en')))
g.add((HISCO[variable_name], SKOS.member, HISCO[''])) 



for row in hisco: # define and columns and names for columns
    hisco_major_group = row[1]
    hisco_major_group_label = row[2]
    hisco_major_group_description = row[3]
    
    g.add((MAJOR[hisco_major_group], RDF.type, SKOS['Concept']))
    g.add((MAJOR[hisco_major_group], SKOS['inScheme'], HISCO[variable_name]))
    g.add((MAJOR[hisco_major_group], SKOS['prefLabel'], Literal(hisco_major_group_label,'en')))
    g.add((MAJOR[hisco_major_group], SKOS['definition'], Literal(hisco_major_group_description,'en')))

print g.serialize(format='turtle')

with open('./rdf/hisco/hisco_major_group.ttl','w') as out:
    g.serialize(out, format='turtle')


# In[ ]:




# In[ ]:




# In[ ]:



