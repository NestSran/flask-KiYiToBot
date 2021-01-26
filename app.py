from flask import Flask,request,abort
import requests ##ส่งข้อความกลับLine
import json ##Line Using Json only
#from Project.Config import* 
from datetime import datetime,date
from pprint import pprint
import sys
#sys.path.append("D:\\Users\PEA\Desktop\KiYiToBot\Calendar")
from Project.mygoogle import Create_Service


app = Flask(__name__)


#Authorizing GoogleCalendar

CLIENT_SECRET_FILE = 'credentials.json'
API_NAME = 'calendar'
API_VERSION = 'V3'
SCOPES = ['https://www.googleapis.com/auth/calendar']

service = Create_Service(CLIENT_SECRET_FILE,API_NAME,API_VERSION,SCOPES)

# Find CalendarID

#find_calendar_id =service.calendars().get(calendarId='primary').execute()
#calendar_id= find_calendar_id["id"]
Channel_access_token ='ve4MtHBnXqxyFK2Uhg5oalJMZJQYMEstRvNjdEFZSTiWk0/hEyNW/X/iJnOssxUpGQ0K4bh1xnhtSR9zNuTjbELgGhjo5IkNeSuYE1OdMheGjtCRaDTw6rAf8BvMwghtAzuNbS60EmMBcBlkUb+jiAdB04t89/1O/w1cDnyilFU='

#Line Chatbot
   
