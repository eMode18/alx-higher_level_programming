/*
 * File: c function to check if string is palindrome
 */

#include "lists.h"

listint_t *reverse_listint(listint_t **head);
int is_palindrome(listint_t **head);

/**
 * reverse_listint - Reverse list
 * @head: list pointer
 *
 * Return: reversed list pointer
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *node = *head, *next, *previous = NULL;

	while (point)
	{
		next = point->next;
		point->next = prev;
		previous = point;
		point = next;
	}

	*head = previous;
	return (*head);
}

/**
 * is_palindrome - Check palidnrome
 * @head: list pointer
 *
 * Return: not a palindrome - 0.
 *         palindrome - 1.
 */
int is_palindrome(listint_t **head)
{
	listint_t *store, *reverse, *split;
	size_t _length = 0, k;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	store = *head;
	while (store)
	{
		_length++;
		store = store->next;
	}

	store = *head;
	for (k = 0; k < (_length / 2) - 1; k++)
		store = store->next;

	if ((_length % 2) == 0 && store->n != store->next->n)
		return (0);

	store = store->next->next;
	reverse = reverse_listint(&store);
	split = reverse;

	store = *head;
	while (reverse)
	{
		if (store->n != reverse->n)
			return (0);
		store = store->next;
		reverse = reverse->next;
	}
	reverse_listint(&split);

	return (1);
}

