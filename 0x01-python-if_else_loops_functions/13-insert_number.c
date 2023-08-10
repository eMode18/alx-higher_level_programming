#include "lists.h"

/**
 * insert_node - add number to sorted list
 * @head: linked list pointer (head)
 * @number: number
 *
 * Return: New node pointer, else NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *_node = *head, *curr;

	curr = malloc(sizeof(listint_t));
	if (curr == NULL)
		return (NULL);
	curr->n = number;

	if (_node == NULL || _node->n >= number)
	{
		curr->next = _node;
		*head = curr;
		return (curr);
	}

	while (_node && _node->next && _node->next->n < number)
		_node = _node->next;

	curr->next = _node->next;
	_node->next = curr;

	return (curr);
}

