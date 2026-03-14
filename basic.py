#this is first mini project i want to push into git
#this is an exam study timetables
import datetime
def subjects():
    sub={}
    n=int(input("enter the number of subjects: "))
    for i in range(n):
        name=input(f"enter {i+1} subject name: ")
        ex_date=input(f"Enter {i+1} exam date(dd-mm-yy):")
        date=datetime.datetime.strptime(ex_date,'%d-%m-%y')
        diff=int(input("enter the difficulty level: "))
        sub[name]={"Difficulty":diff ,  "Date":date}
    print(sub)
    return sub
def urgency(sub):    
    total=0
    hr=float(input("enter the daily study hours:  "))
    pr_date=datetime.datetime.now()
    urg_dict={}
    for k,v in sub.items():             #k is sub name , v is its value like math:{"diff":diff,"date":date}
        rem_days=(v["Date"]-pr_date).days
        if rem_days>0:

            urg_score=v["Difficulty"]/rem_days
            urg_dict[k]=urg_score               #here urg_dict[k] is math=urg_scrore basically storing urgency scores of that subject
            total+=urg_score                    # urg_dict={math(k):0.85(v)
    return urg_dict,total,hr                                                #     phy:0-75    }
def all(urg_dict,total,hr):            
    allocation={}
    for k,v in urg_dict.items():
        weight=v/total
        allocation[k]=round(weight*hr,2)        # like allocating each sub particular hrs
    print(urg_dict)
    print(allocation)
    return allocation
def save_to_json(subjects,urg_dict,allocation):
    import json
    
    temp = {}
    data={}
    for k,v in subjects.items():
        temp[k] = {
            "Difficulty": v["Difficulty"],
            "Date": v["Date"].strftime("%d-%m-%Y")
        }
    data["Subjects"]=temp
    data["Urgency Score:"]=urg_dict
    data["Allocation"]=allocation
    with open("examT.json","w") as f:
        json.dump(data,f,indent=4)
def main():
    s=subjects()
    save_to_json(s,urg_dict,allocation)
    urg_dict,total,hr=urgency(s)
    allocation=all(urg_dict,total,hr)
    print(f"Urgency score: {urg_dict}")
    print(f"Allocation: {allocation}")
main()