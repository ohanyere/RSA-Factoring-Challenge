#include <stdio.h>

/**
* main - function that calculates the factors
*
* Return: 0 on Success
*/
int main(void)
{
	long long int number = 239809320265259;
	long int fact1 = 2;
	long int fact2;

	while (number % fact1)
	{
		if (fact1 <= number)
		{
			fact1++;
		}
		else
		{
			return (-1);
		}
	}

	fact2 = number / fact1;
	printf("%lld = %ld * %ld\n", number, fact2, fact1);
	return (0);
}
