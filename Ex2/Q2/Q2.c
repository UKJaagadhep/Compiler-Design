#include <stdio.h>
#include <string.h>

#define MAX 100

char input[MAX][10]; // tokens like id, +
int n = 0;            // total tokens
int top = -1;         // stack top

char stack[MAX][10];  // parser stack

// Function to push to stack
void push(char *sym) {
    strcpy(stack[++top], sym);
}

// Function to pop from stack
void pop() {
    top--;
}

// Function to display stack and input
void print_stack_input(int pos) {
    printf("Stack: ");
    for (int i = 0; i <= top; i++) printf("%s ", stack[i]);
    printf(" | Input: ");
    for (int i = pos; i < n; i++) printf("%s ", input[i]);
    printf("\n");
}

// Try to reduce stack symbols
int reduce() {
    // E → id
    if (strcmp(stack[top], "id") == 0) {
        strcpy(stack[top], "E");
        printf("Reduced: E → id\n");
        return 1;
    }

    // E → E + id
    if (top >= 2 &&
        strcmp(stack[top - 2], "E") == 0 &&
        strcmp(stack[top - 1], "+") == 0 &&
        strcmp(stack[top], "E") == 0) {
        top -= 2;
        strcpy(stack[top], "E");
        printf("Reduced: E → E + E\n");
        return 1;
    }

    return 0;
}

int main() {
    printf("Enter tokens from LR lexer (e.g., id + id):\n");

    // Input from user (tokenized)
    while (scanf("%s", input[n]) != EOF) n++;

    int i = 0;
    while (i < n) {
        push(input[i]);
        i++;
        print_stack_input(i);

        // Keep reducing while possible
        while (reduce()) {
            print_stack_input(i);
        }
    }

    // Final check
    if (top == 0 && strcmp(stack[0], "E") == 0) {
        printf("LR Parsing Success\n");
    } else {
        printf("LR Parsing Failed\n");
    }

    return 0;
}

