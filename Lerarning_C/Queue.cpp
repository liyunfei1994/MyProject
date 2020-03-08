# include <stdio.h>
# include <malloc.h>

typedef struct Queue
{	
	int * pBase;
	int front;
	int rear;
}QUEUE;

void init(QUEUE *);
bool en_queue(QUEUE *, int);
void traverse_queue(QUEUE *);
bool full_queue(QUEUE *);
bool out_queue(QUEUE *, int *);

int main(void)
{
	QUEUE Q;
	int val;

	init(&Q);

	en_queue(&Q, 1);
	en_queue(&Q, 10);
	en_queue(&Q, 20);
	en_queue(&Q, 9);
	en_queue(&Q, 8);
	en_queue(&Q, 99);

	traverse_queue(&Q);

	out_queue(&Q, &val);
	printf("Dequeue! The value is %d\n", val);

	printf("The new queue is:\n");
	traverse_queue(&Q);


	return 0;
}

void init(QUEUE * pQ)
{
	pQ->pBase = (int *)malloc(sizeof(int)*6);	//数组的指针
	pQ->front = 0;
	pQ->rear = 0;
}

bool full_queue(QUEUE * pQ)
{
	if ( (pQ->rear+1) % 6 == pQ->front)
		return true;
	else
		return false;
}

bool en_queue(QUEUE * pQ, int val)
{
	if (full_queue(pQ))
		return false;
	else
	{
		pQ->pBase[pQ->rear] = val;
		pQ->rear = (pQ->rear+1) % 6;


		return true;
	}
}

void traverse_queue(QUEUE * pQ)
{
	printf("The entire queue contains:\n");
	int i = pQ->front;

	while(i != pQ->rear)
	{
		printf("%d ", pQ->pBase[i]);
		i = (i+1)%6;
	}

	printf("\n");

	return;
}

bool empty_queue(QUEUE * pQ)
{
	if (pQ->front == pQ->rear)
		return true;
	else
		return false;
}

bool out_queue(QUEUE * pQ, int * pVal)
{
	if (empty_queue(pQ))
		return false;
	else
	{	
		*pVal = pQ->pBase[pQ->front];
		pQ->front = (pQ->front +1)%6;

		return true;
	}
}

---------------------
---------------------

The entire queue contains:
1 10 20 9 8
Dequeue! The value is 1
The new queue is:
The entire queue contains:
10 20 9 8
