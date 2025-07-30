%{
#include <stdio.h>
int word = 0, dgit = 0, spce = 0, spec = 0;
%}

%%
[ \t]+              { spce++; }
[0-9]+              { dgit++; }
[a-zA-Z]+           { word++; }
[^a-zA-Z \t\n0-9]   { spec++; }
\n                  ; // Ignore
%%

int main() {
    yylex();
    printf("Words: %d\nDigits: %d\nSpaces: %d\nSpecials: %d\n", word, dgit, spce, spec);
    return 0;
}


