#include "lists.h"
#include <stdlib.h>

/**
 * reverse_list - reverses a linked list in-place
 * @head: pointer to the head of the list
 * Return: pointer to the new head of the reversed list
 */
listint_t *reverse_list(listint_t **head)
{
	listint_t *prev = NULL, *current = *head, *next;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	*head = prev;
	return (*head);
}

/**
 * is_palindrome - identifies if a singly linked list is a palindrome
 * @head: pointer to the head of the list
 * Return: 1 if it is palindrome, else 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *second_half;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	// Move 'fast' two steps and 'slow' one step to find the middle
	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		slow = slow->next;
	}

	// If the number of elements is odd, move 'slow' one more step
	if (fast != NULL)
		slow = slow->next;

	// Reverse the second half of the list
	second_half = reverse_list(&slow);

	// Compare the first half with the reversed second half
	while (second_half != NULL)
	{
		if ((*head)->n != second_half->n)
		{
			reverse_list(&slow); // Revert changes to the second half
			return (0);
		}
		*head = (*head)->next;
		second_half = second_half->next;
	}

	reverse_list(&slow); // Revert changes to the second half
	return (1);
}
