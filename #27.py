

def numberData(userNumbers):
    numData = len(userNumbers)
    return numData


def sortValues(userNumbers):
    sortedValues = sorted(userNumbers)
    return sortedValues


def sumValues(userNumbers):
    sum = 0
    for y in userNumbers:
        sum += y
    return sum


def averageVal(sumValues, numberData):
    avrVal = sumValues / numberData
    return avrVal


def medianVal(userNumbers):
    numData = numberData(userNumbers)
    sortMed = sortValues(userNumbers)
    if numData % 2 == 0:
        medVal = (sortMed[int((len(sortMed) - 1)/ 2)]  +  sortMed[int(len(sortMed) / 2 )]) / 2
    else:   
        medVal = sortMed[int((len(sortMed) - 1)/ 2)]
    return medVal


def modeVal(userNumbers):
    sortMode= sortValues(userNumbers)
    mode = sortMode[0]
    modeTimes = 0
    checkingValues = sortMode[0]
    checkingTimes = 0

    for i in range(0,len(sortMode)):
        if checkingValues == sortMode[i]:
            checkingTimes += 1
        else:
            if checkingTimes > modeTimes:
                mode = checkingValues
                modeTimes = checkingTimes
                checkingValues = sortMode[i]
                checkingTimes = 1
            else:
                checkingValues = sortMode[i]
                checkingTimes = 1
    
    if checkingTimes > modeTimes:
                mode = checkingValues
                modeTimes = checkingTimes
                
        
    return mode, modeTimes

def maxVal(userNumbers):
     sortMax = sortValues(userNumbers)
     maxi = sortMax[len(sortMax)-1]
     
     return maxi



def minVal(userNumbers):
     sortMin = sortValues(userNumbers)
     mini = sortMin[0]

     return mini

def ranVal(maxVal,minVal):
    rangeV = maxVal - minVal
    return rangeV

def variaDat(userNumbers):
    number = 0
    dataDev = numberData(userNumbers)
    avgDev = averageVal(sumValues(userNumbers) ,dataDev)
   
    for i in userNumbers:
       number += (i - avgDev)**2
       var = number / dataDev
    return var        

def stanDev(userNumbers): 
    var = variaDat(userNumbers)
    devStan = var **(1/2)
    return devStan

def geoMean(userNumbers):
    product = 1 
    dataGeo = numberData(userNumbers)
    for i in userNumbers:
        product *= i 
    geMean = product **(1 / dataGeo)
    return geMean
    
def menuCalc():
    print("WELCOME TO YOUR FAVORITE CALCULATORRRRR!!!!")
    Numbers = input("TYPE ANY NUMBER YOU WANT AND WE'LL GIVE YOU EVERYTHING ABOUT IT!: ")
    splitUserNum = (Numbers.split(","))
    userNumbers = [int(x) for x in splitUserNum]

    numData = numberData(userNumbers)
    sorVal = sortValues(userNumbers)
    sumVal = sumValues(userNumbers)
    avrgVal = averageVal(numData,sumVal)
    medVal = medianVal(userNumbers)
    modVal = modeVal(userNumbers)
    maxiVal = maxVal(userNumbers)
    miniVal = minVal(userNumbers)
    rangVal = ranVal(maxiVal,miniVal)
    variData = variaDat(userNumbers)
    staDev = stanDev(userNumbers)
    geoMe = geoMean(userNumbers)

    print(f'''THESE ARE YOUR FINAL RESULTSTSTTSTSTS!!!!!: 
              YOU ENTERED {numData} values
              THESE ARE: {userNumbers} 
              ARRANGED THEY LOOK LIKE: {sorVal}
              THE SUM OF THESE VALUES IS: {sumVal}
              THE MEAN(AVERAGE) IS: {avrgVal}, THE MEDIAN IS: {medVal} AND THE MODE ARE THESE VALUES: {modVal}
              THE LARGEST VALUE IS: {maxiVal} AND THE SMALLEST VALUE IS: {miniVal}, AND THE VALUE'S RANGE IS: {rangVal}
              THE STANDARD DEVIATION IS: {staDev} AND ITS VARIANCE IS: {variData}, AND TO WRAP THIS UP; THE GEOMETRIC MEAN IS {geoMe}
              THANK ME FOR THIS AMAZING CALCULATOR AND GIVE ME DONATIONS PLS!! :)''')

menuCalc()
