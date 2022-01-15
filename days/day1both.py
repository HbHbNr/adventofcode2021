import fileinput

inputfile = "inputfiles/day1_input.txt"


def sweep(windowsize):
    lastwindow = []
    increments = 0
    for line in fileinput.input(inputfile):
        value = int(line)
        if len(lastwindow) < windowsize:
            lastwindow.append(value)
        else:
            currentwindow = lastwindow[1:]
            currentwindow.append(value)
            if(sum(currentwindow) > sum(lastwindow)):
                increments += 1
            lastwindow = currentwindow
        # print(lastwindow)
    return increments


for windowsize in [1, 3]:
    print('windowsize {}: {} increments'.format(windowsize, sweep(windowsize)))
