#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * struct listint_r - a list that is singly linked
 * @n: int value
 * @next: next node pointer
 *
 * Description: node fr singly linked list
 */
typedef struct listint_r
{
	int n;
	struct listint_r *next;
} listint_t;

int check_cycle(listint_t *list);
void free_listint(listint_t *head);
size_t print_listint(const listint_t *h);
listint_t *add_nodeint(listint_t **head, const int n);

#endif
