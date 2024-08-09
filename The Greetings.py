import datetime

current_time = datetime.datetime.now()

if(current_time.hour>=0 and current_time.hour < 12):
    print("good morning")
elif(current_time.hour>=12 and current_time.hour< 18):
    print("Good Afternoon")
elif(current_time.hour>=18 and current_time.hour<19):
    print("Good Evening")
elif(current_time.hour>=19 and current_time.hour< 23):
    print("Good Night")