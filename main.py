string = input("Please enter your own word: ")

char = input("Please eneter your own character: ")
i = 0
count = 0

while(i < len(string)): #loop through the string
    if(string[i] == char): #check if character matches
        count = count + 1 #increment count
    i = i + 1 #increment i
    print("The total number of times ", char, "has ocurred = " , count) #print the count