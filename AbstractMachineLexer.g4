lexer grammar AbstractMachineLexer;

channels {
    ERRORS
}

// Keywords
DATA : '.DATA';
STACK : 'STACK';
QUEUE : 'QUEUE';
TAPE : 'TAPE';
TAPE_2D: '2D_TAPE';

LOGIC : '.LOGIC';
SCAN : 'SCAN';
PRINT : 'PRINT';
SCAN_RIGHT : 'SCAN RIGHT';
SCAN_LEFT : 'SCAN LEFT';
READ : 'READ';
WRITE : 'WRITE';
RIGHT : 'RIGHT';
LEFT : 'LEFT';
UP : 'UP';
DOWN : 'DOWN';

// ACCEPT: 'accept';
// REJECT: 'reject';

// Operators
COMMA : ',';
CLOSE_BRACKET : ']';
OPEN_PAR : '(';
CLOSE_PAR : ')';
SLASH : '/';

// TODO: How to differentiate symbol A from identifier A?
SYMBOL : [a-zA-Z0-9#$];
IDENTIFIER : [a-zA-Z][a-zA-Z0-9_]*;

WS : [ \t\r\n]+ -> skip;