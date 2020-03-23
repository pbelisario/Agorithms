'''
 You want to schedule a meeting of a certain duration with a coworker. 
 You have access to your calendar and your coworker's calendar 
  (both of which contain your respective meetings for the day, in the form of [startTime, endTime]), 
 as well as both of your daily bounds 
  (i.e., the earliest and latest times at which you're available for meetings every day, 
    in the form of[earliestTime, latestTime]). 

Inputs:  your calendar, 
         your daily bounds,
         your coworker's calendar, 
         your coworker's daily bounds,
         the duration of the meeting that you want to schedule

Return:  A list of all the time blocks(in the form of[startTime, endTime]) 
          during which you could schedule the meeting. 
          
Note that times will be given and should be returned in military time(example times: '8:30', '9:01', '23:56').

'''

def calendarMatching(calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration):

    updatedCalendar1 = updateCalendar(calendar1, dailyBounds1)

    updatedCalendar2 = updateCalendar(calendar2, dailyBounds2)

    mergedCalendars = mergeCalendars(updatedCalendar1, updatedCalendar2)
    
    flattenedCalendar = flattenCalendar(mergedCalendars)

    return getMatchingAvailabilities(flattenedCalendar, meetingDuration)

def updateCalendar(calendar, dailyBounds):
    updatedCalendar = calendar[:]
    updatedCalendar.insert(0, ['00:00', dailyBounds[0]])
    updatedCalendar.append([dailyBounds[1], '23:59'])
    return list(map(lambda m: [timeToMinutes(m[0]), timeToMinutes(m[1])], updatedCalendar))

def timeToMinutes(time):
    hours, minutes = list(map(int, time.split(':')))
    return hours * 60 + minutes

def mergeCalendars(calendar1, calendar2):
    merged = []
    i, j = 0, 0
    while i < len(calendar1) and j < len(calendar2):
        meeting1, meeting2 = calendar1[i], calendar2[j]
        if meeting1[0] < meeting2[0]:
            merged.append(meeting1)
            i += 1
        else:
            merged.append(meeting2)
            j += 1
    # In case one calendar is bigger than another
    while i < len(calendar1):
        merged.append(meeting1)
        i += 1
    while j < len(calendar2):
        merged.append(meeting2)
        j += 1

    return merged

def flattenCalendar(calendar):
    flattened = [calendar[0][:]]
    print(flattened)
    for i in range(1, len(calendar)):
        currMeeting = calendar[i]
        prevMeeting = flattened[-1]

        currStart, currEnd = currMeeting
        prevStart, prevEnd = prevMeeting

        if prevEnd == currStart:
            newPrevMeeting = [prevStart, max(currEnd, prevEnd)]
            flattened[-1] = newPrevMeeting
        
        # No overlap
        else:
            flattened.append(currMeeting[:])
    
    return flattened

def getMatchingAvailabilities (calendar, meetingDuration):
    matchingAvailabilities = []
    for i in range(1, len(calendar)):
        start = calendar[i - 1][1]
        end = calendar[i][0]
        availabilityDuration = end - start
        if availabilityDuration >= meetingDuration:
            matchingAvailabilities.append([start, end])
    return list(map(lambda m: [minutesToTime(m[0]), minutesToTime(m[1])], matchingAvailabilities))

def minutesToTime(minutes):
    hours = minutes // 60
    minutes = minutes % 60
    hourString = str(hours)
    minuteString = '0' + str(minutes) if minutes < 10 else str(minutes)
    return hourString + ':' + minuteString

c1 = [["9:00", "10:30"], ["12:00", "13:00"], ["16:00", "18:00"]]
db1 = ["9:00", "20:00"]
c2 = [["10:00", "11:30"], ["12:30", "14:30"], ["14:30", "15:00"], ["16:00", "17:00"] ]
db2 = ["10:00", "18:30"]
mtdr = 30
print(calendarMatching(c1, db1, c2, db2,mtdr))