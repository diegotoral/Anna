# Anna Specification


## Introdução ##

Este é o manual de referência para a linguagem de programação Anna.

Anna é uma linugagem de propósito geral, projetada para ser simples de escrever, de aprender e para rodar rápido. Anna é inspirada em Python, Ruby e C, três linguagens incríveis e poderosas.

## Notação ##

A sintaxe é especificada usando uma notação modificada da [Extended Backus-Naur Form](http://en.wikipedia.org/wiki/Extended_Backus%E2%80%93Naur_Form) (EBNF) e usa o estilo seguinte para as definições:

    name   = letter ( letter | digit | "_" )*
    letter = "a" | "e" | "i" | "o" | "u"
    digit  = "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9"

Na primeira linha do exemplo, temos que `name` é um `letter` seguido por uma sequência de zero ou mais `letter`, `digit` ou ainda do caractere `_`. Por sua vez, um `letter` pode se tornar um dos caracteres a, e, i, o ou u. De maneira análoga, `digit` pode assumir os valores numéricos de 0 até 9.

Cada regra inicia com um nome, o qual é seguido pelo simbolo `=`. Uma barra vertial (`|`) é usada para separar alternativas. A estrela (`*`) significa zero ou mais repetições do item precedente. De maneira análoga, o símbolo plus (`+`) denota uma ou mais repetições do item ao qual se refere. Qualquer valor entre colchetes (`[ ]`) é considerado opcional, significando que zero ou uma ocorrências do item podem aparecer. Parenteses são usados para agrupar, enquanto strings literais estão contidas entre aspas (`"`).


## Elementos léxicos ##

### Estrutura de linha ###

Um programa é dividido em uma série de `linhas lógicas`.


#### Linhas lógicas ####

O fim de uma linha lógica é representado pelo token `newline`. Uma linha lógica é formada de uma ou mais `linhas físicas`.

    newline = '\n'


#### Linhas físicas ####

Linhas físicas são sequências de caracteres terminados por um marcador de fim de linha.


#### União de linhas ####

Duas ou mais `linhas físicas` podem ser unidas em `linhas lógicas` utilizando o caractere `\`, como no exemplo:

```
if foo == 123 and bar == 321 \
   and foo_bar == 231:
    return 1
```


### Comentários ###

Existe apenas uma forma de comentário, o comentário de uma linha, iniciado pelo caractere # e que termina ao fim da linha. Qualquer comentário atua como uma nova linha.


### Letras e Dígitos ###

O caractere _ é considerado uma letra.

    decimal_digit = "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9"
    octal_digit   = "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7"
    hex_digit     = "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" | "A" | "B" | "C"
                    | "D" | "E" | "F" | "a" | "b" | "c" | "d" | "e" | "f"
    letter        = "A" | "B" | "C" | "D" | "E" | "F" | "G" | "H" | "I" | "J" | "K" | "L" | "M"
                    | "N" | "O" | "P" | "Q" | "R" | "S" | "T" | "U" | "V" | "W" | "X" | "Y" | "Z"
                    | "a" | "b" | "c" | "d" | "e" | "f" | "g" | "h" | "i" | "j" | "k" | "l" | "m"
                    | "n" | "o" | "p" | "q" | "r" | "s" | "t" | "u" | "v" | "w" | "x" | "y" | "z" | "_"


### Identificadores ###

Identificadores nomeam entidades de um programa, tais como variáveis e tipos. Um identificador é uma sequência de uma ou mais letras e dígitos. O primeiro caratere de um identificador deve, obrigatoriamente, ser uma letra.

    identifier = letter ( letter | decimal_digit )*


### Palavras reservadas (Keywords) ###

As palavras seguintes são reservadas para a linguagem e não podem ser usadas como identificadores.

    return      else      pass      for      try
    if          loop      exit      del      until
    class       or        and       in       not
    true        false     null      elif


### Operadores e Delimitadores ###

As sequências de caracteres seguinte representam operadores, delimitadores e outros tokens da linguagem:

    +      -      +=      -=      *
    /      *=      /=     (       )
    [      ]      ,       %


### Literais inteiros ###

Um literal inteiro é uma sequência de dígitos representando uma contante inteira. Um prefixo opicional define a base do literal: 0 para octal e 0x ou 0X para hexadecimal. Literais hexadecimais suportam as letras a-f e A-F para representar valores de 10 à 15.

    int_literal     = decimal_literal | octal_literal | hex_literal
    decimal_literal = ( "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" ) ( decimal_digit )*
    octal_literal   = "0" ( octal_digit )*
    hex_literal     = "0" ( "x" | "X" ) hex_digit ( hex_digit )*


### Literais ponto flutuante ###

Literal ponto flutuante é uma sequência de dígitos representando uma constante de ponto flutuante. Possui uma parte inteira, um ponto decimal, e outra parte fracionária. Tanto a parte inteira quanto a fracionária, são compostas de dígitos decimais.

    float_literal = decimals "." [decimals] | "." decimals
    decimals      = decimal_digit ( decimal_digit )*

*Todo* Expoentes


### Literais strings ###

Literais strgins são sequências de caracteres representando uma constante string.

    string_literal        = single_quoted_literal | double_quoted_literal
    single_quoted_literal = "'" {} "'"
    double_quoted_literal = '"' {} '"'


### Constantes ###

Existem constantes de diferentes tipos, constantes booleanas, constantes inteiras, constantes de ponto flutuante e constantes string.


### Tipos ###

Um tipo determina um conjunto de valores e operações específicas para valores daquele tipo.


#### Tipos booleano ####


#### Tipos numéricos ####


#### Tipos string ####


#### Tipos array ####


#### Tipos funções ####


### Blocos ###


### Declarações e escopo ###


### Expressões ###
