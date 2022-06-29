#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 *insert_node - function that inserts node to a linked list
 *@head: pointer to the pointer to the head of the list
 *@number: number to be added to list
 *Return: newNode or NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp;
	listint_t *newNode;
	listint_t *current;
	listint_t *first;
	int count = 0, i, p;

	p = 0;
	newNode = malloc(sizeof(listint_t));
	if (newNode == NULL)
		return (NULL);
	current = *head;
	while (count < number)
	{
		current = current->next;
		count = current->n;
		p++;
	}
	first = *head;
	for (i = 1; i < p; i++)
	{
		first = first->next;
	}
	temp = first->next;
	first->next = newNode;
	newNode->n = number;
	newNode->next = temp;
	return (newNode);
}
