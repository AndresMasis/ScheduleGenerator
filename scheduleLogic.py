from itertools import product


coursesDictionary = {}
keysList = []
generatedSchedules = []

'''coursesDictionary = {'Arquitectura': [{'Jorge': [(0,1),(0,2),(3,1),(3,2)], 'Kirstein': [(5,8),(6,9),(5,8),(6,9)]}, 4],
                        'Analisis': [{'Chinito': [(6,5),(7,2),(6,5),(7,2)], 'Ivannia': [(0,1),(0,2),(3,1),(3,2)]}, 4],
                        'Ingles': [{'Katherine': [(0,1),(0,2),(3,1),(3,2)], 'Daniel': [(0,1),(0,2),(3,1),(3,2)]}, 2]}
                        
   keysList = ['Arquitectura', 'Analisis', 'Ingles']
   generatedSchedules = [['Jorge', 'Chinito', 'Katherine'], ['Kirstein', 'Ivannia', 'Daniel'], ['Jorge', 'Ivannia', 'Daniel']]'''


'''-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
   This function creates a new course
   Courses are lists that contain a dictionary of teachers and the credits of the course
   Courses list are added to courseDictionary
   It receives as parameter a string that is the course name (the key of the course), and an integer that is the credits amount (part of the value list)
   It does not return anything'''


def addCourse(courseName, credits):
    coursesDictionary[courseName] = []  # Creates the course in the dictionary
    coursesDictionary[courseName].append({})  # Creates the teacher dictionary of that specific course
    coursesDictionary[courseName].append(credits)  # Adds the amount of credits of that course

    keysList.append(courseName)  # Keeps the order for the keys backup


'''-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
   This function adds a new teacher to a course
   Teachers are added to the teacher dictionary of a course
   It receives as parameter a string that is the key of the course where the new teacher will be added
   another string that is the name of the new teacher (its key in the teachers dictionary)
   and a list of tuples that is the teachers schedule (its value in the teachers dictionary)
   It does not return anything'''


def addTeacherToCourse(courseName, teacherName, teacherSchedule):
    coursesDictionary[courseName][0][teacherName] = teacherSchedule


'''-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
   This deletes a course from courseDictionary
   It receives as parameter a string that is the course name (the key of the course)
   It does not return anything'''


def deleteCourse(courseName):
    del coursesDictionary[courseName]  # Deletes the course in the dictionary
    keysList.remove(courseName)  # Keeps the order for the keys backup


'''-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
   This function deletes a teacher from the teacher dictionary of a course
   It receives as parameter a string that is the key of the course where the teacher resides
   another string that is the name of the new teacher (its key in the teachers dictionary)
   It does not return anything'''


def deleteTeacherFromCourse(courseName, teacherName):
    del coursesDictionary[courseName][0][teacherName]


'''-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
   This function changes the name of a course
   This will change the key of the course in coursesDictionary
   Also rearranges the keysList
   It receives as parameter a string that is the current key of the course in coursesDictionary
   another string that is the new name of the course (it will be the new key in coursesDictionary)
   It does not return anything'''


def updateCourseName(oldName, newName):
    # Updates the dictionary
    coursesDictionary[newName] = coursesDictionary.pop(oldName)

    # Updates the list
    keysList.remove(oldName)
    keysList.append(newName)


'''-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
   This function changes the name of a teacher in a specific course
   This will change the key of the teacher in the teachers dictionary of just that course
   It receives as parameter a string that is the key of the course where the teacher currently resides
   another string that is the current (name) key of the teacher in the teachers dictionary of that course
   also a string that is the new name of the teacher (it will be the new key in the teacher dictionary of that course)
   It does not return anything'''


def updateTeacherNameOnce(courseKey, oldName, newName):
    # Updates the teachers dictionary of the given course
    coursesDictionary[courseKey][0][newName] = coursesDictionary[courseKey][0].pop(oldName)


'''-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
   This function changes the name of a teacher in all the courses he appears
   This will change the key of the teacher in the teachers dictionary of all the courses he appears
   It receives as parameter a string that is the current (name) key of the teacher in the teachers dictionary
   also a string that is the new name of the teacher (it will be the new key in the teacher dictionary)
   It does not return anything'''


def updateTeacherNameAll(oldName, newName):
    # Goes thru all the courses dictionary checking course by course
    for courseKey, courseValue in coursesDictionary.items():
        # It takes a specific course to analyze
        # courseValue looks like [{'Jorge': [(0,1),(0,2),(3,1),(3,2)], 'Kirstein': [(5,8),(6,9),(5,8),(6,9)]}, 4]

        # Checks if the teacher (key) exists in the teachersDictionary
        if oldName in courseValue[0].keys():
            # That teacher does exist, so it can be modified
            coursesDictionary[courseKey][0][newName] = coursesDictionary[courseKey][0].pop(oldName)


