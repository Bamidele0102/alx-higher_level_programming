#include "lists.h"

/**
 * check_cycle - Function to check if there is a cycle in the list
 * @list: Linked list to check
 * Return: 1 if the list has a cycle, 0 if it doesn't
 */

int check_cycle(listint_t *list)
{
	listint_t *hare, *tortoise;

	if (!list)
		return (0);

	hare = list;
	tortoise = list;

	while (hare->next && hare->next->next)
	{
		hare = hare->next->next;
		tortoise = tortoise->next;

		/* Circle is found if nodes match */
		if (hare == tortoise)
			return (1);
	}

	return (0);
}
