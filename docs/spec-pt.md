# Anna Specification


## Introdução ##

Este é o manual de referência para a linguagem de programação Anna.

Anna é uma linugagem de propósito geral, projetada para ser simples de escrever, de aprender e para rodar rápido. Anna é inspirada em Python, Ruby e C, três linguagens incríveis e poderosas.

## Notação ##

A sintaxe é especificada usando a Extended Backus-Naur Form (EBNF):

    *TODO* Adicionar notação EBNF usada


## Elementos léxicos ##

### Caracteres ###

    newline = '\n'

### Letras e Dígitos ###

O caractere _ é considerado uma letra.

    decimal_digit = "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9"
    octal_digit = "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7"
    hex_digit = "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" | "A" | "B"
                | "C" | "D" | "E" | "F" | "a" | "b" | "c" | "d" | "e" | "f"
    letter = "A" | "B" | "C" | "D" | "E" | "F" | "G" | "H" | "I" | "J" | "K" | "L" | "M"
             | "N" | "O" | "P" | "Q" | "R" | "S" | "T" | "U" | "V" | "W" | "X" | "Y" | "Z"
             | "a" | "b" | "c" | "d" | "e" | "f" | "g" | "h" | "i" | "j" | "k" | "l" | "m"
             | "n" | "o" | "p" | "q" | "r" | "s" | "t" | "u" | "v" | "w" | "x" | "y" | "z" | "_"


### Comentários ###

Existe apenas uma forma de comentário, o comentário de uma linha, iniciado pelo caractere # e que termina ao fim da linha. Qualquer comentário atua como uma nova linha.


### Identificadores ###

Identificadores nomeam entidades de um programa, tais como variáveis e tipos. Um identificador é uma sequência de uma ou mais letras e dígitos. O primeiro caratere de um identificador deve, obrigatoriamente, ser uma letra.

    identifier = letter { letter | decimal_digit }


### Palavras reservadas (Keywords) ###

As palavras seguintes são reservadas para a linguagem e não podem ser usadas como identificadores.

    return      else      pass      for      try
    if          loop      exit      del      until
    class       or        and       in       not


### Operadores e Delimitadores ###

As sequências de caracteres seguinte representam operadores, delimitadores e outros tokens da linguagem:

    +      -      +=      -=      *
    /      *=      /=     (       )


### Inteiros literais ###

Um inteiro literal é uma sequência de dígitos representando uma contante inteira. Um prefixo opicional define a base do literal: 0 para octal e 0x ou 0X para hexadecimal. Literais hexadecimais suportam as letras a-f e A-F para representar valores de 10 à 15.

    int_literal = decimal_literal | octal_literal | hex_literal
    decimal_literal = ( "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" ) { decimal_digit }
    octal_literal = "0" { octal_digit }
    hex_literal = "0" ( "x" | "X" ) hex_digit { hex_digit }


### Literais ponto flutuante ###

Literal ponto flutuante é uma sequência de dígitos representando uma constante de ponto flutuante. Possui uma parte inteira, um ponto decimal, e outra parte fracionária. Tanto a parte inteira quanto a fracionária, são compostas de dígitos decimais.

    float_literal = decimals "." [decimals] | "." decimals
    decimals = decimal_digit { decimal_digit }

*Todo* Expoentes

### Strings literais ###


### Constantes ###


### Tipos ###

#### Tipos booleano ####


#### Tipos numéricos ####


#### Tipos string ####


#### Tipos array ####
