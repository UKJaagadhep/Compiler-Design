%{
#include <stdio.h>
#include <ctype.h>
#define YYSTYPE double    // to handle floating point numbers
int yylex();
int yyerror();
%}

%token NUMBER
%left '+' '-'
%left '*' '/'
%right UMINUS

%%

lines:
      lines expr '\n'   { printf("= %g\n", $2); }
    | lines '\n'
    | /* empty */
    ;

expr:
      expr '+' expr     { $$ = $1 + $3; }
    | expr '-' expr     { $$ = $1 - $3; }
    | expr '*' expr     { $$ = $1 * $3; }
    | expr '/' expr     { $$ = $1 / $3; }
    | '(' expr ')'      { $$ = $2; }
    | '-' expr %prec UMINUS { $$ = -$2; }
    | NUMBER
    ;

%%

// lexical analyzer
int yylex() {
    int c;
    while ((c = getchar()) == ' ');   // skip spaces
    if (c == '.' || isdigit(c)) {
        ungetc(c, stdin);
        scanf("%lf", &yylval);
        return NUMBER;
    }
    return c;
}

// error handler
int yyerror() {
    printf("Invalid Expression!\n");
    return 1;
}

int main() {
    printf("Enter expression:\n");
    yyparse();
    return 0;
}

int yywrap() { return 1; }



