#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - Checks if a singly-linked list contains a cycle.
 * @list: A singly-linked list.
 *
 * Return: If  no cycle - 0.
 *         If  cycle - 1.
 */
int check_cycle(listint_t *list)
{
	listint_t *walk, *sprint;

	if (list == NULL || list->next == NULL)
		return (0);

	walk = list->next;
	sprint = list->next->next;

	while (walk && sprint && sprint->next)
	{
		if (walk == sprint)
			return (1);

		walk = walk->next;
		sprint = sprint->next->next;
	}

	return (0);
}
