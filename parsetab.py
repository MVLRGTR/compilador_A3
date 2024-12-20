
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftOP_SOMAOP_SUBleftOP_MULTOP_DIVENQUANTO IMPRIMIR INTEIRO LBRACE LEIA LPAREN MAIOR MAIORIGUAL MENOR MENORIGUAL NUMERO OP_DIFERENTE OP_DIV OP_IGUAL OP_IGUALDADE OP_MULT OP_PONTO OP_PONTO_VIRGULA OP_SOMA OP_SUB OP_VIRGULA PARA RBRACE REAL RPAREN SE SENAO TEXTO TEXTONORMAL VARIAVELprogram : statement_listvariavel : VARIAVELliteral : NUMERO\n               | VARIAVEL\n               | TEXTONORMALstatement_list : statement_list statement\n                      | statementstatement : INTEIRO VARIAVEL\n                 | REAL VARIAVEL\n                 | TEXTO VARIAVELstatement : INTEIRO VARIAVEL OP_IGUAL expression\n                 | REAL VARIAVEL OP_IGUAL expression\n                 | TEXTO VARIAVEL OP_IGUAL expressionstatement : VARIAVEL OP_IGUAL expressionexpression : expression OP_SOMA expression\n                  | expression OP_SUB expression\n                  | expression OP_MULT expression\n                  | expression OP_DIV expressionexpression : expression MAIOR expression\n                  | expression MENOR expression\n                  | expression MAIORIGUAL expression\n                  | expression MENORIGUAL expression\n                  | expression OP_IGUALDADE expression\n                  | expression OP_DIFERENTE expressionexpression : LPAREN expression RPARENexpression : NUMERO\n                  | VARIAVELstatement : SE LPAREN expression RPAREN LBRACE statement RBRACE SENAO LBRACE statement RBRACE\n                 | SE LPAREN expression RPAREN LBRACE statement RBRACEstatement : ENQUANTO LPAREN expression RPAREN LBRACE statement RBRACEstatement : PARA LPAREN expression OP_PONTO_VIRGULA expression OP_PONTO_VIRGULA expression RPAREN LBRACE statement RBRACEstatement : IMPRIMIR LPAREN literal RPARENstatement : LEIA variavel'
    
