#include <stdio.h>
#include <stdlib.h>

struct node {
    int data;
    struct node* next;
};

int main() {
    struct node *n1, *n2, *tmp;

    // Print "Hello World!" with the result of 10 + 9
    printf("Hello World! %d", (10 + 9));

    // Print message for linked list
    printf("\nThe linked list is: ");

    // Allocate memory for nodes
    n1 = (struct node*)malloc(sizeof(struct node));
    n2 = (struct node*)malloc(sizeof(struct node));

    // Check if memory allocation was successful
    if (n1 == NULL || n2 == NULL) {
        printf("Memory allocation failed\n");
        return 1;
    }

    // Initialize the nodes
    n1->data = 552;
    n1->next = n2;

    n2->data = 103;
    n2->next = NULL;

    // Traverse and print the linked list
    tmp = n1;
    while (tmp != NULL) {
        printf("%d ", tmp->data);
        tmp = tmp->next;
    }
    printf("NULL\n");

    // Free the allocated memory
    free(n1);
    free(n2);

    return 0;
}
