import itertools

coursesDictionary = {}
keysList = []
generatedSchedules = []
'''coursesDictionary = {'Arquitectura': [{'Jorge': [(0,1),(0,2),(3,1),(3,2)], 'Kirstein': [(5,8),(6,9),(5,8),(6,9)]}, 4],
                        'Analisis': [{'Chinito': [(6,5),(7,2),(6,5),(7,2)], 'Ivannia': [(0,1),(0,2),(3,1),(3,2)]}, 4],
                        'Ingles': [{'Katherine': [(0,1),(0,2),(3,1),(3,2)], 'Daniel': [(0,1),(0,2),(3,1),(3,2)]}, 2]}
                        
   keysList = ['Arquitectura', 'Analisis', 'Ingles']
   generatedSchedules = [('Jorge', 'Chinito', 'Katherine'), ('Kirstein', 'Ivannia', 'Daniel'), ('Jorge', 'Ivannia', 'Daniel')]'''



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
   This function checks if a teacher combination is valid
   In case that a teacher crashes with another one, it returns False
   If the are no collisions at all it returns True
   It receives as parameter a tuple which is the combination'''


def checkCombination(combination):
    # Compares a single teacher with all the others
    i = 0  # Index for the current teacher
    for currentTeacher in combination:
        # Takes a single teacher to be compared

        j = 0  # Index of the comparison teacher per comparison iteration
        for comparisonTeacher in combination:
            if i != j:
                # It makes sure it is comparing 2 different individuals

                # The schedules are lists of tuples [(0,1),(0,2),(3,1),(3,2)]
                currentTeacherSchedule = coursesDictionary[keysList[i]][0][currentTeacher]  # current teacher
                comparisonTeacherSchedule = coursesDictionary[keysList[j]][0][comparisonTeacher]  # comparison teacher

                # Checks if one of the tuples of the currentTeacher is in the other teacher schedule
                for scheduleTuple in currentTeacherSchedule:
                    if scheduleTuple in comparisonTeacherSchedule:
                        # A collision was found
                        return False

            j += 1

        i += 1

    # Never found a collision
    return True


'''-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
   This function makes all the possible combinations of teachers of coursesDictionary
   It combines each teacher of course A, with each teacher of course B, with each teacher of course C and son on
   If fills the generatedSchedules list by appending all the possible combination
   It receives no parameters and does not return anything'''


def makeCombinations():
    # This for creates all the possible combinations of teachers between different courses
    for combination in itertools.product(*coursesDictionary.values()):
        # combination is a tuple that has a combination of teachers (it has the teacher name which is his key)   (Jorge, Yuen, Ivannia)

        # checks if the created combination has collisions
        if checkCombination(combination):
            # the combination had no collisions, it can be added
            generatedSchedules.append(combination)


'''-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
   Main function
   Currently used for tests'''


def main():
    addCourse("Analisis de Algoritmos", 4)
    addCourse("Arquitectura de Computadores",4)
    addCourse("Seminarios de Estudios Filosoficos", 2)
    addTeacherToCourse("Arquitectura de Computadores", "Jorge Vargas", [(4, 4), (4, 5), (6, 4), (6, 5)])
    addTeacherToCourse("Arquitectura de Computadores", "Kirstein Gatjens", [(0, 3), (0, 3), (2, 3), (2, 4)])
    addTeacherToCourse("Seminarios de Estudios Filosoficos", "Kirstein Gatjens", [(0, 3), (0, 3), (2, 3), (2, 4)])
    addTeacherToCourse("Analisis de Algoritmos", "Kirstein Gatjens", [(0, 3), (0, 3), (2, 3), (2, 4)])
    updateTeacherNameAll("Kirstein Gatjens", "Esteban Arias")


if __name__ == "__main__":
    main()