_lr_action_items = {'INTEIRO':([0,2,3,13,14,16,17,22,23,25,26,28,38,50,51,55,56,57,58,59,60,61,62,63,64,65,66,67,68,73,74,78,79,82,83,],[4,4,-7,-6,-8,-9,-10,-33,-2,-27,-14,-26,-11,-12,-13,-32,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,4,4,-29,-30,4,4,-28,-31,]),'REAL':([0,2,3,13,14,16,17,22,23,25,26,28,38,50,51,55,56,57,58,59,60,61,62,63,64,65,66,67,68,73,74,78,79,82,83,],[6,6,-7,-6,-8,-9,-10,-33,-2,-27,-14,-26,-11,-12,-13,-32,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,6,6,-29,-30,6,6,-28,-31,]),'TEXTO':([0,2,3,13,14,16,17,22,23,25,26,28,38,50,51,55,56,57,58,59,60,61,62,63,64,65,66,67,68,73,74,78,79,82,83,],[7,7,-7,-6,-8,-9,-10,-33,-2,-27,-14,-26,-11,-12,-13,-32,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,7,7,-29,-30,7,7,-28,-31,]),'VARIAVEL':([0,2,3,4,6,7,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,38,39,40,41,42,43,44,45,46,47,48,50,51,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,72,73,74,78,79,82,83,],[5,5,-7,14,16,17,23,-6,-8,25,-9,-10,25,25,25,36,-33,-2,25,-27,-14,25,-26,25,25,-11,25,25,25,25,25,25,25,25,25,25,-12,-13,25,-32,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,5,5,25,-29,-30,5,5,-28,-31,]),'SE':([0,2,3,13,14,16,17,22,23,25,26,28,38,50,51,55,56,57,58,59,60,61,62,63,64,65,66,67,68,73,74,78,79,82,83,],[8,8,-7,-6,-8,-9,-10,-33,-2,-27,-14,-26,-11,-12,-13,-32,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,8,8,-29,-30,8,8,-28,-31,]),'ENQUANTO':([0,2,3,13,14,16,17,22,23,25,26,28,38,50,51,55,56,57,58,59,60,61,62,63,64,65,66,67,68,73,74,78,79,82,83,],[9,9,-7,-6,-8,-9,-10,-33,-2,-27,-14,-26,-11,-12,-13,-32,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,9,9,-29,-30,9,9,-28,-31,]),'PARA':([0,2,3,13,14,16,17,22,23,25,26,28,38,50,51,55,56,57,58,59,60,61,62,63,64,65,66,67,68,73,74,78,79,82,83,],[10,10,-7,-6,-8,-9,-10,-33,-2,-27,-14,-26,-11,-12,-13,-32,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,10,10,-29,-30,10,10,-28,-31,]),'IMPRIMIR':([0,2,3,13,14,16,17,22,23,25,26,28,38,50,51,55,56,57,58,59,60,61,62,63,64,65,66,67,68,73,74,78,79,82,83,],[11,11,-7,-6,-8,-9,-10,-33,-2,-27,-14,-26,-11,-12,-13,-32,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,11,11,-29,-30,11,11,-28,-31,]),'LEIA':([0,2,3,13,14,16,17,22,23,25,26,28,38,50,51,55,56,57,58,59,60,61,62,63,64,65,66,67,68,73,74,78,79,82,83,],[12,12,-7,-6,-8,-9,-10,-33,-2,-27,-14,-26,-11,-12,-13,-32,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,12,12,-29,-30,12,12,-28,-31,]),'$end':([1,2,3,13,14,16,17,22,23,25,26,28,38,50,51,55,56,57,58,59,60,61,62,63,64,65,66,73,74,82,83,],[0,-1,-7,-6,-8,-9,-10,-33,-2,-27,-14,-26,-11,-12,-13,-32,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-29,-30,-28,-31,]),'OP_IGUAL':([5,14,16,17,],[15,24,29,30,]),'LPAREN':([8,9,10,11,15,18,19,20,24,27,29,30,39,40,41,42,43,44,45,46,47,48,54,72,],[18,19,20,21,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,]),'RBRACE':([14,16,17,22,23,25,26,28,38,50,51,55,56,57,58,59,60,61,62,63,64,65,66,70,71,73,74,80,81,82,83,],[-8,-9,-10,-33,-2,-27,-14,-26,-11,-12,-13,-32,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,73,74,-29,-30,82,83,-28,-31,]),'NUMERO':([15,18,19,20,21,24,27,29,30,39,40,41,42,43,44,45,46,47,48,54,72,],[28,28,28,28,35,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,]),'TEXTONORMAL':([21,],[37,]),'OP_SOMA':([25,26,28,31,32,33,38,49,50,51,56,57,58,59,60,61,62,63,64,65,66,69,75,],[-27,39,-26,39,39,39,39,39,39,39,-15,-16,-17,-18,39,39,39,39,39,39,-25,39,39,]),'OP_SUB':([25,26,28,31,32,33,38,49,50,51,56,57,58,59,60,61,62,63,64,65,66,69,75,],[-27,40,-26,40,40,40,40,40,40,40,-15,-16,-17,-18,40,40,40,40,40,40,-25,40,40,]),'OP_MULT':([25,26,28,31,32,33,38,49,50,51,56,57,58,59,60,61,62,63,64,65,66,69,75,],[-27,41,-26,41,41,41,41,41,41,41,41,41,-17,-18,41,41,41,41,41,41,-25,41,41,]),'OP_DIV':([25,26,28,31,32,33,38,49,50,51,56,57,58,59,60,61,62,63,64,65,66,69,75,],[-27,42,-26,42,42,42,42,42,42,42,42,42,-17,-18,42,42,42,42,42,42,-25,42,42,]),'MAIOR':([25,26,28,31,32,33,38,49,50,51,56,57,58,59,60,61,62,63,64,65,66,69,75,],[-27,43,-26,43,43,43,43,43,43,43,-15,-16,-17,-18,43,43,43,43,43,43,-25,43,43,]),'MENOR':([25,26,28,31,32,33,38,49,50,51,56,57,58,59,60,61,62,63,64,65,66,69,75,],[-27,44,-26,44,44,44,44,44,44,44,-15,-16,-17,-18,44,44,44,44,44,44,-25,44,44,]),'MAIORIGUAL':([25,26,28,31,32,33,38,49,50,51,56,57,58,59,60,61,62,63,64,65,66,69,75,],[-27,45,-26,45,45,45,45,45,45,45,-15,-16,-17,-18,45,45,45,45,45,45,-25,45,45,]),'MENORIGUAL':([25,26,28,31,32,33,38,49,50,51,56,57,58,59,60,61,62,63,64,65,66,69,75,],[-27,46,-26,46,46,46,46,46,46,46,-15,-16,-17,-18,46,46,46,46,46,46,-25,46,46,]),'OP_IGUALDADE':([25,26,28,31,32,33,38,49,50,51,56,57,58,59,60,61,62,63,64,65,66,69,75,],[-27,47,-26,47,47,47,47,47,47,47,-15,-16,-17,-18,47,47,47,47,47,47,-25,47,47,]),'OP_DIFERENTE':([25,26,28,31,32,33,38,49,50,51,56,57,58,59,60,61,62,63,64,65,66,69,75,],[-27,48,-26,48,48,48,48,48,48,48,-15,-16,-17,-18,48,48,48,48,48,48,-25,48,48,]),'RPAREN':([25,28,31,32,34,35,36,37,49,56,57,58,59,60,61,62,63,64,65,66,75,],[-27,-26,52,53,55,-3,-4,-5,66,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,77,]),'OP_PONTO_VIRGULA':([25,28,33,56,57,58,59,60,61,62,63,64,65,66,69,],[-27,-26,54,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,72,]),'LBRACE':([52,53,76,77,],[67,68,78,79,]),'SENAO':([73,],[76,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'statement_list':([0,],[2,]),'statement':([0,2,67,68,78,79,],[3,13,70,71,80,81,]),'variavel':([12,],[22,]),'expression':([15,18,19,20,24,27,29,30,39,40,41,42,43,44,45,46,47,48,54,72,],[26,31,32,33,38,49,50,51,56,57,58,59,60,61,62,63,64,65,69,75,]),'literal':([21,],[34,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> statement_list','program',1,'p_program','grammar.py',14),
  ('variavel -> VARIAVEL','variavel',1,'p_variavel','grammar.py',18),
  ('literal -> NUMERO','literal',1,'p_literal','grammar.py',22),
  ('literal -> VARIAVEL','literal',1,'p_literal','grammar.py',23),
  ('literal -> TEXTONORMAL','literal',1,'p_literal','grammar.py',24),
  ('statement_list -> statement_list statement','statement_list',2,'p_statement_list','grammar.py',28),
  ('statement_list -> statement','statement_list',1,'p_statement_list','grammar.py',29),
  ('statement -> INTEIRO VARIAVEL','statement',2,'p_define_tipo','grammar.py',33),
  ('statement -> REAL VARIAVEL','statement',2,'p_define_tipo','grammar.py',34),
  ('statement -> TEXTO VARIAVEL','statement',2,'p_define_tipo','grammar.py',35),
  ('statement -> INTEIRO VARIAVEL OP_IGUAL expression','statement',4,'p_define_tipo_com_atribuicao','grammar.py',45),
  ('statement -> REAL VARIAVEL OP_IGUAL expression','statement',4,'p_define_tipo_com_atribuicao','grammar.py',46),
  ('statement -> TEXTO VARIAVEL OP_IGUAL expression','statement',4,'p_define_tipo_com_atribuicao','grammar.py',47),
  ('statement -> VARIAVEL OP_IGUAL expression','statement',3,'p_statement_atribuicao','grammar.py',78),
  ('expression -> expression OP_SOMA expression','expression',3,'p_expression_arit','grammar.py',107),
  ('expression -> expression OP_SUB expression','expression',3,'p_expression_arit','grammar.py',108),
  ('expression -> expression OP_MULT expression','expression',3,'p_expression_arit','grammar.py',109),
  ('expression -> expression OP_DIV expression','expression',3,'p_expression_arit','grammar.py',110),
  ('expression -> expression MAIOR expression','expression',3,'p_expression_rel','grammar.py',115),
  ('expression -> expression MENOR expression','expression',3,'p_expression_rel','grammar.py',116),
  ('expression -> expression MAIORIGUAL expression','expression',3,'p_expression_rel','grammar.py',117),
  ('expression -> expression MENORIGUAL expression','expression',3,'p_expression_rel','grammar.py',118),
  ('expression -> expression OP_IGUALDADE expression','expression',3,'p_expression_rel','grammar.py',119),
  ('expression -> expression OP_DIFERENTE expression','expression',3,'p_expression_rel','grammar.py',120),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression','grammar.py',124),
  ('expression -> NUMERO','expression',1,'p_expression_var','grammar.py',128),
  ('expression -> VARIAVEL','expression',1,'p_expression_var','grammar.py',129),
  ('statement -> SE LPAREN expression RPAREN LBRACE statement RBRACE SENAO LBRACE statement RBRACE','statement',11,'p_statement_se','grammar.py',144),
  ('statement -> SE LPAREN expression RPAREN LBRACE statement RBRACE','statement',7,'p_statement_se','grammar.py',145),
  ('statement -> ENQUANTO LPAREN expression RPAREN LBRACE statement RBRACE','statement',7,'p_statement_enquanto','grammar.py',149),
  ('statement -> PARA LPAREN expression OP_PONTO_VIRGULA expression OP_PONTO_VIRGULA expression RPAREN LBRACE statement RBRACE','statement',11,'p_statement_para','grammar.py',153),
  ('statement -> IMPRIMIR LPAREN literal RPAREN','statement',4,'p_statement_imprimir','grammar.py',157),
  ('statement -> LEIA variavel','statement',2,'p_statement_leia','grammar.py',161),
]