'''-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
   This function changes the value of the credits of a course
   It receives as parameter a string that is the key of the course
   also an int that is the new amount of credits
   It does not return anything'''


def updateCourseCredits(courseName, newCredits):
    coursesDictionary[courseName][1] = newCredits


'''-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
   This function changes the schedule of a teacher in a specific course
   It receives as parameter a string that is the key of the course where the teacher resides
   another string that is the teacherKey
   and a list of tuples that is the new schedule
   It does not return anything'''


def updateTeacherSchedule(courseName, teacherName, newSchedule):
    coursesDictionary[courseName][0][teacherName] = newSchedule


'''-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
   This function checks which of 2 teachers has the lower priority in case there is collision
   The decision is based on who has the higher amount of credits in the course they are giving
   It receives 2 strings as parameters which are the courses of each teacher to be compared
   It returns True if the first teacher has lower priority
   It returns False in case the second has lower priority or both have the same priority'''


def firstIsLessImportant(courseA, courseB):
    if coursesDictionary[courseA][1] < coursesDictionary[courseB][1]:
        return True
    else:
        return False


'''-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
   This function checks if a teacher combination has collisions
   In case that a teacher crashes with another one, it prioritizes the one with a course with higher credits and deletes the other one
   It receives as parameter a list which is the combination with no collisions checked
   It returns the combination with combinations checked'''


def checkCombination(teachers):
    combination = mergeData(teachers)

    # Compares a single teacher with all the others
    i = 0  # Index for the current teacher
    for currentTeacher in combination:
        # Takes a single teacher to be compared
        j = 0  # Index of the comparison teacher per comparison iteration
        for comparisonTeacher in combination:
            if i != j:
                # It makes sure it is comparing 2 different individuals

                # The schedules are lists of tuples [(0,1),(0,2),(3,1),(3,2)]
                currentTeacherSchedule = coursesDictionary[keysList[i]][0][currentTeacher[2]]  # current teacher
                comparisonTeacherSchedule = coursesDictionary[keysList[j]][0][comparisonTeacher[2]]  # comparison teacher


                # Checks if one of the tuples of the currentTeacher is in the other teacher schedule
                for scheduleTuple in currentTeacherSchedule:
                    if scheduleTuple in comparisonTeacherSchedule:
                        # A collision was found

                        # Checks which teacher survive and which one is gone
                        if firstIsLessImportant(keysList[i], keysList[j]):
                            # First one leaves, second one stays
                            if currentTeacher in combination:
                                combination.remove(currentTeacher)

                        else:
                            # Second one leaves, first one stays
                            if comparisonTeacher in combination:
                                combination.remove(comparisonTeacher)

                j += 1

        i += 1

    return combination


'''-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
   This function is an auxiliary I needed
   This function makes all the possible combinations of teachers of coursesDictionary
   It receives as argument a dict_value
   It looks like dict_values([[{'Law Wa Yuen': [(3, 7), (3, 8)], 'Ivannia Cerdas': [(3, 7), (5, 8)]}, 4], [{'Daniel Lewis': [(3, 5), (3, 6), (3, 7)]}, 2], [{'Platon de Atenas': [(0, 3), (2, 4)]}, 2]])
   It makes a list of list
   Each sublist is a list of the teachers of a given course
   It returns the flattened list'''


def myFunction(argument):
    myList = []

    for element in argument:
        myList.append(tuple(element[0].keys()))

    return myList


'''-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
   This function makes all the possible combinations of teachers of coursesDictionary
   It combines each teacher of course A, with each teacher of course B, with each teacher of course C and son on
   If fills the generatedSchedules list by appending all the possible combination
   It receives no parameters and does not return anything'''


def makeCombinations():
    # This for creates all the possible combinations of teachers between different courses
    for combination in product(*myFunction(coursesDictionary.values())):
        # combination is a tuple that has a combination of teachers (it has the teacher name which is his key)   (Jorge, Yuen, Ivannia)

        #                         checks if the created combination has collisions
        generatedSchedules.append(checkCombination(combination))


'''-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
   This function fills the course of the teacher, its schedule and credits
   It receives as parameter a list of names
   It receives a list of tuples according to the the given names'''


def mergeData(combination):
    retList = []

    i = 0
    for teacher in combination:
        #             Course name       course credits                teacher name         teacher schedule
        retList.append((keysList[i], coursesDictionary[keysList[i]][1], teacher, coursesDictionary[keysList[i]][0][teacher]))
        i += 1

    return retList


'''-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
   This finds if a coordinate is part of the generated schedules
   It receives as parameter one of the approved teacher combinations, and both values of the coordinate
   In case the coordinate does exist in the combination, it returns the index of the teachers that holds it
   In case the coordinate does not exist in the combination, it returns none'''


