%%
[0-9]+         { printf("Number: %s\n", yytext); }
[+\-*/]        { printf("Operator: %s\n", yytext); }
[()=]          { printf("Symbol: %s\n", yytext); }
[ \t\n]+       ;
.              { printf("Unknown: %s\n", yytext); }
%%

int main() {
    yylex();
    return 0;
}