@app.route('/webhook',methods=['GET','POST'])
def webhook():
    if request.method == 'POST':
        payload = request.json

        Reply_token = payload['events'][0]['replyToken']
        print(Reply_token)
        message = payload['events'][0]['message']['text']
        print(message)
  
        if "คิยิโตะ"  in message and "แนะนำตัว" in message :
            Reply_messasge = 'สวัสดีครับ น้องชื่อคิยิโตะ (KiYiTo) เป็นหุ่นยนต์อัตโนมัติมาช่วยแจ้งเตือนกิจกรรม PSC(PEA Safety Culture) ประจำกฟส.อ.คลองใหญ่'
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        
        elif "คิยิโตะ"  in message and "สบายดี" in message :
            Reply_messasge = 'สบายดีครับ ขอบคุณนะครับ'
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)

        elif "คิยิโตะ"  in message and "ใช้งาน" in message :
            Reply_messasge = """น้องจะแจ้งเตือนผู้ที่จะดำเนินกิจกรรม PSC(PEA Safety Culture) แต่ละสัปดาห์ก่อนล่วงหน้า 1 วันเวลา 8:45 A.M.นะครับ 
                                **หมายเหตุ :ถ้าหากจะเปลี่ยนแปลงเวรผู้ที่จะดำเนินกิจกรรมให้แจ้งพี่เนสล่วงหน้าอย่างช้าสุด 2 วันก่อนถึงการทำกิจกรรมนะครับ"""
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        
        elif "คิยิโตะ"  in message and "อัพเดตตารางเวร" in message :
            Reply_messasge = "รับทราบครับ กำลังอัพเดตตารางเวร PSC(PEA Safety Culture) ประจำกฟส.อ.คลองใหญ่"
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
            notify_PSC()

        elif "คิยิโตะ"  in message and "เนส" in message :
            Reply_messasge = 'ใช่คนที่หน้าตาดีในกฟส.คลองใหญ่ใช่ไหมงับ อิอิ'
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)

        elif "คิยิโตะ"  in message and "อ้อฟ" in message :
            Reply_messasge = 'โวโวเย่เย้...พวก!!ขอให้ทุกท่านโชคดี+_+ ห้าๆ'
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        
        elif "คิยิโตะ"  in message and "โอ้ต" in message :
            Reply_messasge = 'ช่วงนี้เข้าจันทบุรีไม่ได้ เข้าวัดแทนนะครับ haha'
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)

        elif "คิยิโตะ"  in message and "ลา" in message :
            Reply_messasge = 'เย็นนี้เหรอ เหรอ หาปลาดิ'
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        
        elif "คิยิโตะ"  in message and "โหน่ง" in message :
            Reply_messasge = 'ใครเอามะม่วงสุกมา....(วิ่ง)'
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)

        elif "คิยิโตะ"  in message and "ตู้" in message :
            Reply_messasge = 'น้องเอ้....พี่มีอะไรจะคุยด้วย ห้าๆ'
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)

        elif "คิยิโตะ"  in message and "เปิ้ล" in message :
            Reply_messasge = 'คืออย่างงี้นา......'
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        
        elif "คิยิโตะ"  in message and "ยูง" in message :
            Reply_messasge = 'อ้อฟ หนมหวานป่าว'
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        
        elif "คิยิโตะ"  in message and "ฟรุค" in message :
            Reply_messasge = 'มีใครอยากทานอะไรไหมครับ (เชฟฟรุค)'
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)

        elif "คิยิโตะ"  in message and "เอ้" in message :
            Reply_messasge = 'พี่ตู้....ขอสาระ ห้าๆ'
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)

        elif "คิยิโตะ"  in message and "เอ๋" in message :
            Reply_messasge = 'มาๆมื้อนี้พี่เลี้ยงเอง'
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)

        elif "คิยิโตะ"  in message and "ตุ่น" in message :
            Reply_messasge = 'ว.เนสส พี่ว่านาา...'
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)

        elif "คิยิโตะ"  in message and "อุ้ม" in message :
            Reply_messasge = 'ว.เนสส พี่ลองทำขนมมาให้ชิม'
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)

        elif "คิยิโตะ"  in message and "อาย" in message :
            Reply_messasge = 'เจอน้ำจิ่มรสเด็ดต้องจัดหมูกระทะสักหน่อย'
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)

        elif "คิยิโตะ"  in message and "ยุ้ย" in message :
            Reply_messasge = 'พี่เนส....มารับตังค่ะ'
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        
        elif "คิยิโตะ"  in message and "ไก่" in message :
            Reply_messasge = 'เรียบร้อยสุดๆ ผบง.ใช่เหรอ?'
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)

        elif "คิยิโตะ"  in message and "ตั๋ง" in message :
            Reply_messasge = 'เป็นไงบ้างวัยรุ่น ROVซักตาไหมหละ'
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)

        elif "คิยิโตะ"  in message and "นพ" in message :
            Reply_messasge = 'กุ้งซักกิโลไหมหล่ะ (เงืนเหลือครับ)'
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)

        elif "คิยิโตะ"  in message and "โน้ต" in message :
            Reply_messasge = 'จะสร้างอพาร์ทเมนต์กี่ห้องดี'
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)

        elif "คิยิโตะ"  in message and "โป้ง" in message :
            Reply_messasge = 'ฮึฮึ พูดวันละ10ประโยค(ยิ้มอ่อน)'
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)

        elif "คิยิโตะ"  in message and "นิว" in message :
            Reply_messasge = 'เขอะ...ทำดาที่ไหน'
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        
        elif "คิยิโตะ"  in message and "บาส" in message :
            Reply_messasge = 'พูดวันละ5ประโยค(ยิ้มอ่อน)'
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)

        elif "คิยิโตะ"  in message and "มด" in message :
            Reply_messasge = 'อยู่ระหว่างดำเนินการหาประโยคเด็ด'
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)

        elif "คิยิโตะ"  in message and "ทัก" in message :
            Reply_messasge = 'นี่ว.เนส ห.จะบอกให้นา...(ลุกลี้ลุกลน)'
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        
        elif "คิยิโตะ"  in message and "โต้ง" in message :
            Reply_messasge = 'อืม...ฮึฮึ'
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)

        elif "คิยิโตะ"  in message and "บาส" in message :
            Reply_messasge = 'พูดวันละ5ประโยค(ยิ้มอ่อน)'
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        
        elif "คิยิโตะ"  in message and "แม็ก" in message :
            Reply_messasge = 'ของหวานกินไม่เป็น แอลกอฮอลเท่านั้น (ช่วงโควิดหนะ)'
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        
        elif "คิยิโตะ"  in message and "อ้อม" in message :
            Reply_messasge = 'ว.เนส เซ็นชื่อด้วย...'
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        
        elif "คิยิโตะ"  in message and "ดี้" in message :
            Reply_messasge = 'ผมอยากจะเลี้ยงข้าว มีใครสนใจไหมครับ'
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)

        return request.json, 200

    elif request.method == 'GET':
        return 'this is method GET!!!',200

    else:
        abort(400)




def ReplyMessage(Reply_token, TextMessage, Line_Acees_Token):
    LINE_API = 'https://api.line.me/v2/bot/message/reply'

    Authorization = 'Bearer {}'.format(Line_Acees_Token) ##Channel_access_token เพื่อยืนยันตัวตน
    print(Authorization)
    
    ##เงื่อนไข LINE_API
    headers = {   ##Head ศึกษา HttpMethod,RestAPI
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization':Authorization
    }

    data = {   ##Body
        "replyToken":Reply_token,
        "messages":[{
            "type":"text",
            "text":TextMessage
        }]
    }

    data = json.dumps(data) ## dump dict >> Json Object
    r = requests.post(LINE_API, headers=headers, data=data) 
    return 200 



