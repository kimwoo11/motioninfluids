import re

def removeZeros(position, time):
    index = [-1] * len(position)
    countPops = 0
    for i in range(len(position)):
        if position[i] == 0:
            index[i] = i
    for i in range(len(index)):
        if index[i] != -1:
            position.pop(i - countPops)
            time.pop(i - countPops)
            countPops+= 1
    return position, time

def dataToList():
    path = "C:/Users/Steve Kim/Desktop/motion in fluids/texts/t"
    time = {}
    position = {}   
    
    for i in range(30):
        dirPath = path + (str)(i+1) + ".txt"
        
        f = open(dirPath, "r")
        data = f.read()
        
        procData = re.split('\t|\n',data)
        
             

        for j in range(3):
            del procData[0]            
        
        timeList = [0] * len(procData)
        posList = [0] * len(procData)        
        
        for k in range(len(procData)):
            if (k%2 == 0):
                timeList[(int)(k/2)] = procData[k] #typecast because 0/2 is float
            else:
                posList[k//2] = procData[k]
        
        index = (str)(i+1)

        time[index] = timeList
        position[index] = posList    
        
    return time, position    
    
def getVelocityList(position, time):
    length = len(position)
    velocity = [0] * (length - 1)
    for i in range(length - 1):
        velocity[i] = (position[i+1] - position[i])/(time[i+1] - time[i])
    return velocity
    
def variance(y):
    N = len(y)
    yBar = sum(y)/N
    var = 0
    for i in range(N):
        var += (y[i] - yBar) ** 2
    var = var/(N-1)
    return var   
    
def getChiSquared(x, y, yInt, slope):
    chi2 = 0
    for i in range(len(x)):
        chi2 += (y [i] - yInt - slope * x[i]) ** 2
    chi2 = chi2/(variance(y))
    return chi2

if __name__ == "__main__":
    time, position = dataToList()

    