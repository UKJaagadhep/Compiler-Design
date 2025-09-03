%{
#include <stdio.h>
%}

%%

[ \t\n]+                  ;                  // Ignore whitespace
[a-zA-Z_][a-zA-Z0-9_]*    { printf("id\n"); } // Identifiers as 'id'
"+"                       { printf("+\n"); }  // Plus operator
.                         { printf("Invalid token: %s\n", yytext); }

%%

int main() {
    yylex();
    return 0;
}

