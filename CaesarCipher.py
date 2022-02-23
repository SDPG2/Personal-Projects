import pyfiglet

#Translate the Message
#Match the position of each letter in the word with the position it is in in the alphabet list
#Add the counter and append new letter into a list
#Output the message
def Encrypt(word, counter):
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    TransMessage = [] #The translated word variable


    for x in range(0,len(word)): #For every letter in the message, find the position of the letter and add the counter
        count = 0
        pos = 0
        while True:
            if word[x] == alphabet[count]:
                pos = count
                break
            else:
                count+=1
        if (pos + counter) > len(alphabet):
            letterPos = (pos + counter) - len(alphabet)
            TransMessage.append(alphabet[letterPos])
        else:
            TransMessage.append(alphabet[pos + counter])

        
    
    print(*TransMessage)

    
#Converts the user response to accept valid arguments
#Convert string to all lowercase to match with alphabet
#Eliminate spaces in the string if present
#Convert the number inputed as an integer
def Translate(message, count):
    toLower = message.lower()
    strConvert = ''.join(toLower.split())
    intConvert = int(count)
    Encrypt(strConvert, intConvert)

#Driver Code
#Allow input of message and of counter
def main():
    print(pyfiglet.figlet_format("Caesar Cipher\n"))
    cipher = input('Enter a message\n')
    counter = input('Enter a counter\n')
    Translate(cipher, counter)


main()   