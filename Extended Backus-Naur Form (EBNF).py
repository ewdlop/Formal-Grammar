ebnf_grammar = """
(* EBNF Grammar for Simple Arithmetic Expressions *)

expression = term, { ("+" | "-"), term } ;
term       = factor, { ("*" | "/"), factor } ;
factor     = number | "(", expression, ")" ;
number     = digit, { digit } ;
digit      = "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" ;
"""

print(ebnf_grammar)
