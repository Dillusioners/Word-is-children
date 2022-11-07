# * Author - jayspray
# * Team - Dillusioners
# * Word - experience
# * Info - This is my efficient solution to Euler problem after gaining experience as a programmer
# * Bibliography - https://projecteuler.net/problem=14

#Creating a dictionary where key is number and value is its collatz sequence amount
sequences = {1:1}
#Funcion to get sequence count of a number below 1 million
def sequence_count(num):
    #Initialising count
    count = 1
    #Running loop till number is not 1
    while num != 1:
        #Implementing the method of cacheing
        #This checks if the sequence count of a number which is a part of another numbers series exists or not
        #If it does we just add the sequence count from the dictionary
        if num in sequences:
            count += sequences.get(num)
            #Breaks once we know that number is already there in the dict
            break
        #Else we run it till it finishes
        else:
            #Condition for even number
            if num % 2 == 0:
                count += 1
                num /= 2
            #Condition for odd number
            else:
                count += 1
                num = num * 3 + 1
    #Returning the count
    return count
#Main method
def main():
    #Looping from 1 - 1000000
    for i in range(1,1000000):
        #Appending series count for verification in the dict
        sequences.update({i:sequence_count(i)})
    #Printing the number with largest series
    print(max(sequences,key = sequences.get))
#Invoking main method
main()
