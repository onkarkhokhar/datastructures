a = [1,2,3,4,5,6,7,8]
import math
class Binheap:
    def __init__(self):
        self.heapList = []

        #heapsort
        self.sortedElements = []

    def percUp(self, i):
        while i//2 >= 0:
            #parent = self.heapList[i/2]

            if self.heapList[i] < self.heapList[i//2]:
                temp = self.heapList[i//2]
                self.heapList[i//2] = self.heapList[i]
                self.heapList[i] = temp
            if i//2 == 0:
                break
            i = i // 2

    def insert(self,k):
        self.heapList.append(k)
        self.percUp(len(self.heapList)-1)

    def percDown(self, i):
        while (2*i+2) <= len(self.heapList)-1 or (2*i+1) <= len(self.heapList)-1:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                temp = self.heapList[mc]
                self.heapList[mc] = self.heapList[i]
                self.heapList[i] = temp
                i = mc
            else:
                break

    def minChild(self,i):
        #find min of two childs
        if 2 * i + 1 == len(self.heapList)-1:
            return 2*i + 1
        elif self.heapList[2 * i + 1] > self.heapList[2 *i + 2]:
            return 2*i + 2
        else:
            return  2*i + 1

    def delRoot(self):
        last_element = self.heapList[-1]
        #appending popped elements to array heapsort
        self.sortedElements.append(self.heapList.pop(0))
        self.heapList.insert(0, last_element)
        self.heapList.pop(-1)
        self.percDown(0)


hp = Binheap()
hp.insert(5)
hp.insert(4)
hp.insert(3)
hp.insert(2)
hp.insert(1)


hp.delRoot()
hp.delRoot()
hp.delRoot()
hp.delRoot()
hp.delRoot()




print(hp.heapList)
print(hp.sortedElements)
