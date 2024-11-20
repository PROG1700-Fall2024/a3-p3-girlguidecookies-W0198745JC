#Program 3 – Girl Guide Cookies
#Description:   The organizers of the annual Girl Guide cookie sale event want to raise 
#               the stakes on the number of cookies sold and are offering cool prizes to
#               those guides who go above and beyond in their sales efforts. The organizers
#               want a program to print the guide list and their prizes.

#Student #:     w0198745
#Student Name:  Jenille Cheney 

def CalcAvgBoxSold(_boxesSold,_guideNames):
    return(sum(_boxesSold))/(len(_guideNames))
def printAvgBoxes(_boxesSold,_guideNames):
    averageBoxes=CalcAvgBoxSold(_boxesSold,_guideNames)
    print(f"The average number of boxes sold by each guide was {averageBoxes:.1f}")    # forgot it needed to be just 1 decimal place
def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)
    while (True):
        try:
            NumOfGuides=int(input("Enter the number of guides selling cookies: "))
            if NumOfGuides> 0:
                 break
            else:
                 print("The number of Guides must be greater than 0!")
        except ValueError:
             print("Invalid entry. Please enter a number greater than 0")
    print("")
    # parallel list woohoo 
    guideNames=[]
    boxesSold=[]
    for count in range(NumOfGuides):
        while(True):
                try:
                    guide=input(f"Enter the name of guide #{count+1}: ")
                    if guide and all(char.isalpha() or char.isspace()  for char in guide):   # i did use chat gpt for this specific line because i could not for the life of me get it to register a number as invalid only the blank entry . my prompt was this code asking for number error checking! 
                    # really cool the .isspace() used so that a two part name could still be entered !
                        guideNames.append(guide)
                        break
                    else:
                        print("Please Enter a Valid Name")
                except ValueError:
                     print("Number entered Please enter a valid name. ")
        while(True):
                try:
                    numOfBoxes=int(input(f"Enter the number of boxes sold by {guideNames[count]}: "))
                    print("")
                    if numOfBoxes>= 0:
                        boxesSold.append(numOfBoxes)
                        break
                    else:
                         print("Number of boxes sold must be 0 or more.")
                except ValueError:
                     print("Please enter a valid number")  
    #Really been enjoying the try-except error handling its so much easier than using just isalpha or isnumeric. (Boolean and I are working on being friends but it is not now)

    print("\n")
    printAvgBoxes(boxesSold,guideNames) #function with a return
    print("\n")
    print("Guide                Prizes Won:")
    print("-----------------------------------------------------------------")
   #prizes 
    #highest selling guide = Trip to GGJ in aruba
    #above average gets a badge
    # sells any split the remaining 
    # sells 0 GETS NOTHING

    prizes = ["Trip to Girl Guide Jamboree in Aruba!","Super Seller Badge","Left Over Cookies",""]
    for i in range(len(guideNames)):
            if boxesSold[i] == max(boxesSold):     #Forgot about if/elif for a minute and over complicated it then came back and was like light bulb
                 print(f"{guideNames[i]:<16} - {prizes[0]}")
            elif boxesSold[i]>= CalcAvgBoxSold(boxesSold,guideNames):
                 print(f"{guideNames[i]:<16} - {prizes[1]}")
            elif boxesSold[i]>= 1:
                 print(f"{guideNames[i]:<16} - {prizes[2]}")
            else:
                 print(f"{guideNames[i]:<16} - {prizes[3]}")

    # This program felt so much easier after the last 2 it really clicked 

    # YOUR CODE ENDS HERE

main()