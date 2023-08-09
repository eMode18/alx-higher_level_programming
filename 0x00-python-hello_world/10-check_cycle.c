#include "lists.h"

/**
 * check_cycle - inspect if linked list includes a list
 * @list: list to inspect
 *
 * Return: 1 on success and ) on faiure
 */
int check_cycle(listint_t *list)
{
	listint_t *bad = list;
	listint_t *great = list;

	if (!list)
		return (0);

	while (bad && great && great->next)
	{
		bad = bad->next;
		great = great->next->next;
		if (bad == great)
			return (1);
	}

	return (0);
}

