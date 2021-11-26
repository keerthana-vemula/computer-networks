class Hamming:
    def __init__(self):
        file = open("input.txt","r")
        self.message = file.readline()
        print("input is",'"{}"'.format(self.message))

    def convertToBinary(self):
        self.ascii = []
        for i in self.message:
            x = (bin(ord(i)))[2:]
            self.ascii.append(('0' * (7 - len(x))) + x)
    
    def convertToHammingCode(self):
        for i in range(len(self.ascii)):
            x = self.ascii[i]
            x = x[:3]+'0'+x[3:6]+'0'+x[6]+'00'
            if (x[-1]+x[-3]+x[-5]+x[-7]+x[-9]+x[-11]).count('1') % 2 != 0:
                x = x[:10]+'1'
            if(x[-2]+x[-3]+x[-6]+x[-7]+x[-10]+x[-11]).count('1') % 2 !=0:
                x = x[:9] + '1' + x[10] 
            if (x[-4]+x[-5]+x[-6]+x[-7]).count('1') % 2!=0:
                x = x[-11:-4] + '1' +x[-3:]
            if (x[-8]+x[-9]+x[-10]+x[-11]).count('1') %2 !=0:
                x = x[-11:-8] +'1' + x[-7:]
            self.ascii[i] = x

    def checkHammingCode(self):
        for i in range(len(self.ascii)):
            x = self.ascii[i]
            if ((x[-1]+x[-3]+x[-5]+x[-7]+x[-9]+x[-11]).count('1') % 2 != 0) or ((x[-2]+x[-3]+x[-6]+x[-7]+x[-10]+x[-11]).count('1') % 2 !=0) or ((x[-4]+x[-5]+x[-6]+x[-7]).count('1') % 2!=0) or ((x[-8]+x[-9]+x[-10]+x[-11]).count('1') %2 !=0):
                print('Message has noise/incorrect')
                break
        else:
            print('Message is recieved without noise')

    def printRecievedMessage(self):
        print('Message recieved after using hamming code is:"',end="")
        for i in self.ascii:
            x = i[-11:-8] + i[-7:-4] + i[-3]
            print(chr(int(x,2)),end="")
        print('"')
if __name__ == '__main__':
    h = Hamming()
    h.convertToBinary()
    h.convertToHammingCode()    
    h.checkHammingCode()
    h.printRecievedMessage()




"""
output:
input is "keerthana is a good girl
"
Message is recieved without noise
Message recieved after using hamming code is:"keerthana is a good girl
"
"""
