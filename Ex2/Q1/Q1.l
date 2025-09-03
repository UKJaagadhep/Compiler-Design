%{
#include <stdio.h>
%}

%%
[ \t\n]+                      ; // Skip whitespace
[a-zA-Z_][a-zA-Z0-9_]*        { printf("id\n"); }
"+"                           { printf("+\n"); }
.                             { printf("Invalid token\n"); }
%%

