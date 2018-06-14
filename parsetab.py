
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.2'

_lr_method = 'LALR'

_lr_signature = '\xa8G\x95\xb9R\xb6\x1f\xed\xc4|\xf4F"\x1b\xee2'
    
_lr_action_items = {'RWICKET':([14,22,25,38,48,59,63,64,81,92,96,97,101,],[15,26,30,42,54,62,69,70,84,95,99,100,105,]),'XMLENDTAG':([7,],[9,]),'UMLMODELENDTAG':([23,28,51,56,65,],[27,-15,-13,-12,-14,]),'ENCODING':([4,],[7,]),'XMLNSUML':([11,],[12,]),'VISIBILITY':([59,],[63,]),'LOWERVALUEENDTAG':([19,36,98,103,],[-9,-8,102,107,]),'HREF':([40,78,],[45,82,]),'OWNEDENDENDTAG':([91,106,108,110,],[94,-20,-18,-19,]),'OWNEDATTRIBUTEENDTAG':([19,36,72,75,79,85,],[-9,-8,77,80,83,-1,]),'XSITYPE':([24,73,87,90,],[29,78,89,93,]),'IMPORTEDPACKAGETAG':([19,34,36,],[-9,40,-8,]),'PACKAGEDELEMENTENDTAG':([19,36,47,53,57,60,66,77,80,83,94,],[-9,-8,51,56,-5,65,-22,-3,-4,-2,-21,]),'SOURCE':([18,],[22,]),'RWICKETEND':([45,46,82,101,],[49,50,85,106,]),'UPPERVALUEENDTAG':([19,36,104,109,],[-9,-8,108,110,]),'MEMBEREND':([38,],[43,]),'ASSOCIATION':([76,],[81,]),'$end':([1,5,27,],[0,-25,-24,]),'OWNEDATTRIBUTETAG':([19,36,47,53,57,77,80,83,],[-9,-8,52,52,52,-3,-4,-2,]),'PACKAGEDELEMENTTAG':([20,23,28,44,51,56,65,],[24,24,24,-11,-13,-12,-14,]),'EANNOTATIONSTAG':([15,17,19,30,34,36,42,47,54,58,62,68,69,70,74,75,84,86,95,98,99,100,103,104,105,109,],[16,16,16,16,16,-8,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,]),'UPPERVALUETAG':([88,102,107,],[90,-16,-17,]),'VALUE':([41,92,97,],[46,96,101,]),'XMIID':([12,16,21,29,31,52,61,89,93,],[13,18,25,33,35,55,67,92,97,]),'DETAILSTAG':([26,32,37,50,],[31,31,31,-6,]),'VERSION':([2,],[4,]),'UMLMODELTAG':([3,9,],[6,-23,]),'TYPETAG':([19,36,68,74,],[-9,-8,73,73,]),'NAVIGABLEOWNEDEND':([43,],[48,]),'NAME':([13,33,55,67,],[14,38,59,71,]),'XMLNSXSI':([10,],[11,]),'XMLSTARTTAG':([0,],[2,]),'OWNEDENDTAG':([19,36,58,60,66,94,],[-9,-8,61,61,61,-21,]),'LOWERVALUETAG':([19,36,86,],[-9,-8,87,]),'EANNOTATIONSENDTAG':([32,37,50,],[36,-7,-6,]),'XMIVERSION':([6,],[8,]),'KEY':([35,],[41,]),'XMLNSXMI':([8,],[10,]),'PACKAGEIMPORTTAG':([17,19,36,],[21,-9,-8,]),'TYPE':([59,71,],[64,76,]),'PACKAGEIMPORTENDTAG':([39,49,],[44,-10,]),}

