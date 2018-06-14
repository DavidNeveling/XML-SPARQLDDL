import ply.yacc as yacc
from lex import *

def p_attributetype(p): #type
    'attributetype : TYPETAG XSITYPE HREF RWICKETEND'
    p[0] = p[3][p[3].rfind("/"):]
    

def p_classattribute(p): #ownedattribute
    '''
    classattribute : OWNEDATTRIBUTETAG XMIID NAME VISIBILITY RWICKET eannotation attributetype OWNEDATTRIBUTEENDTAG
                   | OWNEDATTRIBUTETAG XMIID NAME RWICKET eannotation attributetype OWNEDATTRIBUTEENDTAG
                   | OWNEDATTRIBUTETAG XMIID NAME TYPE RWICKET eannotation OWNEDATTRIBUTEENDTAG
                   | classattribute classattribute
    '''
    pass
    
def p_eannotationdetail(p):
    '''
    eannotationdetail : DETAILSTAG XMIID KEY VALUE RWICKETEND
                      | eannotationdetail eannotationdetail
    '''
    pass
        

def p_eannotation(p):
    '''
    eannotation : EANNOTATIONSTAG XMIID SOURCE RWICKET eannotationdetail EANNOTATIONSENDTAG
                | eannotation eannotation
    '''
    pass

def p_importedpackage(p):
    'importedpackage : IMPORTEDPACKAGETAG HREF RWICKETEND'
    pass

def p_packageimport(p):
    'packageimport : PACKAGEIMPORTTAG XMIID RWICKET eannotation importedpackage PACKAGEIMPORTENDTAG'
    pass

def p_packagedelement(p):
    '''
    packagedelement : PACKAGEDELEMENTTAG XSITYPE XMIID NAME RWICKET eannotation classattribute PACKAGEDELEMENTENDTAG
                    | PACKAGEDELEMENTTAG XSITYPE XMIID NAME RWICKET eannotation PACKAGEDELEMENTENDTAG
                    | PACKAGEDELEMENTTAG XSITYPE XMIID NAME MEMBEREND NAVIGABLEOWNEDEND RWICKET eannotation ownedend PACKAGEDELEMENTENDTAG
                    | packagedelement packagedelement
    '''
    if p[1] == '<packagedElement':
        temp = p[2][p[2].find(":") + 1:]
        if temp == 'Association':
            splitIndex = p[4].find("_")
            p[0] = (temp,p[4][0:splitIndex],p[4][splitIndex+1:],p[9])
        elif temp == 'Class':
            if p[7] == '</packagedElement>':
                p[0] = (temp,p[4])
            else:
                p[0] = (temp,p[4],p[7])
    else:
        p[0] = (p[1],p[2])

def p_lowervalue(p):
    '''
    lowervalue : LOWERVALUETAG XSITYPE XMIID RWICKET eannotation LOWERVALUEENDTAG
               | LOWERVALUETAG XSITYPE XMIID VALUE RWICKET eannotation LOWERVALUEENDTAG
    '''
    if p[5] == '>':
        p[0] = p[4]
    else:
        pass

def p_uppervalue(p):
    '''
    uppervalue : UPPERVALUETAG XSITYPE XMIID RWICKET eannotation UPPERVALUEENDTAG
               | UPPERVALUETAG XSITYPE XMIID VALUE RWICKET eannotation UPPERVALUEENDTAG
               | UPPERVALUETAG XSITYPE XMIID VALUE RWICKETEND
    '''
    if p[5] == '>' or p[5] == '/>':
        p[0] = p[4]
    else:
        pass

def p_ownedend(p):
    '''
    ownedend : OWNEDENDTAG XMIID NAME TYPE ASSOCIATION RWICKET eannotation lowervalue uppervalue OWNEDENDENDTAG
             | ownedend ownedend
    '''
    if p[1] == '<ownedEnd':
        p[0] = p[9]
    else:
        p[0] = (p[1],p[2])

def p_xmldata(p):
    'xmldata : XMLSTARTTAG VERSION ENCODING XMLENDTAG'
    pass

def p_umlmodel(p):
    'umlmodel : UMLMODELTAG XMIVERSION XMLNSXMI XMLNSXSI XMLNSUML XMIID NAME RWICKET eannotation packageimport packagedelement UMLMODELENDTAG'
    p[0] = (p[7],p[11])

def p_xmidoc(p):
    'xmidoc : xmldata umlmodel'
    p[0] = p[2]
    
def p_error(p):
    if p:
        print("parse error: {0}".format(p.value))
        parser.errok()
       
    else:
        print("Syntax error EOF")
        

    #p[0] = (p[4][0:splitIndex],p[4][splitIndex+1:]) #(CLASS1,CLASS2)
    
start = 'xmidoc'

parser = yacc.yacc()
