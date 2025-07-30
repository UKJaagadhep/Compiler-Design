%%
[0-9]+\.[0-9]+  { printf("Float: %s\n", yytext); }
[0-9]+          { printf("Integer: %s\n", yytext); }
[ \t\n]+        ;
.               ; // Ignore everything else
%%

int main() {
    yylex();
    return 0;
}
