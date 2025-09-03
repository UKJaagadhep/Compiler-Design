#include <stdio.h>
#include <string.h>

#define MAX 100
// holds tokens like id, +
char tokens[MAX][10]; 
int pos = 0, n = 0;

// Simulate reading tokens from LL lexer output
void read_tokens_from_stdin() {
    while (scanf("%s", tokens[n]) != EOF) {
        n++;
    }
}

// Grammar:
// E  → id E'
// E' → + id E' | ε

int E();
int Eprime();

int E() {
    if (strcmp(tokens[pos], "id") == 0) {
        pos++;
        return Eprime();
    }
    return 0;
}

int Eprime() {
    if (strcmp(tokens[pos], "+") == 0) {
        pos++;
        if (strcmp(tokens[pos], "id") == 0) {
            pos++;
            return Eprime();
        }
        return 0;
    }
    return 1; // ε
}

int main() {
    printf("Enter tokens from LL lexer (e.g. id + id):\n");
    read_tokens_from_stdin();
    
    if (E() && pos == n) {
        printf("LL Parsing Success\n");
    } else {
        printf("LL Parsing Failed\n");
    }

    return 0;
}

