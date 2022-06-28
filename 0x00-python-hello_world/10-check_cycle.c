#include <stdio.h>
#include "lists.h"
/**
*check_cyle - function that checks if a linked list is cylic
*@list: poiner to the list
*Return: 1 if cylic or 0 if otherwise
*/
int check_cycle(listint_t *list)
{
listint_t *slow;
listint_t *fast;

slow = fast = list;
while (slow && fast && fast->next)
{
slow = slow->next;
fast = fast->next->next;
if (slow == fast)
return (1);
}
return (0);
}
