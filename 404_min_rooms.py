
def getNextTime(schedule, currentTime):
    nextTime = (None,'')
    for period in schedule:
        if period[0] > currentTime[0] and (nextTime[0] is None or period[0] < nextTime[0]):
            nextTime = (period[0], 'Start')
        elif period[1] > currentTime[0] and (nextTime[0] is None or period[1] < nextTime[0]):
            nextTime = (period[1], 'End')
    return nextTime


def getMinRooms(schedule):
    numRooms = 0
    minRooms = 0
    currentTime = (-1, None)
    while True:
        currentTime = getNextTime(schedule, currentTime)
        if currentTime[1] == '':
            break
        else:
            if currentTime[1] == 'Start':
                numRooms += 1
                if numRooms > minRooms:
                    minRooms = numRooms
            else:
                numRooms -= 1
    return minRooms


schedule = [(30, 70), (0, 50), (60, 150)]
print(getMinRooms(schedule))
