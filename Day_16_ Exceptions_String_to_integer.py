class Farhad:
    def faru(self,a):
        array=list(map(int,input().split()))#taking input in array
        #print(array)
        array.sort()
        #print(array)
        for i in range(a-1,-1,-1):
            if array[i]!=array[i-1]:
             print(array[i-1])
             break
farhad=Farhad()
a=int(input())
farhad.faru(a)