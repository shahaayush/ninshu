
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.8'

_lr_method = 'LALR'

_lr_signature = '5E72EFA06628140E0F84FC4A1E2295DC'
    
_lr_action_items = {'ID':([0,7,8,9,10,11,12,],[2,13,13,13,13,13,13,]),'NUMBER':([0,7,8,9,10,11,12,],[4,4,4,4,4,4,4,]),'DIV':([2,4,5,13,14,15,16,17,18,19,],[-11,-10,9,-11,-9,9,-8,-7,9,9,]),'EQ':([2,],[8,]),'$end':([1,2,3,4,5,6,13,14,15,16,17,18,19,],[-1,-11,0,-10,-4,-2,-11,-9,-3,-8,-7,-5,-6,]),'PLUS':([2,4,5,13,14,15,16,17,18,19,],[-11,-10,11,-11,-9,11,-8,-7,-5,-6,]),'MINUS':([0,2,4,5,7,8,9,10,11,12,13,14,15,16,17,18,19,],[7,-11,-10,12,7,7,7,7,7,7,-11,-9,12,-8,-7,-5,-6,]),'MULT':([2,4,5,13,14,15,16,17,18,19,],[-11,-10,10,-11,-9,10,-8,-7,10,10,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'move':([0,],[1,]),'combo_move':([0,],[3,]),'hand_sign':([0,],[6,]),'expression':([0,7,8,9,10,11,12,],[5,14,15,16,17,18,19,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> combo_move","S'",1,None,None,None),
  ('combo_move -> move','combo_move',1,'p_combo_move','parser.py',24),
  ('move -> hand_sign','move',1,'p_move','parser.py',30),
  ('hand_sign -> ID EQ expression','hand_sign',3,'p_hand_sign','parser.py',36),
  ('hand_sign -> expression','hand_sign',1,'p_hand_sign','parser.py',37),
  ('expression -> expression PLUS expression','expression',3,'p_expression_binop','parser.py',46),
  ('expression -> expression MINUS expression','expression',3,'p_expression_binop','parser.py',47),
  ('expression -> expression MULT expression','expression',3,'p_expression_binop','parser.py',48),
  ('expression -> expression DIV expression','expression',3,'p_expression_binop','parser.py',49),
  ('expression -> MINUS expression','expression',2,'p_expression_UMINUS','parser.py',62),
  ('expression -> NUMBER','expression',1,'p_expression_variable','parser.py',67),
  ('expression -> ID','expression',1,'p_expression_ID','parser.py',73),
]