_lr_action = { }
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = { }
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'xmidoc':([0,],[1,]),'packagedelement':([20,23,28,],[23,28,28,]),'eannotation':([15,17,19,30,34,42,47,54,58,62,68,69,70,74,75,84,86,95,98,99,100,103,104,105,109,],[17,19,19,34,19,47,19,58,19,68,19,74,75,19,19,86,19,98,19,103,104,19,19,109,19,]),'ownedend':([58,60,66,],[60,66,66,]),'importedpackage':([34,],[39,]),'uppervalue':([88,],[91,]),'umlmodel':([3,],[5,]),'packageimport':([17,],[20,]),'xmldata':([0,],[3,]),'attributetype':([68,74,],[72,79,]),'classattribute':([47,53,57,],[53,57,57,]),'lowervalue':([86,],[88,]),'eannotationdetail':([26,32,37,],[32,37,37,]),}

_lr_goto = { }
for _k, _v in _lr_goto_items.items():
   for _x,_y in zip(_v[0],_v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = { }
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> xmidoc","S'",1,None,None,None),
  ('attributetype -> TYPETAG XSITYPE HREF RWICKETEND','attributetype',4,'p_attributetype','/mnt/e/Python/s18dbfinalproject-neveling-lee-west/XMI-DDL/yacc.py',5),
  ('classattribute -> OWNEDATTRIBUTETAG XMIID NAME VISIBILITY RWICKET eannotation attributetype OWNEDATTRIBUTEENDTAG','classattribute',8,'p_classattribute','/mnt/e/Python/s18dbfinalproject-neveling-lee-west/XMI-DDL/yacc.py',11),
  ('classattribute -> OWNEDATTRIBUTETAG XMIID NAME RWICKET eannotation attributetype OWNEDATTRIBUTEENDTAG','classattribute',7,'p_classattribute','/mnt/e/Python/s18dbfinalproject-neveling-lee-west/XMI-DDL/yacc.py',12),
  ('classattribute -> OWNEDATTRIBUTETAG XMIID NAME TYPE RWICKET eannotation OWNEDATTRIBUTEENDTAG','classattribute',7,'p_classattribute','/mnt/e/Python/s18dbfinalproject-neveling-lee-west/XMI-DDL/yacc.py',13),
  ('classattribute -> classattribute classattribute','classattribute',2,'p_classattribute','/mnt/e/Python/s18dbfinalproject-neveling-lee-west/XMI-DDL/yacc.py',14),
  ('eannotationdetail -> DETAILSTAG XMIID KEY VALUE RWICKETEND','eannotationdetail',5,'p_eannotationdetail','/mnt/e/Python/s18dbfinalproject-neveling-lee-west/XMI-DDL/yacc.py',20),
  ('eannotationdetail -> eannotationdetail eannotationdetail','eannotationdetail',2,'p_eannotationdetail','/mnt/e/Python/s18dbfinalproject-neveling-lee-west/XMI-DDL/yacc.py',21),
  ('eannotation -> EANNOTATIONSTAG XMIID SOURCE RWICKET eannotationdetail EANNOTATIONSENDTAG','eannotation',6,'p_eannotation','/mnt/e/Python/s18dbfinalproject-neveling-lee-west/XMI-DDL/yacc.py',28),
  ('eannotation -> eannotation eannotation','eannotation',2,'p_eannotation','/mnt/e/Python/s18dbfinalproject-neveling-lee-west/XMI-DDL/yacc.py',29),
  ('importedpackage -> IMPORTEDPACKAGETAG HREF RWICKETEND','importedpackage',3,'p_importedpackage','/mnt/e/Python/s18dbfinalproject-neveling-lee-west/XMI-DDL/yacc.py',34),
  ('packageimport -> PACKAGEIMPORTTAG XMIID RWICKET eannotation importedpackage PACKAGEIMPORTENDTAG','packageimport',6,'p_packageimport','/mnt/e/Python/s18dbfinalproject-neveling-lee-west/XMI-DDL/yacc.py',38),
  ('packagedelement -> PACKAGEDELEMENTTAG XSITYPE XMIID NAME RWICKET eannotation classattribute PACKAGEDELEMENTENDTAG','packagedelement',8,'p_packagedelement','/mnt/e/Python/s18dbfinalproject-neveling-lee-west/XMI-DDL/yacc.py',43),
  ('packagedelement -> PACKAGEDELEMENTTAG XSITYPE XMIID NAME RWICKET eannotation PACKAGEDELEMENTENDTAG','packagedelement',7,'p_packagedelement','/mnt/e/Python/s18dbfinalproject-neveling-lee-west/XMI-DDL/yacc.py',44),
  ('packagedelement -> PACKAGEDELEMENTTAG XSITYPE XMIID NAME MEMBEREND NAVIGABLEOWNEDEND RWICKET eannotation ownedend PACKAGEDELEMENTENDTAG','packagedelement',10,'p_packagedelement','/mnt/e/Python/s18dbfinalproject-neveling-lee-west/XMI-DDL/yacc.py',45),
  ('packagedelement -> packagedelement packagedelement','packagedelement',2,'p_packagedelement','/mnt/e/Python/s18dbfinalproject-neveling-lee-west/XMI-DDL/yacc.py',46),
  ('lowervalue -> LOWERVALUETAG XSITYPE XMIID RWICKET eannotation LOWERVALUEENDTAG','lowervalue',6,'p_lowervalue','/mnt/e/Python/s18dbfinalproject-neveling-lee-west/XMI-DDL/yacc.py',63),
  ('lowervalue -> LOWERVALUETAG XSITYPE XMIID VALUE RWICKET eannotation LOWERVALUEENDTAG','lowervalue',7,'p_lowervalue','/mnt/e/Python/s18dbfinalproject-neveling-lee-west/XMI-DDL/yacc.py',64),
  ('uppervalue -> UPPERVALUETAG XSITYPE XMIID RWICKET eannotation UPPERVALUEENDTAG','uppervalue',6,'p_uppervalue','/mnt/e/Python/s18dbfinalproject-neveling-lee-west/XMI-DDL/yacc.py',73),
  ('uppervalue -> UPPERVALUETAG XSITYPE XMIID VALUE RWICKET eannotation UPPERVALUEENDTAG','uppervalue',7,'p_uppervalue','/mnt/e/Python/s18dbfinalproject-neveling-lee-west/XMI-DDL/yacc.py',74),
  ('uppervalue -> UPPERVALUETAG XSITYPE XMIID VALUE RWICKETEND','uppervalue',5,'p_uppervalue','/mnt/e/Python/s18dbfinalproject-neveling-lee-west/XMI-DDL/yacc.py',75),
  ('ownedend -> OWNEDENDTAG XMIID NAME TYPE ASSOCIATION RWICKET eannotation lowervalue uppervalue OWNEDENDENDTAG','ownedend',10,'p_ownedend','/mnt/e/Python/s18dbfinalproject-neveling-lee-west/XMI-DDL/yacc.py',84),
  ('ownedend -> ownedend ownedend','ownedend',2,'p_ownedend','/mnt/e/Python/s18dbfinalproject-neveling-lee-west/XMI-DDL/yacc.py',85),
  ('xmldata -> XMLSTARTTAG VERSION ENCODING XMLENDTAG','xmldata',4,'p_xmldata','/mnt/e/Python/s18dbfinalproject-neveling-lee-west/XMI-DDL/yacc.py',93),
  ('umlmodel -> UMLMODELTAG XMIVERSION XMLNSXMI XMLNSXSI XMLNSUML XMIID NAME RWICKET eannotation packageimport packagedelement UMLMODELENDTAG','umlmodel',12,'p_umlmodel','/mnt/e/Python/s18dbfinalproject-neveling-lee-west/XMI-DDL/yacc.py',97),
  ('xmidoc -> xmldata umlmodel','xmidoc',2,'p_xmidoc','/mnt/e/Python/s18dbfinalproject-neveling-lee-west/XMI-DDL/yacc.py',101),
]