def josephus(n, k):
    link = range(1, n + 1)
    ind = 0
    for loop_i in range(n - 1):
        ind = (ind + k) % len(link)
        ind -= 1
        print 'Kill:', link[ind]
        del link[ind]
        if ind == -1:  # the last element of link
            ind = 0
    print 'survice :', link[0]


if __name__ == '__main__':
    josephus(30, 10)
    print '-' * 30
    josephus(10, 5)
    print '-' * 30
    josephus(10, 1)