parser grammar AbstractMachineParser;
options {
    language = Python3;
    tokenVocab = AbstractMachineLexer;
}

program : (DATA memory_declaration+)* LOGIC logic_declaration+     #FullProgram
        // | LOGIC logic_declaration+                              #LogicOnlyProgram
        ;

identifier : IDENTIFIER                      # IdentifierReal
          | SYMBOL                          # SymbolAsIdentifier
          ;

memory_declaration  : STACK IDENTIFIER          
                    | QUEUE IDENTIFIER          
                    | TAPE IDENTIFIER           
                    | TAPE_2D IDENTIFIER        
                    ;

logic_declaration   : identifier CLOSE_BRACKET command transition (COMMA transition)*                 # CommandLogicDeclaration
                    | identifier CLOSE_BRACKET memory_operation transition (COMMA transition)*         # MemoryOperationLogicDeclaration
                    | identifier CLOSE_BRACKET tape_operation replacement (COMMA replacement)*         # MoveOverTapeLogicDeclaration
                    ;

command    : SCAN                  # ScanCommand
            | PRINT                 # PrintCommand
            | SCAN_RIGHT            # ScanRightCommand
            | SCAN_LEFT             # ScanLeftCommand
            ;

memory_operation    : READ OPEN_PAR identifier CLOSE_PAR        
                    | WRITE OPEN_PAR identifier CLOSE_PAR       
                    ;

tape_operation  : RIGHT OPEN_PAR identifier CLOSE_PAR              
                | LEFT OPEN_PAR identifier CLOSE_PAR             
                | UP OPEN_PAR identifier CLOSE_PAR                
                | DOWN OPEN_PAR identifier CLOSE_PAR              
                ;

transition  : OPEN_PAR SYMBOL COMMA identifier CLOSE_PAR
            ;

replacement : OPEN_PAR SYMBOL SLASH SYMBOL COMMA identifier CLOSE_PAR
            ;

