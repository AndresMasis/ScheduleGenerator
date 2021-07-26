import tkinter as tk
from itertools import product


'''
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Backend
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''


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
    if teacherName not in coursesDictionary[courseName][0]:
        coursesDictionary[courseName][0][teacherName] = teacherSchedule

    else:
        addTeacherToCourse(courseName, teacherName + ' ', teacherSchedule)


'''-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
   This deletes a course from courseDictionary
   It receives as parameter a string that is the course name (the key of the course)
   It does not return anything'''


def deleteCourse(courseName):
    del coursesDictionary[courseName]  # Deletes the course in the dictionary
    keysList.remove(courseName)  # Keeps the order for the keys backup


'''-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
   This function deletes a teacher from the teacher dictionary of a course just one time
   It deletes the first teacher with the name it finds
   It receives as parameter a string that is the key of the course where the teacher resides
   another string that is the name of the teacher (its key in the teachers dictionary)
   It does not return anything'''


def deleteTeacherFromCourseOnce(courseName, teacherName):
    del coursesDictionary[courseName][0][teacherName]


'''-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
   This function deletes a teacher from the teacher dictionary of a course all the times it appears
   It deletes all the teachers with the name it finds
   It receives as parameter a string that is the key of the course where the teacher resides
   another string that is the name of the teacher (its key in the teachers dictionary)
   It does not return anything'''


def deleteTeacherFromCourseAll(courseName, teacherName):
    # Removes end spaces in case it is a copy to have as root the most pure name
    teacherName = teacherName.rstrip()

    dictionarySize = len(coursesDictionary[courseName][0])
    i = 0
    # Starts adding spaces to check also for the copies and delete the if so
    while i < dictionarySize:
        if teacherName in coursesDictionary[courseName][0]:
            # Found a key with that desired teacher, deletes it
            del coursesDictionary[courseName][0][teacherName]

        teacherName += ' '  # Adds an space at the end
        i += 1


'''-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
   This function deletes a teacher from the teacher dictionary of all the course all the times it appears
   It deletes all the teachers with the name it finds
   It receives as parameter a string that is the name of the teacher (its key in the teachers dictionary)
   It does not return anything'''


def deleteTeacherFromEverything(teacherName):
    # Removes end spaces in case it is a copy to have as root the most pure name
    rootStr = teacherName.rstrip()

    i = 0
    for course in coursesDictionary:
        dictionarySize = len(course[0])
        j = 0
        # Starts adding spaces to check also for the copies and delete the if so
        while j < dictionarySize:
            if teacherName in coursesDictionary[keysList[i]][0]:
                # Found a key with that desired teacher, deletes it
                del coursesDictionary[keysList[i]][0][teacherName]

            teacherName += ' '  # Adds an space at the end
            j += 1

        i += 1
        teacherName = rootStr


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
   This function changes the name of a teacher in a specific course just one time
   It updates the first teacher that has that name 
   This will change the key of the teacher in the teachers dictionary of just that course
   It receives as parameter a string that is the key of the course where the teacher currently resides
   another string that is the current (name) key of the teacher in the teachers dictionary of that course
   also a string that is the new name of the teacher (it will be the new key in the teacher dictionary of that course)
   It does not return anything'''


def updateTeacherNameCourseOnce(courseKey, oldName, newName):
    # Updates the teachers dictionary of the given course
    coursesDictionary[courseKey][0][newName] = coursesDictionary[courseKey][0].pop(oldName)


'''-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
   This function deletes a teacher from the teacher dictionary of a course all the times it appears
   It deletes all the teachers with the name it finds
   It receives as parameter a string that is the key of the course where the teacher resides
   another string that is the name of the teacher (its key in the teachers dictionary)
   It does not return anything'''


def updateTeacherNameCourseAll(courseKey, oldName, newName):
    # Removes end spaces in case it is a copy to have as root the most pure name
    oldName = oldName.rstrip()

    dictionarySize = len(coursesDictionary[courseKey][0])
    i = 0
    # Starts adding spaces to check also for the copies and delete the if so
    while i < dictionarySize:
        if oldName in coursesDictionary[courseKey][0]:
            # Found a key with that desired teacher, deletes it
            coursesDictionary[courseKey][0][newName] = coursesDictionary[courseKey][0].pop(oldName)
            newName += ' '  # Adds an space at the end to avoid collisions in case another update is needed

        oldName += ' '  # Adds an space at the end
        i += 1


'''-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
   This function changes the name of a teacher in all the courses he appears
   This will change the key of the teacher in the teachers dictionary of all the courses he appears
   It receives as parameter a string that is the current (name) key of the teacher in the teachers dictionary
   also a string that is the new name of the teacher (it will be the new key in the teacher dictionary)
   It does not return anything'''


