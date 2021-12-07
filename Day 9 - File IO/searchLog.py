# Python program to filter out search from a logcat

pathName = str(input("Enter the path/file name of your logcat:\n"))     #Checks the location of the file
sea = str(input("Enter the word you wish to search:\n"))

totalLog = True     #Check the variable as true, so as to pass it to the while loop later on
i = 0
f = open(f"{pathName}.txt")
while totalLog:     
    totalLog = f.readline()     # Reads each line of the file and stores it inside the variable 'totalLog'
    i += 1
    if sea in totalLog:
        print(f"The word {sea} is present on line number {i}")
        print(f"{totalLog}\n")

f.close()
