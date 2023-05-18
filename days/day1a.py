import fileinput

inputfile = "inputfiles/day1_input.txt"

firstline = True
lastvalue = 0
increments = 0
for line in fileinput.input(inputfile):
    value = int(line)
    if firstline:
        firstline = False
    elif value > lastvalue:
        increments += 1
    lastvalue = value

print(increments)