def updateTeacherNameEverything(oldName, newName):
    # Removes end spaces in case it is a copy to have as root the most pure name
    oldNameRoot = oldName.rstrip()
    newNameRoot = newName.rstrip()

    # Goes thru all the courses dictionary checking course by course
    for courseKey, courseValue in coursesDictionary.items():
        # It takes a specific course to analyze
        # courseValue looks like [{'Jorge': [(0,1),(0,2),(3,1),(3,2)], 'Kirstein': [(5,8),(6,9),(5,8),(6,9)]}, 0]

        # Checks teachers dictionary if it has to teacher to be updated
        dictionarySize = len(coursesDictionary[courseKey][0])
        i = 0
        # Starts adding spaces to check also for the copies and delete the if so
        while i < dictionarySize:
            # Checks if the teacher (key) exists in the teachersDictionary
            if oldName in courseValue[0].keys():
                # That teacher does exist, so it can be modified
                coursesDictionary[courseKey][0][newName] = coursesDictionary[courseKey][0].pop(oldName)
                newName += ' '

            i += 1
            oldName += ' '

        oldName = oldNameRoot
        newName = newNameRoot


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
   This function checks if a teacher combination has collisions
   In case that a teacher crashes with another one, it prioritizes the one with a course with higher credits and deletes the other one
   It receives as parameter a list which is the combination with no collisions checked
   It returns the combination with combinations checked'''


def checkCombination(teachers):
    combination = mergeData(teachers)

    # Compares a single teacher with all the others
    i = 0  # Index for the current teacher
    for currentTeacher in combination:
        # Takes a new single teacher to compare with the teacher we are analyzing

        j = 0  # Index of the comparison teacher per comparison iteration
        for comparisonTeacher in combination:
            if comparisonTeacher != currentTeacher:
                # Checks if one of the tuples of the currentTeacher is in the other teacher schedule
                for scheduleTuple in currentTeacher[-1]:
                    if scheduleTuple in comparisonTeacher[-1]:
                        # A collision was found

                        # Checks which teacher has a higher priority
                        if currentTeacher[1] < currentTeacher[1]:
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
   This function also checks that all the courses have at least 1 teacher each one
   In case everything is alright it returns the flattened list
   In case a course has no teachers, it returns false'''


def myFunction(argument):
    myList = []

    for element in argument:
        if element:
            myList.append(tuple(element[0].keys()))

        else:
            # There is a course with no teachers
            return False

    # Returns the flattened list
    return myList


'''-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
   This function makes all the possible combinations of teachers of coursesDictionary
   It combines each teacher of course A, with each teacher of course B, with each teacher of course C and son on
   If fills the generatedSchedules list by appending all the possible combination
   It receives no parameters
   It returns True in case all the combinations could be done properly
   In case something went wrong it returns False'''


def makeCombinations():
    # This for creates all the possible combinations of teachers between different courses
    myResult = myFunction(coursesDictionary.values())

    # Checks if it was an error in the user input
    if isinstance(myResult, list):
        # Everything is ok
        for combination in product(*myResult):
            # combination is a tuple that has a combination of teachers (it has the teacher name which is his key)   (Jorge, Yuen, Ivannia)

            #                         checks if the created combination has collisions
            generatedSchedules.append(checkCombination(combination))

        return True

    else:
        # There was an error on the users input
        return False


