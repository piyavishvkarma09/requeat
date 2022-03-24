##Request question one
import requests
import json
from requests.api import request

import os
r=requests.get("https://api.merakilearn.org/courses")
# print(r)
a = r.json()
# print(a)

with open("courses1.json","w") as f:
    json.dump(a,f,indent=4)
#above code only for  1 time run get json file on local    
def getCourseList():
    with open("courses1.json","r") as file1:
        data=json.load(file1)
    c=0
    print("COURSE-NO    ||     COURSE NAME  ||      COURSE ID")
    for i in data:
        for j in i:
            if j=="name": 
                c=c+1
                print(c,i["name"],"ID:",i["id"])
                
    user=int(input("SELECT COURSE NO : "))    
    print("YOUR SELECTED COURSE : ")
    print("COURSE->ID :",data[user-1]["id"])
    print("     COURSE->NAME  :",data[user-1]["name"])
    user1=data[user-1]["id"]
    Ask_user1=input("PLEASE ENTER NEXT/N FOR next LIST and PRE/P for previous LIST: ")  
    if  Ask_user1=="N" or Ask_user1=='NEXT':
        r2=requests.get("https://api.merakilearn.org/courses/"+str(user1)+"/exercises")
        # print(r2)
        exe=r2.json()
        # print(b)
        with open("Course_data.json","w") as f2:
            json.dump(exe,f2,indent=4)
                #Above select Course Execercice JSON data  course_data.json 
        with open("Course_data.json","r") as f3:
            x=f3.read()
            exerciselist=json.loads(x)
            def getExerciselist(exerciselist):
                c3=0
                c4=0
                m=""
                for l in exerciselist["course"]["exercises"]:

                    if l["parent_exercise_id"]== None:
                        c3=c3+1
                        print(c3,l["name"],"ID:",l["id"]) 
                                        
                    elif l["id"]==l["parent_exercise_id"]:
                        c3=c3+1
                        m=l["parent_exercise_id"] 
                        print(c3,l["name"],"ID:",l["id"])
                        c4=0
                    else:
                        c4=c4+1
                        if m==l["parent_exercise_id"]:
                            print(" ",c4,l["name"],"ID:",l["id"])
            getExerciselist(exerciselist) 
            #above getCourseList of Excercise list Print
            Ask_user2=int(input("SELECT Excercise  NO : "))
            c3=0
            c4=0
            m=""
            list1=[]
            n=""
            for l in exerciselist["course"]["exercises"]:
                
                if l["parent_exercise_id"]== None:
                    c3=c3+1
                    if Ask_user2==c3:
                        n=l["parent_exercise_id"]
                        print(c3,l["name"],"ID:",l["id"])
                        print(l["content"]) 
                        break
                    c4=0                                  
                elif l["id"]==l["parent_exercise_id"]:
                    c3=c3+1
                    
                    if Ask_user2==c3 :
                        m=l["parent_exercise_id"]
                        print(c3,l["name"],"ID:",l["id"])
                        
                    c4=0
                else:
                    c4=c4+1
                    if m==l["parent_exercise_id"]:
                        print(" ",c4,l["name"],"ID:",l["id"])
                        list1.append(l["name"])
        # print(list1)
        if len(list1)>1:      
            Ask_user3=int(input("SELECT SUBTOPIC NO : "))
            def getSubExcercise(Ask_user3):
                for l in exerciselist["course"]["exercises"]:
                    # for i in range(len(list1)):
                    if m==l["parent_exercise_id"]:
                        if l["name"]==list1[Ask_user3-1]:
                            print( Ask_user3,l["name"]," ", l['id'])
                            print(l["content"])
                            if Ask_user3<=len(list1)-1:
                                user_input_for_subtopic=input("Please ENTER NEXT/N FOR next LIST and PRE/P for previous LIST:")
                                if user_input_for_subtopic=="N" or user_input_for_subtopic=="NEXT" :
                                    Ask_user3+=1
                                    getSubExcercise(Ask_user3)                               
                                else:
                                    getCourseList()
                            else:
                                 print("END COURSE   .\n THANK YOU")
                            break                   
            getSubExcercise(Ask_user3)            
        else:
            print("END COURSE   .\n THANK YOU ")
    elif Ask_user1=="P" or Ask_user1=="PRE":
        getCourseList()                                
getCourseList()