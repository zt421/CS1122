'''
Zami Talukder
Into to CS
hw03
'''

#2,5
#Converts a number of  >11 base to a number of >11 base
#Parameters: n is the base to convert from, a is base to convert to
def convertBase(a,b):
    num = input("Enter number to convert from a to b")
    num = int(num,b) #converts number to base 10 first
    converted = ''
    answer = -1
    r = 0;
    while(answer != 0):  #converts base 10 number to the next base
        answer = num//a
        r = num%a
        converted = str(r) + converted
        num = answer
        
    print (converted)

#3
def number3():
    stringList = input("Enter a list:")
    stringList = stringList.split(" ")
    line = ""
    for i in range(0,len(stringList)):
        hex_str = stringList[i]
        hex_num = int(hex_str,16)
        line+=chr(hex_num)
        i+=1
    print(line)

#4
def number4():
    bin_num = input("Enter binary # to convert to hex #: ")
    print(hex(int(bin_num,2))) 


convertBase(8,10)
