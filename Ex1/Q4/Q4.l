%%
[a-z]+.in    { printf("Website"); }
.+           { printf("Not a website"); }
[ \t\n]+     ;
%%

int main() {
    yylex();
    return 0;
}


