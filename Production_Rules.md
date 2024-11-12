Production Rules

<query> ::= <select-query> | <insert-query> | <update-query> | <delete-query>

<select-query> ::= "SELECT" <columns> "FROM" <table> [ "WHERE" <condition> ]
<columns> ::= "*" | <column> | <column> "," <columns>
<column> ::= <identifier>
<table> ::= <identifier>
<condition> ::= <expression> <operator> <value>
<expression> ::= <identifier>
<operator> ::= "=" | "!=" | ">" | "<" | ">=" | "<="
<value> ::= <number> | <string>

<insert-query> ::= "INSERT INTO" <table> "(" <columns> ")" "VALUES" "(" <values> ")"
<values> ::= <value> | <value> "," <values>

<update-query> ::= "UPDATE" <table> "SET" <assignments> [ "WHERE" <condition> ]
<assignments> ::= <column> "=" <value> | <column> "=" <value> "," <assignments>

<delete-query> ::= "DELETE FROM" <table> [ "WHERE" <condition> ]

<identifier> ::= any sequence of alphanumeric characters
<number> ::= any numeric value
<string> ::= any quoted string
