import random
from gtts import gTTS
import os
import passlib
import getpass
p1=input('enter you name player 1 ')
p2=input('enter your name player 2 ')
count=0
ps1=0
ps2=0
myobj=gTTS(text="Welcome "+str(p1)+ '&' +str(p2), lang='en',slow=True)
myobj.save("w.mp3")
os.system("mpg321 w.mp3")
while True:
     if count%2==0:
        li=[]
        inp=getpass.getpass("player 1 give your word to player 2 ")
        for x in range(len(inp)):
            li.append(inp[x])
        random.shuffle(li)
        d=""
        for x in range(len(li)):
            d=d+li[x]
        print("your word is ",d)
        inp2=input("enter ans ")
        if inp2==inp:
           ps2=ps2+1
           myobj=gTTS(text="Right Answer"+str(p2), lang='en',slow=True)
           myobj.save("w.mp3")
           os.system("mpg321 w.mp3")
           print("right ans your score is ",ps2)
        else:
           myobj=gTTS(text="Wrong Answer"+str(p2)+"correct answer is "+str(inp), lang='en',slow=True)
           myobj.save("w.mp3")
           os.system("mpg321 w.mp3")
           print("wrong ans right ans is ", inp)
           print("you score is"+ str(ps2),end='')
     if count%2 !=0:
        li=[]
        inp=getpass.getpass("player 2 give your word to player 1 ")
        for x in range(len(inp)):
            li.append(inp[x])
        random.shuffle(li)
        d=""
        for x in range(len(li)):
            d=d+li[x]
        print("Your word is ",d)
        inp2=input("enter ans ")
        if inp2==inp:
           ps1=ps1+1
           myobj=gTTS(text="Right Answer "+str(p1), lang='en',slow=True)
           myobj.save("w.mp3")
           os.system("mpg321 w.mp3")
           print("right ans your score is ",ps1)
        else:
           myobj=gTTS(text="Wrong Answer"+str(p1), lang='en',slow=True)
           myobj.save("w.mp3")
           print("wrong ans right ans is ", inp)
           print("your score is "+str(ps1),end='')
     fip=int(input("do you want to continue 1 for yes 0 for no "))
     if fip== 0:
        break
     count= count+1   
print("Thank you ")
                  
            
