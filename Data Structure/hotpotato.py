import queue

def hotpotato(namelist, num):
    simqueue = queue.Queue()

    for name in namelist:
        simqueue.enqueue(name)

    while simqueue.size() >1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())

        simqueue.dequeue()

    return simqueue.dequeue()


print(hotpotato(["BILL", "MIKE", "BOB", "JANE"], 6))
