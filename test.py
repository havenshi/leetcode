input = 'In the example of Figure 2 (b), according to the definition of the Topological Sort: "If there is an edge (X, Y), vertex (X) must appear before vertex (Y) in the sequence, (rice, rice), the sequence may be "fish, rice, meat, vegetables", but it also exists edge (rice, pork), the sequence may be "rice, meat, vegetables, fish", and the second sequence In violation of "the existence of edge (fish, rice), the fish to eat before eating" restrictions.'
n = len(input)
newinput = input.split(' ')
result = []
tmp = []
count = 1
i = 0
while i < len(newinput):
    newtmp1 = '(%d/%d)' % (count, n) + ' '.join(tmp)
    newtmp2 = newtmp1 + ' ' + newinput[i]
    if len(newtmp2) < 80:
        tmp.append(newinput[i])
        i += 1
    else:
        result.append(newtmp1)
        tmp = []
        count += 1

print result

