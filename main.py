from yacc import *
import sys, os

#Main program initializers
ptok = False;

datafile = 'finalproject.xmi'
if len(sys.argv) > 1:
    datafile = sys.argv[1]

file = open(datafile, "rU")

data = file.read(os.stat(datafile).st_size)


lexer = lex.lex() #Initialize lexer
lexer.input(data) #Feed lexer input
if ptok:
    for tok in lexer: print(tok) #View tokens

parsetree = parser.parse(data)
#unwrap model name
modelname = parsetree[0]
#advance in parse tree
parsetree = parsetree[1]
#pull out elements
elements = [modelname]
while type(parsetree[1]) is tuple:
    elements.append(parsetree[0])
    parsetree = parsetree[1]
elements.append(parsetree)


namespace = elements[0]

elements = elements[1:]

sparqlDDL = "@prefix owl: < http://www.w3.org/2002/07/owl > .\n\
@prefix rdf: < http://www.w3.org/1999/02/22-rdf-syntax-ns > .\n\
@prefix rdfs: < http://www.w3.org/2000/01/rdf-schema > .\n\
@prefix schema: < http://schema.org/ > .\n\
@prefix sh: < http://www.w3.org/ns/shacl > .\n\
@prefix xsd: < http://www.w3.org/2001/XMLSchema > .\n\
@prefix " + namespace + ": < http://" + namespace + ".org/ > .\n\n"

associations = ""

for item in elements:
    if item[0] == 'Class':
        sparqlDDL += namespace+":"+item[1]+"\n\trdf:type rdfs:Class ;\n\trdf:type sh:NodeShape ;\n\trdfs:label \""+item[1]+"\" ;\n\trdfs:subClassOf schema:Thing .\n\n"

    if item[0] == 'Association':
        associations += namespace + ":" + item[1] + "Has" + item[2] + " owl:inverseOf " + namespace + ":" + item[2] + "Has" + item[1] + " .\n"
    
sparqlDDL += associations    

f = 0
if len(sys.argv) > 2:
    f = open(sys.argv[2], 'w')
else:
    f = open('addToSchema.n3', 'w')
    
f.write(sparqlDDL)    

print("File Created")