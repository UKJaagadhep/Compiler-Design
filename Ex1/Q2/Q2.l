%{
#include <stdio.h>
#include <stdlib.h>
%}

%%

[0-9]+    {
              int num = atoi(yytext);
              if (num % 2 == 0)
                  printf("EVEN number: %d\n", num);
              else
                  printf("ODD number: %d\n", num);
          }

[ \t\n]   ; // Ignore 
.         { printf("Invalid input: %s\n", yytext); }

%%

int main() {
    printf("Enter numbers separated by space:\n");
    yylex();
    return 0;
}