#Date Today Convert to Int
yeartoday = int(date.today().strftime("%Y"))
monthtoday = int(date.today().strftime("%m"))
beforetoday = int(date.today().strftime("%d"))-1
nowtoday = int(date.today().strftime("%d"))
list_beforeday = [yeartoday,monthtoday,beforetoday]
list_nowtoday = [yeartoday,monthtoday,nowtoday]


#Time Today, Isoformat
isoformat = datetime.now().isoformat(timespec='seconds')+'Z'
now_today = datetime.now().isoformat(timespec='seconds')
time_today = now_today.split("T")[1]
#Convert Datetime to String and Int
str_time_today = datetime.strptime(time_today,"%H:%M:%S")
get_hour_today = int(str_time_today.strftime("%H"))
get_minute_today = int(str_time_today.strftime("%M"))
get_second_today = int(str_time_today.strftime("%S"))
list_timetoday = [get_hour_today,get_minute_today,get_second_today]



#call event date <Google Calendar>
def call_eventdate(): 
    events = service.events().list(calendarId='saran.kan.pea@gmail.com',timeZone='Asia/Bangkok',timeMin=isoformat,orderBy='startTime',singleEvents=True,maxResults=1).execute()
   
    for event in events['items']:
        # StringToInt
        front_date = event['start']['dateTime'].split('+')[0].split('T')[0]
        back_time = event['start']['dateTime'].split('+')[0].split('T')[1]

        # String To Datetime 
        global list_beforedate
        global list_date
        global list_timeevent

        convert_front_date = datetime.strptime(front_date,"%Y-%m-%d")
        convert_back_time = datetime.strptime(back_time,"%H:%M:%S")

        #1. Convert Datetime to String and Int for Notify 1day in advance
        get_beforeday =int(convert_front_date.strftime("%d"))-1
        get_day =int(convert_front_date.strftime("%d"))
        get_month = int(convert_front_date.strftime("%m"))
        get_year = int(convert_front_date.strftime("%Y"))

        list_beforedate = [get_year,get_month,get_beforeday]
        list_date = [get_year,get_month,get_day]
        
        
        #2. Convert time to String and Int for Notify 1day in advance
        get_hour = int(convert_back_time.strftime("%H"))
        get_minute = int(convert_back_time.strftime("%M"))
        get_second = int(convert_back_time.strftime("%S"))
        

        list_timeevent = [get_hour,get_minute,get_second]
        

        break

call_eventdate()

#Retrieve Event From GoogleCalendar to Dict
def left_event():

    global event_left
    event_left={}
    kyt_queue=["Name:","Time:"]
    page_token = None
    while True:
        events = service.events().list(calendarId='saran.kan.pea@gmail.com', pageToken=page_token,timeZone='Asia/Bangkok',timeMin=isoformat,orderBy='startTime',singleEvents=True,maxResults=100).execute()
        print(events)
        i=0
        
        for event in events['items']:
                
            print(event['start']['dateTime'])    
            
            event_left[i]={}
            
            for x in kyt_queue :    
                
                if x=="Name:" :
                    event_left[i][x]=event['summary']
                
                
                if x=="Time:" :
                    event_left[i][x]=event['start']['dateTime'].split("T")[0]
            
            i+=1
            
                    
        page_token = events.get('nextPageToken')
        if not page_token:
            break


#Line Notify For PSC Event
def notify_PSC():
        left_event()
    

        url = 'https://notify-api.line.me/api/notify'
        token = 'm2qR578FQC7qlcj1WUVElQ0Wmq6NPCc6zNfSf2vuaZJ'

        headers = {
                    'content-type':
                    'application/x-www-form-urlencoded',
                    'Authorization':'Bearer '+token
                  }
        intro = "ประกาศ !!เวรการดำเนินกิจกรรม PSC (PEA SAFETY CULTURE) กฟส.อ.คลองใหญ่ "
    
       
        msg= intro
        r = requests.post(url, headers=headers , data = {'message':msg})
        print(r.text)
        

        for i in event_left :
            if i==3:
                break
            else:
                msg1 = "เวร :{}".format(event_left[i]["Name:"])
                msg2 = "ประจำวันที่:{}".format(event_left[i]["Time:"])
                
                r1 = requests.post(url, headers=headers , data = {'message':msg1})
                r2 = requests.post(url, headers=headers , data = {'message':msg2})
                print(r1.text)
                print(r2.text)
        

    
if list_nowtoday == list_beforedate :

    if list_timetoday == list_timeevent:
    
            notify_PSC()
    else:
        pass


else:
    pass


if __name__== '__main__':
    
    app.run(host='127.0.0.1',port=4000)
    
    