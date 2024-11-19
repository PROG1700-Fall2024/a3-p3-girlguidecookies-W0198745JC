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
    print(f"The average number of boxes sold by each guide was {averageBoxes}")    
def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)
    NumOfGuides=int(input("Enter the number of guides selling cookies: "))

    guideNames=[]
    boxesSold=[]
    for count in range(NumOfGuides):
        guide=input(f"Enter the name of guide #{count+1}")
        guideNames.append(guide)
        numOfBoxes=input(f"Enter the number of boxes sold by {guideNames[count]}")
        boxesSold.append(numOfBoxes)

    printAvgBoxes(boxesSold,guideNames)







    # YOUR CODE ENDS HERE

main()