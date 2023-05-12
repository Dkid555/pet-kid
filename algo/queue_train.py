import queue

if __name__ == "__main__":
    q = queue.PriorityQueue()
    l = [0, 10, 15, 20, 99, -1]
    # for num in l:
    #    q.put(num)
    # print(q.get())
    q.put((2, "hello world"))
    q.put((11, 99))
    q.put((5, 7.5))
    q.put((1, True))
    # print(q.full())
    while not q.empty():
        print(q.get()[0])
