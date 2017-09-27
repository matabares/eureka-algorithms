#138 - Street Numbers
import time
maxHouseNumber=20000000
count=0

def sumOfSeries(beginNumber,offset):
    return (offset*(beginNumber+(beginNumber+offset-1)))/2

start = time.time()
for houseToLiveIn in range(3,maxHouseNumber):
    if(count>9):
        break
    sumLeftNeighborhood=sumOfSeries(1,houseToLiveIn-1)
    for rightNeighborhood in range(2,maxHouseNumber):
        sumRightNeighborhood=sumOfSeries(houseToLiveIn+1,rightNeighborhood)
        if(sumLeftNeighborhood==sumRightNeighborhood):
            print(houseToLiveIn,houseToLiveIn+rightNeighborhood)
            count+=1
            break
        if(sumLeftNeighborhood<sumRightNeighborhood):
            break
end = time.time()
print(end-start)