'''
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Front end
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''


'''-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
   This finds if a coordinate is part of the generated schedules
   It receives as parameter one of the approved teacher combinations, and both values of the coordinate
   In case the coordinate does exist in the combination, it returns the index of the teachers that holds it
   In case the coordinate does not exist in the combination, it returns none'''


def checkPositionInTuple(combination, i, j):
    # It adjust i variable, needed by the triple spaces
    i //= 4

    pos = 0
    # This for searches if a teacher has that schedule
    for teacher in combination:
        if (j, i) in teacher[-1]:
            # The teacher that has that position was found
            return pos

        pos += 1

    # There is not teacher that has that schedule
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
    if makeCombinations():
        # To write in the txt file
        f = open("testFile.txt", "a")

        f.truncate(0)

        # Initial message
        f.write('Asegurate de tener el ajuste de linea desactivado para evitar problemas con el formato visual de los horarios\n')
        f.write('Eso lo puedes revisar en:\n')
        f.write('\t-Menu superiror de Bloc de notas\n')
        f.write('\t-Formato\n')
        f.write('\t-Ajuste de linea debe estar sin seleccionar\n')
        f.write(' \n')
        f.write(' \n')

        # Base to print the hours of the schedule
        hoursList = ('|7:30 ', '|8:20 ', '|     ', '|---------', '|8:30 ', '|9:20 ', '|     ', '|---------', '|9:30 ', '|10:20', '|     ', '|---------', '|10:30', '|11:20', '|     ', '|---------', '|11:30', '|12:20',
                     '|     ', '|---------', '|13:00', '|13:50', '|     ', '|---------',  '|14:00', '|14:50', '|     ', '|---------',  '|15:00', '|15:50', '|     ', '|---------', '|16:00', '|16:50', '|     ', '|---------',  '|17:00', '|17:50',
                     '|     ', '|---------', '|18:00', '|18:50', '|     ', '|---------',  '|19:00', '|19:50', '|     ', '|---------', '|20:00', '|20:50', '|     ', '|---------', '|21:00', '|21:50', '|     ', '|---------')

        # Print the schedule for each created combination
        for combination in generatedSchedules:
            # Prints the days at the very first in the top for the combination
            f.write('          ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n')
            f.write('          |                    Lunes                     |                    Martes                    |                    Miercoles                 |                    Jueves                    |                    Viernes                   |                    Sabado                    |\n')
            f.write('----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n')

            # This for manages the vertical part, it has line jumps
            for i in range(56):
                # It prints the hour. Ex: 7:30  |
                if i%4 == 3:
                    # In this specific case the spaces are unnecessary
                    f.write(hoursList[i] + "|")
                else:
                    f.write(hoursList[i] + "    |  ")

                # This for manages the horizontal part, it goes on the same line
                for j in range(0, 6):
                    dataPos = i % 4  # Determines what part of the data will be printed, needed for the adjustment

                    if dataPos == 3:
                        # It is the turn of the separation between a block and the next one
                        f.write('-----------------------------------------------')

                    else:
                        # In this turn it may be data
                        foundTeacherPos = checkPositionInTuple(combination, i, j)  # Determines if it has data or not

                        if foundTeacherPos is None:
                            # It was not data
                            f.write('                                            |  ')

                        else:
                            # It is data

                            if dataPos == 0:
                                # It is the name of the course
                                stringToPrint = resizeStr(combination[foundTeacherPos][0])
                                f.write(stringToPrint + '        |  ')

                            elif dataPos == 1:
                                # It is the amount of credits
                                stringToPrint = resizeStr(str(combination[foundTeacherPos][1]) + ' creditos')
                                f.write(stringToPrint + '        |  ')

                            elif dataPos == 2:
                                # It is the name of the teacher
                                stringToPrint = resizeStr(combination[foundTeacherPos][2])
                                f.write(stringToPrint + '        |  ')

                # Prints a line jump at the end of each line of the schedule
                f.write(' \n')

            # Prints several spaces between a schedule and another to separate them
            f.write(' \n')
            f.write(' \n')
            f.write(' \n')
            f.write(' \n')
            f.write(' \n')

        # Closes the file
        f.close()


'''
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Gui
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''

'''
# Creates frame
root = tk.Tk()

# Frame dimensioning
canvas = tk.Canvas(root, width=600, height=500)
canvas.grid(columnspan=4, rowspan=4)

# Test label
lblTest = tk.Label(text='Hola', font='Raleway')
lblTest.grid(columnspan=3, column=1, row=0)

# Test label
tstBtnText = tk.StringVar()
tstBtnText.set('Boton')
btnTest = tk.Button(root, textvariable=tstBtnText, command=lambda:test(), font='Raleway', bg='#20bebe', fg='white', height=2, width=15)
btnTest.grid(column=1, row=2)

root.mainloop()'''

'''
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Run
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''


def test():
    addCourse("Analisis de Algoritmos", 4)
    addCourse("Seminarios de Estudios Filosoficos", 2)
    addCourse("Probabilidades", 4)
    addCourse("Matematica General", 3)
    addCourse("Arquitectura de Computadores", 4)

    addTeacherToCourse("Analisis de Algoritmos", "Algoritmos 1", [(1, 5), (1, 6), (3, 5), (3, 6)])
    addTeacherToCourse("Analisis de Algoritmos", "Algoritmos 2", [(1, 5), (1, 6), (3, 5), (3, 6)])
    addTeacherToCourse("Analisis de Algoritmos", "Algoritmos 3", [(1, 5), (1, 6), (3, 5), (3, 6)])
    addTeacherToCourse("Analisis de Algoritmos", "Algoritmos 4", [(1, 5), (1, 6), (3, 5), (3, 6)])
    addTeacherToCourse("Analisis de Algoritmos", "Algoritmos 5", [(2, 0), (2, 1), (4, 0), (4, 1)])

    addTeacherToCourse("Seminarios de Estudios Filosoficos", "Filosofo 1", [(2, 0), (2, 1), (4, 0), (4, 1)])

    addTeacherToCourse("Arquitectura de Computadores", "Arqui 1", [(2, 11), (2, 12), (4, 11), (4, 12)])

    addTeacherToCourse("Probabilidades", "Proba 1", [(1, 2), (1, 3), (3, 2), (3, 3)])

    addTeacherToCourse("Matematica General", "Mate 1", [(0, 0), (0, 1), (0, 2), (0, 3)])
    addTeacherToCourse("Matematica General", "Mate 2", [(1, 2), (1, 3), (3, 2), (3, 3)])

    printSchedule()


if __name__ == "__main__":
    test()

