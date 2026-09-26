play=input("DO you want to play a game?").lower()
crt=0
wrg=0
print("To win you have to score 4 out of 5")
if play=="yes":
    q1=input("Which is the  sweetest fruit in the world?").lower()
    if q1=="dates":
        crt+=1
    else: 
        wrg+=1
    q2=input("Who is the mosst populaar singer of 50's?").lower()
    if q2=="Elvis Presley":
        crt+=1
    else:
        wrg+=1
    q3=input("which is the biggest arena in the world?").lower()
    if q2=="narendra modi stadium":
        crt+=1
    else:
        wrg+=1
    q4=int(input("how many hours are there in a day?"))
    if q2==24:
        crt+=1
    else:
        wrg+=1
    q5=input("Name the National bird of India?").lower()
    if q2=="peacock":
        crt+=1
    else:
        wrg+=1
    if(crt>=4):
        print(f"Congragulations you won!! and your score is: {crt}")
    else:
        print(f"Oh no, you lost and your score is :{wrg}")
if play=="no":
    quit()
