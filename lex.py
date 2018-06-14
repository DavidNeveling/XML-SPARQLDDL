import ply.lex as lex

tokens = (
    'RWICKETEND', # />
    'RWICKET', # >
    'XMIID', # xmi:id=""
    'XMIVERSION', # xmi:version="" 
    'XMLNSXMI', # xmlns:xmi=""
    'XMLNSXSI', # xmlns:xsi="" 
    'XMLNSUML', # xmlns:uml=""
    'NAME', # name=""
    'EANNOTATIONSTAG', # <eAnnotations
    'EANNOTATIONSENDTAG', # </eAnnotations>
    'SOURCE', # source=""
    'KEY', # key=""
    'VALUE', # value=""
    'PACKAGEIMPORTTAG', # <packageImport
    'PACKAGEIMPORTENDTAG', # </packageImport>
    'IMPORTEDPACKAGETAG', # <importedPackage
    #'IMPORTEDPACKAGEENDTAG', # </importedPackage>
    'PACKAGEDELEMENTTAG', # <packagedElement
    'PACKAGEDELEMENTENDTAG', # </packagedElement>
    'XSITYPE', # xsi:type=""
    #'DETAILS', # details=""
    'OWNEDATTRIBUTETAG', # <ownedAttribute
    'OWNEDATTRIBUTEENDTAG', #</ownedAttribute>
    'VISIBILITY', # visibility=""
    'HREF', # href=""
    'TYPE', # type=""
    'TYPETAG', # <type
    #'TYPETAGENDTAG', # </type>
    'MEMBEREND', # memberEnd=""
    'NAVIGABLEOWNEDEND', # navigableOwnedEnd=""
    'ASSOCIATION', # association=""
    'OWNEDENDTAG', # <ownedEnd
    'OWNEDENDENDTAG', # </ownedEnd>
    'LOWERVALUETAG', # <lowerValue
    'LOWERVALUEENDTAG', # </lowerValue>
    'UPPERVALUETAG', # <upperValue
    'UPPERVALUEENDTAG', # </upperValue>
    'UMLMODELTAG', # <uml:Model
    'UMLMODELENDTAG', # </uml:Model>
    'DETAILSTAG', # <details
    'XMLSTARTTAG', # <?xml
    'XMLENDTAG', # ?>
    'VERSION', #version=""
    'ENCODING' # encoding=""
)

t_RWICKETEND = r'/>'
t_RWICKET = r'>'
t_EANNOTATIONSTAG = r'<eAnnotations'
t_EANNOTATIONSENDTAG = r'</eAnnotations>'
t_PACKAGEIMPORTTAG = r'<packageImport'
t_PACKAGEIMPORTENDTAG = r'</packageImport>'
t_IMPORTEDPACKAGETAG = r'<importedPackage'
#t_IMPORTEDPACKAGEENDTAG = r'</importedPackage>'
t_PACKAGEDELEMENTTAG = r'<packagedElement'
t_PACKAGEDELEMENTENDTAG = r'</packagedElement>'
t_OWNEDATTRIBUTETAG = r'<ownedAttribute'
t_OWNEDATTRIBUTEENDTAG = r'</ownedAttribute>'
t_TYPETAG = r'<type'
#t_TYPETAGENDTAG = r'</type>'
t_OWNEDENDTAG = r'<ownedEnd'
t_OWNEDENDENDTAG = r'</ownedEnd>'
t_LOWERVALUETAG = r'<lowerValue'
t_LOWERVALUEENDTAG = r'</lowerValue>'
t_UPPERVALUETAG = r'<upperValue'
t_UPPERVALUEENDTAG = r'</upperValue>'
t_UMLMODELTAG = r'<uml:Model'
t_UMLMODELENDTAG = r'</uml:Model>'
t_DETAILSTAG = r'<details'
t_XMLSTARTTAG = r'<\?xml'
t_XMLENDTAG = r'\?>'

def t_XMIID(t):
    r'xmi:id="[^"]+"'
    t.value = t.value[8:-1]
    return t

def t_XMIVERSION(t):
    r'xmi:version="[^"]+"'
    t.value = t.value[13:-1]
    return t

def t_XMLNSXMI(t):
    r'xmlns:xmi="[^"]+"'
    t.value = t.value[11:-1]
    return t

def t_XMLNSXSI(t):
    r'xmlns:xsi="[^"]+"'
    t.value = t.value[11:-1]
    return t

def t_XMLNSUML(t):
    r'xmlns:uml="[^"]+"'
    t.value = t.value[11:-1]
    return t

def t_NAME(t):
    r'name="[^"]+"'
    t.value = t.value[6:-1]
    return t

def t_SOURCE(t):
    r'source="[^"]+"'
    t.value = t.value[8:-1]
    return t

def t_KEY(t):
    r'key="[^"]+"'
    t.value = t.value[5:-1]
    return t

def t_VALUE(t):
    r'value="[^"]+"'
    t.value = t.value[7:-1]
    return t

def t_XSITYPE(t):
    r'xsi:type="[^"]+"'
    t.value = t.value[10:-1]
    return t

def t_DETAILS(t):
    r'details="[^"]+"'
    t.value = t.value[9:-1]
    return t

def t_VISIBILITY(t):
    r'visibility="[^"]+"'
    t.value = t.value[12:-1]
    return t

def t_TYPE(t):
    r'type="[^"]+"'
    t.value = t.value[6:-1]
    return t

def t_HREF(t):
    r'href="[^"]+"'
    t.value = t.value[6:-1]
    return t

def t_MEMBEREND(t):
    r'memberEnd="[^"]+"'
    t.value = t.value[11:-1]
    return t

def t_NAVIGABLEOWNEDEND(t):
    r'navigableOwnedEnd="[^"]+"'
    t.value = t.value[19:-1]
    return t

def t_ASSOCIATION(t):
    r'association="[^"]+"'
    t.value = t.value[13:-1]
    return t

def t_VERSION(t):
    r'version="[^"]+"'
    t.value = t.value[9:-1]
    return t

def t_ENCODING(t):
    r'encoding="[^"]+"'
    t.value = t.value[10:-1]
    return t

#Count and ignore new lines
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    
#Ignore spaces and tabs
t_ignore  = ' \t'

#Error handling
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
