#include "learn.h"

using namespace std;

int main()
{
	mystruct* aa = new mystruct(28, 99.8);

	printf("age = %d\n", aa->age);

	printf("%s", "yes");

	return 0;
}

/*
This constructor!
age = 28
yes
*/
