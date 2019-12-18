import re
file = open('test_file.txt','w')
file.write("Anand 23 anandaugust9@gmail.com 7094315031")
file.write("\nInfant 23 infantarun@gmail.com 8932154678")
file.write("\nPraveen 23 praveen34@gmail.com 8874562153")
file.write("\nSaivignesh 23 saivignesh56@gmail.com 8932154678")
file.write("\nBalaji 23 balaji86@gmail.com 8932154678")
file.close()
#file = open('test_file.txt', 'r')
#content = file.readlines()
#print (content)
#file.close()
def fetchEmail(content):
    if re.match("(.*)@(.*).(.*)", content):
        return True
    return False
file = open('test_file.txt', 'r')
for line in file:
        for word in line.split():
            if (fetchEmail(word)):
                print(word)

        #print(word)