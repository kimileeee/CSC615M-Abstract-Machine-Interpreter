parser grammar AbstractMachineParser;
options {
    language = Python3;
    tokenVocab = AbstractMachineLexer;
}

program : DATA memory_declaration+ LOGIC logic_declaration+
        | LOGIC logic_declaration+
        ;

identifer : IDENTIFIER                      # Identifier
          | SYMBOL                          # SymbolAsIdentifier
          ;

memory_declaration  : STACK IDENTIFIER          # StackDeclaration
                    | QUEUE IDENTIFIER          # QueueDeclaration
                    | TAPE IDENTIFIER           # TapeDeclaration
                    ;

logic_declaration   : identifer CLOSE_BRACKET commmand param_list (COMMA param_list)*
                    | identifer CLOSE_BRACKET memory_operation param_list (COMMA param_list)*
                    | identifer CLOSE_BRACKET direction param_list (COMMA param_list)*
                    ;

commmand    : SCAN
            | PRINT
            | SCAN_RIGHT
            | SCAN_LEFT
            ;

memory_operation    : READ OPEN_PAR IDENTIFIER CLOSE_PAR
                    | WRITE OPEN_PAR IDENTIFIER CLOSE_PAR
                    ;

direction  : RIGHT
            | LEFT
            | UP
            | DOWN
            ;

move_over_tape : direction OPEN_PAR IDENTIFIER CLOSE_PAR
               ;

replacement : SYMBOL SLASH SYMBOL
            ;

param_list : OPEN_PAR SYMBOL COMMA identifer CLOSE_PAR 
           | OPEN_PAR replacement COMMA identifer CLOSE_PAR
           ;