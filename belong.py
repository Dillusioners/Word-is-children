# * Author - jayspray
# * Team - Dillusioners
# * Word - Belongs
# * Info - This program checks in which line of a txt file a word belongs

#Display method for user
def user_display():
    print("#################################################################")
    print("     Find in which line of a txt file a word belongs to          ")
    print("#################################################################")

#Line cleaner method
#This method takes a line and splits it cleanly into its constituent word
def line_cleaner(l):
    #Splitting and storing line in clean_array[]
    clean_array = l.split()
    #Returning the clean_array[]
    return clean_array

#Heart of the program the solve method
def solve(path,word,f):
    #Length of the previously opened txt file
    length = len(f.readlines())
    #Closing the file
    f.close()
    #Opening it again to read from beginning
    data = open(path,'r')
    #Looping through lines
    for i in range(length):
        #Reading each line and cleaning them through the line_cleaner(l) method
        line = line_cleaner(data.readline())
        #Checking if word exists
        if word in line:
            print("Word is in line ",i+1)
            #If yes we print its line number and exit(0)
            exit()
    #Else it continues and says word is non existant
    #Closing file
    data.close()
    print("Word is not present in the txt file")
        
#The main method
def main():
    #Invoking user_display()
    user_display()
    #Try except block to handle any emergent errors
    try:
        #Inputting path with extension
        loc = input("Enter the path in which the file is in(WITH EXTENSION!!!) : ")
        #Opening file before calling solve() just to check if file exists
        f = open(loc,'r')
        #If it doesnt the except block catches it and terminates program
    except Exception as e:
        print("Oops something went wrong :(\nError -> ",e)
        #If file is existant we continue
    else:
        word = input("Enter the word you want to find : ")
        solve(loc,word,f)
    
#calling the main() method
main()