def checkPositionInTuple(combination, i, j):
    # It adjust i variable, needed by the triple spaces
    i //= 4

    pos = 0
    for teacher in combination:
        if (j, i) in teacher[-1]:
            # The teacher was found
            return pos

        pos += 1

    # The teacher was never found
    return None


'''-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
   This function resizes a string to exactly 36 characters
   It receives as parameter the string to be resized
   It returns the resized string'''


def resizeStr(myString):
    # Makes the string longer
    while len(myString) < 36:
        myString += ' '

    # Makes the string shorter
    while len(myString) > 36:
        myString = myString[:-1]

    return myString


'''-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
   This function prints in console all the generated schedules
   It doesnt receive any parameters
   It doesnt return anything'''


def printSchedule():
    # Base to print the hours of the schedule
    hoursList = ('7:30', '8:20', '\t', '-------', '8:30', '9:20', '\t', '-------', '9:30', '10:20', '\t', '-------', '10:30', '11:20', '\t', '-------', '11:30', '12:20',
                 '\t', '-------', '13:00', '13:50', '\t', '-------',  '14:00', '14:50', '\t', '-------',  '15:00', '15:50', '\t', '-------', '16:00', '16:50', '\t', '-------',  '17:00', '17:50',
                 '\t', '-------', '18:00', '18:50', '\t', '-------',  '19:00', '19:50', '\t', '-------', '20:00', '20:50', '\t', '-------', '21:00', '21:50', '\t', '-------')

    # Print the schedule for each created combination
    for combination in generatedSchedules:
        # Prints the days at the very first in the top for the combination
        print('\t\t---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        print('\t\t|\t\t\t\t\tLunes\t\t\t\t\t|\t\t\t\tMartes\t\t\t\t\t\t|\t\t\t\t\tMiercoles\t\t\t\t|\t\t\t\t\tJueves\t\t\t\t\t|\t\t\t\t\tViernes\t\t\t\t\t|\t\t\t\t\tSabado\t\t\t\t\t|')
        print('-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')

        # This for manages the vertical part, it has line jumps
        for i in range(56):
            # It prints the hour. Ex: 7:30  |
            print(hoursList[i] + "\t", end="|  ")

            # This for manages the horizontal part, it goes on the same line
            for j in range(0, 6):
                dataPos = i % 4  # Determines what part of the data will be printed, needed for the adjustment

                if dataPos == 3:
                    # It is the turn of the separation between a block and the next one
                    print('--------------------------------------------', end='')

                else:
                    # In this turn it may be data
                    foundTeacherPos = checkPositionInTuple(combination, i, j)  # Determines if it has data or not

                    if foundTeacherPos is None:
                        # It was not data
                        print('\t\t\t\t\t\t\t\t\t\t\t', end='|  ')

                    else:
                        # It is data

                        if dataPos == 0:
                            # It is the name of the course
                            stringToPrint = resizeStr(combination[foundTeacherPos][0])
                            print(stringToPrint + '\t\t', end='|  ')

                        elif dataPos == 1:
                            # It is the amount of credits
                            stringToPrint = resizeStr(str(combination[foundTeacherPos][1]) + ' creditos')
                            print(stringToPrint + '\t\t', end='|  ')

                        elif dataPos == 2:
                            # It is the name of the teacher
                            stringToPrint = resizeStr(combination[foundTeacherPos][2])
                            print(stringToPrint + '\t\t', end='|  ')

            # Prints a line jump at the end of each line of the schedule
            print('')

        # Prints several spaces between a schedule and another to separate them
        print('\n\n\n\n')


'''-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
   Currently used for tests'''


def test():
    addCourse("Analisis de Algoritmos", 4)
    addCourse("Arquitectura de Computadores",4)
    addCourse("Ingles", 2)
    addCourse("Seminarios de Estudios Filosoficos", 2)

    addTeacherToCourse("Analisis de Algoritmos", "Law Wa Yuen", [(1, 5), (1, 6), (3, 5), (3, 6)])
    addTeacherToCourse("Analisis de Algoritmos", "Ivannia Cerdas", [(2, 0), (2, 1), (4, 0), (4, 1)])

    addTeacherToCourse("Arquitectura de Computadores", "Jorge Vargas", [(2, 10), (2, 11), (4, 10), (4, 11)])
    addTeacherToCourse("Arquitectura de Computadores", "Kirstein Gatjens", [(0, 0), (0, 1), (0, 2), (0, 3)])

    addTeacherToCourse("Ingles", "Daniel Lewis", [(0, 2), (0, 3), (0, 4)])

    addTeacherToCourse("Seminarios de Estudios Filosoficos", "Platon de Atenas", [(1, 3), (1, 4), (3, 3), (3, 4)])
    addTeacherToCourse("Seminarios de Estudios Filosoficos", "Confucio", [(0, 0), (0, 1), (2, 0), (2, 1)])

    makeCombinations()

    printSchedule()


if __name__ == "__main__":
    test()
    print()