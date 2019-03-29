def hello():
    name = input("What is your name?")
    print("Hello ", name)

#reads in a file and squashes it
def readFile():
     fileName=input("Please input the file name?")
    #fileName = "test.txt"
    file = open(fileName, "r")
    cleanFile = file.read()
    cleanFile = cleanFile.replace(" ", "")  #takes out all the spaces
    cleanFile = cleanFile.replace("\n", "") #takes out all the end lines
    cleanFile = cleanFile.lower()           #putts all to lower case
    print(cleanFile)                        #prints the squashed file
    for number in range(97, 123):           #for loop for counting
        count = cleanFile.count(chr(number))
        print(chr(number) + " " + str(count))
    for number in range(48, 58):
        count = cleanFile.count(chr(number))
        print(chr(number) + " " + str(count))


def arraySwitch(array):
    print(array)
    array.reverse()
    print(array)

#############################################
##########      Linked List       ##########
############################################

class Node:
    def __init__(self, value, nextNode=None):
        self.value = value
        self.nextNode = nextNode

    def checkLoop(self):
        node=self
        dictionary = {}
        while(node!=None):
            if node in dictionary.keys():
                return 1
            dictionary[node] = True
            node = node.nextNode
        return 0









#############################################
##########      Call it       ##########
############################################


# hello()
# readFile()
array=[1,2,3,4,5,6,7,8,9]
arraySwitch(array)


node1 = Node(11)
node2 = Node(56)
node3 = Node(42)
node1.nextNode = node2 # 11->56
node2.nextNode = node3 # 56->42
#node3.nextNode=node1  #un comment this to make a loop

print(node1.checkLoop())
input("Press enter to exit")
