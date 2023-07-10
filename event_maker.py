text = """ 10:40 - 11:00am: Review what you hope to accomplish today and set clear and achievable goals for yourself. Take this time to motivate and encourage yourself to have a productive day.
11:00 - 11:45am: Apply for 5 internships
11:45 - 12:00pm: Break. Drink water and stretch.
12:00 - 2:00pm: Work on your German speaker project.
2:00 - 2:30pm: Break. Drink water and stretch.
2:30 - 4:30pm: Work on your Node website project
4:30 - 5:00pm: Break. Drink water and stretch.
5:00 - 6:00pm: Go to the gym for a workout
6:00 - 6:30pm: Break. Drink water and stretch.
6:30 - 7:30pm: Read your book for an hour.
7:30 - 9:30pm: Relax and unwind before bed.
9:30 - 11:59pm: Get ready for bed and set a plan for tomorrow. Drink water throughout the day so you reach your 2 liter goal.


"""
import logging

# Create a custom logger
logger = logging.getLogger(__name__)

# Create handlers
c_handler = logging.StreamHandler()
f_handler = logging.FileHandler('event_details.log')

c_handler.setLevel(logging.WARNING)
f_handler.setLevel(logging.INFO)

# Create formatters and add it to handlers
c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

c_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)

# Add handlers to the logger
logger.addHandler(c_handler)
logger.addHandler(f_handler)
#print(text)
from datetime import date
from datetime import datetime
from quickstart import main
input1="11:00 - 11:45am: Apply for 5 internships"
input2 = date.today()
def event_splitter(text):
  events = text.strip().split("\n") # splits prompt into many events
  for event in events:
        summary,start_time,end_time = event_detail_extraction(event,date.today())
        try :
            main(summary,start_time,end_time)
        except :
            print("didn't work")
        logger.info(f"Summary: {summary}")
        logger.info(f"Start time: {start_time}")
        logger.info(f"End time: {end_time}")
        pass
def event_detail_extraction(data1,data2 ):
    try :
        time, summary = data1.split(": ", 1)
        #print(f" time is {time} summary is {summary} " )
        try:
            start_time, end_time = time.split(" - ")
            #print(f" start time is {start_time} endtime  is {end_time} " )
            start_time = start_time.replace('am', '').replace('pm', '')
            start_time=  datetime.strptime(start_time, "%H:%M").time()
            end_time = end_time.replace('am', '').replace('pm', '')
            end_time=  datetime.strptime(end_time, "%H:%M").time()
            #print(f" start time is {start_time} endtime  is {end_time} " )
            start_time_final = datetime.combine(data2, start_time).isoformat()
            end_time_final = datetime.combine(data2, end_time).isoformat()
            print(f" start time is {start_time_final} endtime  is {end_time_final} " )

        except:
            print(" end time not given")
    except:
        print("crap")
        pass
    return summary,start_time_final,end_time_final
"""
 i need to create a function which will take the above mentioned inputs and 
 give me 3 outputs 
 summary = "Apply for 5 internships"
 start_time = '2023-07-11T11:00:00'
 end_time = '2023-07-11T11:45:00'
"""

summary,start_time,end_time = event_detail_extraction(input1,input2)
print(f"Summary: {summary}")
print(f"Start time: {start_time}")
print(f"End time: {end_time}")
def test1(data2,start_time):
    start_time=  datetime.strptime(start_time, "%H:%M").time()
    start_time_final = datetime.combine(data2, start_time).isoformat()
    print(start_time_final)
#test1(date.today(),"11:45" )
#event_splitter(text)
if __name__ == '__main__':
    event_splitter(text)