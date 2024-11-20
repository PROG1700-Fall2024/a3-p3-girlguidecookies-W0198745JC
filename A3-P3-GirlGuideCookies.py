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
    NumOfGuides=int(input("Enter the number of guides selling cookies: "))
    # parallel list woohoo 
    guideNames=[]
    boxesSold=[]
    for count in range(NumOfGuides):
        guide=input(f"Enter the name of guide #{count+1}: ")
        guideNames.append(guide)
        numOfBoxes=int(input(f"Enter the number of boxes sold by {guideNames[count]}: "))
        print("")
        boxesSold.append(numOfBoxes)

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

    prizes = ["Trip to Girl Guide Jamboree in Aruba!","Super Seller Badge","Left Over Cookies"]
    for i in range(len(guideNames)):
            if boxesSold[i] == max(boxesSold):     #Forgot about if/elif for a minute and over complicated it then came back and was like light bulb
                 print(f"{guideNames[i]}              - {prizes[0]}")
            elif boxesSold[i]>= CalcAvgBoxSold(boxesSold,guideNames):
                 print(f"{guideNames[i]}              - {prizes[1]}")
            elif boxesSold[i]>= 1:
                 print(f"{guideNames[i]}              - {prizes[2]}")
            else:
                 print(f"{guideNames[i]}              - ")

    # This program felt so much easier after the last 2 it really clicked 

    # YOUR CODE ENDS HERE

main()