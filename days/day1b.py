import fileinput

inputfile = "day1_input.txt"

lastwindow = []
increments = 0
for line in fileinput.input(inputfile):
    value = int(line)
    if len(lastwindow) < 3:
        lastwindow.append(value)
    else:
        currentwindow = lastwindow[1:]
        currentwindow.append(value)
        if(sum(currentwindow) > sum(lastwindow)):
            increments += 1
        lastwindow = currentwindow
    # print(lastwindow)

print(increments)
