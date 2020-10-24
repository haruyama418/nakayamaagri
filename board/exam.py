import tkinter as tk
import requests
from bs4 import BeautifulSoup
from tkinter import *
from time import *
import tkinter
from PIL import Image, ImageTk
## \n

root = tk.Tk()

fr1 = tk.Frame(root,bg='skyblue4',width=400,height=35,)
fr1.propagate(False) #フレームのpropagate設定 (この設定がTrueだと内側のwidgetに合わせたフレームサイズになる)
fr1.grid(column=0,row=0,columnspan=2,sticky=tk.W+tk.E)

fr2=tk.Frame(root,bg='hotpink2',width=200,height=100,)
fr2.propagate(False)
fr2.grid(column=0,row=1,sticky=tk.W+tk.E)

fr3=tk.Frame(root,bg='skyblue4',width=200,height=100)
fr3.propagate(False)
fr3.grid(column=1,row=1,sticky=tk.W+tk.E)

fr4=tk.Frame(root,bg='medium aquamarine',width=400,height=20)
fr4.propagate(False)
fr4.grid(column=0,row=2,columnspan=2,sticky=tk.W+tk.E)

fr5=tk.Frame(root,bg='aquamarine2',width=400,height=150)
fr5.propagate(False)
fr5.grid(column=0,row=3,columnspan=2,sticky=tk.W+tk.E)

fr6=tk.Frame(root,bg='medium aquamarine',width=400,height=27)
fr6.propagate(False)
fr6.grid(column=0,row=4,columnspan=2,sticky=tk.W+tk.E)

fr7=tk.Frame(root,bg='skyblue4',width=400,height=250)
fr7.propagate(False)
fr7.grid(column=0,row=5,columnspan=2,sticky=tk.W+tk.E)
#-----inner frame--------------------------------------------------------------------
fr5_1=tk.Frame(fr5,bg='skyblue4',width=66.6666667,height=150)
fr5_1.propagate(False)
fr5_1.grid(column=0,row=0,sticky=tk.W+tk.E)

fr5_2=tk.Frame(fr5,bg='skyblue4',width=66.6666667,height=150)
fr5_2.propagate(False)
fr5_2.grid(column=1,row=0,sticky=tk.W+tk.E)

fr5_3=tk.Frame(fr5,bg='skyblue4',width=66.6666667,height=150)
fr5_3.propagate(False)
fr5_3.grid(column=2,row=0,sticky=tk.W+tk.E)

fr5_4=tk.Frame(fr5,bg='skyblue4',width=66.6666667,height=150)
fr5_4.propagate(False)
fr5_4.grid(column=4,row=0,sticky=tk.W+tk.E)

fr5_5=tk.Frame(fr5,bg='skyblue4',width=66.6666667,height=150)
fr5_5.propagate(False)
fr5_5.grid(column=5,row=0,sticky=tk.W+tk.E)

fr5_6=tk.Frame(fr5,bg='skyblue4',width=66.6666667,height=150)
fr5_6.propagate(False)
fr5_6.grid(column=6,row=0,sticky=tk.W+tk.E)

"""
#----------------traffic------------------
def traffic():
    traffic_lb1 = tk.Label(fr1, text='運行状況:',bg='skyblue4',font=("", 14),foreground='white')
    traffic_lb1.grid(column=0,row=0,sticky=tk.W)
    #----------------odakyu------------------
    address = "https://www.odakyu.jp/cgi-bin/user/emg/emergency_bbs.pl"
    resp = requests.get(address)
    soup = BeautifulSoup(resp.text, 'html.parser')#resp.text
    odakyu = soup.find('p', class_='ttl_daiya_blue')
    odakyu=str(odakyu.text)
    print(odakyu)
    if "平常"in odakyu:
        traffic_lb2 = tk.Label(fr1, text="小田急線：平常運転",bg='skyblue4',font=("", 14,"bold"),foreground='white')
        traffic_lb2.grid(column=1,row=0,sticky=tk.W+tk.E,padx=10)
    else:
        traffic_lb2 = tk.Label(fr1, text=odakyu, foreground='white',bg='red',font=("", 14))
        traffic_lb2.grid(column=1, row=0,sticky=tk.W+tk.E)
    # ----------------Keio------------------
    address = "https://www.keio.co.jp/unkou/unkou_pc.html"
    resp = requests.get(address)
    soup = BeautifulSoup(resp.content, 'html.parser')#文字化け防止でresp.content
    keio = soup.find(class_='status')
    keio = str(keio.text)
    print(keio)
    if "平常"in keio:
        traffic_lb3 = tk.Label(fr1, text="京王線：平常運転", bg='skyblue4',font=("", 14,"bold"),foreground='white')
        traffic_lb3.grid(column=2, row=0,sticky=tk.W+tk.E,padx=8)
    else:
        traffic_lb3 = tk.Label(fr1, text=keio, foreground='white', bg='red',font=("", 14))
        traffic_lb3.grid(column=1, row=1, sticky=tk.W+tk.E)
    up_date= strftime('%H:%M:%S')
    time_label=tk.Label(fr1,text="最終更新:\n"+str(up_date),bg='skyblue4',font=("", 10),foreground='white')
    time_label.grid(column=3,row=0)
    root.after(100000, traffic)

traffic()

#------------時計--------------------------------------------------

buff = StringVar()
buff.set('')
buff2 = StringVar()
buff2.set('')
buff3 = StringVar()
buff3.set('')
#font1= tk.Fotnt(size=25)
day_label=Label(fr2,textvariable = buff3,bg='hotpink2', font=("",20),fg="white")
day_label.pack(anchor='w')
time=Label(fr2,textvariable = buff, bg="hotpink2",font=("Arial",55,"bold"),fg="white")
time.pack(side='left')
sec=Label(fr2,textvariable = buff2,bg='hotpink2', font=("",25),fg="white")
sec.pack(side='left',anchor='s')

def show_time():
    buff.set(strftime('%H:%M'))
    buff2.set(strftime('%S'))
    buff3.set(strftime('%m /%d (%a)'))
    root.after(1000, show_time)  #つまり、時間の取得を関数化して、毎秒行う

show_time()
"""
#--------------------------------------------------------------

#---------天気-----------------------------------------------------
def weather():
    address = "https://tenki.jp/forecast/3/17/4610/14137/"
    resp = requests.get(address)
    soup = BeautifulSoup(resp.text, 'html.parser')  # resp.text
    weather = soup.find('p', class_='weather-telop').text
    prb1 = soup.find_all('td')[0].text#probability of rain
    prb2 = soup.find_all('td')[1].text
    prb3 = soup.find_all('td')[2].text
    prb4 = soup.find_all('td')[3].text
    print(weather)
    print(prb1,prb2,prb3,prb4)
    # --週間天気予報------------------------------------------------------------
    day1_weather=soup.find_all(class_='weather-icon')[0].text
    day1_weather=day1_weather.strip()
    day1_high=soup.find_all("p",class_='high-temp')[0].text
    day1_low=soup.find_all("p",class_='low-temp')[0].text
    day1_rain=soup.find_all("p",class_='precip')[0].text

    day2_weather = soup.find_all(class_='weather-icon')[1].text
    day2_weather=day2_weather.strip()
    day2_high = soup.find_all("p", class_='high-temp')[1].text
    day2_low = soup.find_all("p", class_='low-temp')[1].text
    day2_rain = soup.find_all("p", class_='precip')[1].text

    day3_weather = soup.find_all(class_='weather-icon')[2].text
    day3_weather = day3_weather.strip()
    day3_high = soup.find_all("p", class_='high-temp')[2].text
    day3_low = soup.find_all("p", class_='low-temp')[2].text
    day3_rain = soup.find_all("p", class_='precip')[2].text

    day4_weather = soup.find_all(class_='weather-icon')[3].text
    day4_weather = day4_weather.strip()
    day4_high = soup.find_all("p", class_='high-temp')[3].text
    day4_low = soup.find_all("p", class_='low-temp')[3].text
    day4_rain = soup.find_all("p", class_='precip')[3].text

    day5_weather = soup.find_all(class_='weather-icon')[4].text
    day5_weather = day5_weather.strip()
    day5_high = soup.find_all("p", class_='high-temp')[4].text
    day5_low = soup.find_all("p", class_='low-temp')[4].text
    day5_rain = soup.find_all("p", class_='precip')[4].text

    day6_weather = soup.find_all(class_='weather-icon')[5].text
    day6_weather = day6_weather.strip()
    day6_high = soup.find_all("p", class_='high-temp')[5].text
    day6_low = soup.find_all("p", class_='low-temp')[5].text
    day6_rain = soup.find_all("p", class_='precip')[5].text
    print(day1_weather, day1_high, day1_low, day1_rain,
          day2_weather,day2_high,day2_low,day2_rain)
    # --------------------------------------------------------------
    if weather =="晴":
        txt="☀︎"
        bg="orange"
    elif weather =="晴時々曇":
        txt='☀︎/☁︎'
        bg="gray"
    elif weather =="晴時々雨":
        txt='☀︎/︎☔︎'
        bg="gray"
    elif weather =="晴のち曇":
        txt='☀‣︎☁︎'
        bg="gray"
    elif weather =="晴のち雨":
        txt='☀‣☔︎︎'
        bg="gray"


    elif weather == "雨":
        txt = "☔︎"
        bg = "royalblue"
    elif weather == "雨のち曇":
        txt = "☔︎‣︎☁︎"
        bg = "royalblue"
    elif weather == "雨のち晴":
        txt = "☔︎‣☀︎︎"
        bg = "royalblue"


    elif weather == "曇":
        txt = "☁︎"
    elif weather =="曇のち晴":
        txt="☁︎‣☀︎"
        bg="royalblue"
    elif weather =="曇のち雨":
        txt="☁‣☔︎"
        bg="royalblue"


    elif weather =="雪":
        txt="☃︎"
        bg="gray"
    elif weather =="雷":
        txt="🌪☔️"
        bg="royalblue"
    else:
        txt="?"
        bg="coral"
    tenki_label = tk.Label(fr3, text=weather+txt,font=("",40),bg="skyblue4",fg="white")
    tenki_label.pack(fill='x')
    #tenki_label2 = tk.Label(fr3, text=weather, font=("", 16), bg="skyblue4")
    #tenki_label2.pack(fill='x')
    rain_prob= tk.Label(fr3,text=str(prb1)+"|"+str(prb2)+"|"+str(prb3)+"|"+str(prb4),
                        font=("",27),bg='skyblue4',fg="white")
    rain_prob.pack()




    # ---週間天気予報ラベル-----------------------------------------------------------
    neweather_info = tk.Label(fr4, text="週間天気：", bg='skyblue4', fg="white", font=("", 16, "bold"))
    neweather_info.pack(anchor=tk.W)
    day1_date,day2_date,day3_date,day4_date,day5_date,day6_date=\
        int(strftime('%d'))+1,int(strftime('%d'))+2,int(strftime('%d'))+3,int(strftime('%d'))+4,int(strftime('%d'))+5,int(strftime('%d'))+6
    #month=strftime('%m')


    # ---day1_label-----------------------------------------------------------
    day1 = tk.Label(fr5_1, text=str(day1_date)+"日",bg="skyblue4",font=("", 14,"bold"), fg="white")
    day1.pack()
    day1_weather_lab = tk.Label(fr5_1, text=str(day1_weather), bg="skyblue4", font=("", 15),fg="white",)
    day1_weather_lab.pack()
    day1_high_lab= tk.Label(fr5_1, text=str(day1_high)+"℃",bg="skyblue4",fg="firebrick3",font=("", 15),)
    day1_high_lab.pack(fill="x")
    day1_low_lab = tk.Label(fr5_1, text=str(day1_low)+"℃", bg="skyblue4", fg="turquoise2",font=("", 15),)
    day1_low_lab.pack(fill="x")
    day1_rain_lab = tk.Label(fr5_1, text='-------\n'+str(day1_rain), bg="skyblue4", fg="white",font=("", 15),)
    day1_rain_lab.pack(fill="x")

    # ----day2_label----------------------------------------------------------
    day2 = tk.Label(fr5_2, text=str(day2_date) + "日", bg="skyblue4", font=("", 14, "bold"), fg="white")
    day2.pack()
    day2_weather_lab = tk.Label(fr5_2, text=str(day2_weather), bg="skyblue4", font=("", 15,), fg="white", )
    day2_weather_lab.pack()
    day2_high_lab = tk.Label(fr5_2, text=str(day2_high) + "℃", bg="skyblue4", fg="firebrick3", font=("", 15,), )
    day2_high_lab.pack(fill="x")
    day2_low_lab = tk.Label(fr5_2, text=str(day2_low) + "℃", bg="skyblue4", fg="turquoise2", font=("", 15, ), )
    day2_low_lab.pack(fill="x")
    day2_rain_lab = tk.Label(fr5_2, text='-------\n'+str(day2_rain), bg="skyblue4", fg="white", font=("", 15, ), )
    day2_rain_lab.pack(fill="x")
    # ----day3_label----------------------------------------------------------
    day3 = tk.Label(fr5_3, text=str(day3_date) + "日", bg="skyblue4", font=("", 14, "bold"), fg="white")
    day3.pack()
    day3_weather_lab = tk.Label(fr5_3, text=str(day3_weather), bg="skyblue4", font=("", 15), fg="white", )
    day3_weather_lab.pack()
    day3_high_lab = tk.Label(fr5_3, text=str(day1_high) + "℃", bg="skyblue4", fg="firebrick3", font=("", 15), )
    day3_high_lab.pack(fill="x")
    day3_low_lab = tk.Label(fr5_3, text=str(day1_low) + "℃", bg="skyblue4", fg="turquoise2", font=("", 15), )
    day3_low_lab.pack(fill="x")
    day3_rain_lab = tk.Label(fr5_3, text='-------\n' + str(day3_rain), bg="skyblue4", fg="white", font=("", 15), )
    day3_rain_lab.pack(fill="x")
    # ----day4_label----------------------------------------------------------
    day4 = tk.Label(fr5_4, text=str(day4_date) + "日", bg="skyblue4", font=("", 14, "bold"), fg="white")
    day4.pack()
    day4_weather_lab = tk.Label(fr5_4, text=str(day4_weather), bg="skyblue4", font=("", 15), fg="white", )
    day4_weather_lab.pack()
    day4_high_lab = tk.Label(fr5_4, text=str(day4_high) + "℃", bg="skyblue4", fg="firebrick3", font=("", 15), )
    day4_high_lab.pack(fill="x")
    day4_low_lab = tk.Label(fr5_4, text=str(day4_low) + "℃", bg="skyblue4", fg="turquoise2", font=("", 15), )
    day4_low_lab.pack(fill="x")
    day4_rain_lab = tk.Label(fr5_4, text='-------\n' + str(day4_rain), bg="skyblue4", fg="white", font=("", 15), )
    day4_rain_lab.pack(fill="x")
    # ----day5_label----------------------------------------------------------
    day5 = tk.Label(fr5_5, text=str(day5_date) + "日", bg="skyblue4", font=("", 14, "bold"), fg="white")
    day5.pack()
    day5_weather_lab = tk.Label(fr5_5, text=str(day5_weather), bg="skyblue4", font=("", 15), fg="white", )
    day5_weather_lab.pack()
    day5_high_lab = tk.Label(fr5_5, text=str(day5_high) + "℃", bg="skyblue4", fg="firebrick3", font=("", 15), )
    day5_high_lab.pack(fill="x")
    day5_low_lab = tk.Label(fr5_5, text=str(day5_low) + "℃", bg="skyblue4", fg="turquoise2", font=("", 15), )
    day5_low_lab.pack(fill="x")
    day5_rain_lab = tk.Label(fr5_5, text='-------\n' + str(day5_rain), bg="skyblue4", fg="white", font=("", 15), )
    day5_rain_lab.pack(fill="x")
    # ----day6_label----------------------------------------------------------
    day6 = tk.Label(fr5_6, text=str(day6_date) + "日", bg="skyblue4", font=("", 14, "bold"), fg="white")
    day6.pack()
    day6_weather_lab = tk.Label(fr5_6, text=str(day6_weather), bg="skyblue4", font=("", 15), fg="white", )
    day6_weather_lab.pack()
    day6_high_lab = tk.Label(fr5_6, text=str(day6_high) + "℃", bg="skyblue4", fg="firebrick3", font=("", 15), )
    day6_high_lab.pack(fill="x")
    day6_low_lab = tk.Label(fr5_6, text=str(day6_low) + "℃", bg="skyblue4", fg="turquoise2", font=("", 15), )
    day6_low_lab.pack(fill="x")
    day6_rain_lab = tk.Label(fr5_6, text='-------\n' + str(day6_rain), bg="skyblue4", fg="white", font=("", 15), )
    day6_rain_lab.pack(fill="x")
weather()



#--------------------------------------------------------------

#----just for fun--------------------------------------------------------
"""
move_btn=tk.Button(fr6,text="最新ニュース",command="move")
move_btn.pack(anchor=tk.W)
def move(flag,i):
    if(flag==True):
        i-=1
    elif i <= 0:
        breakpoint()
        print('fda')
    label.place(x=i,y=305)
    label.after(4,lambda: move(flag,i))

label=tk.Label(root,text="Labeltext")
i=400
flag=True
#move(flag,i)
move_btn.bind("<Button-1>", move(flag,i)) # by pushing btn do job(def)
move_btn.pack()
"""


#--------------------------------------------------------------


#-------NEWS-------------------------------------------------------

def news():
    address = "https://news.yahoo.co.jp/"
    resp = requests.get(address)
    soup = BeautifulSoup(resp.text, 'html.parser')  # resp.text
    contents = soup.find_all('li',class_='topicsListItem')
    for content in contents:
    #latest_news = soup.find_all('em',class_='title')
        print(content.text)
        main_news=tk.Label(fr7,text=":"+str(content.text),font=("",15,"bold"),bg='skyblue4',fg="white")
        #main_news.grid(column=0,columnspan=3,sticky=tk.W)
        main_news.pack(anchor=tk.W, )
    root.after(1000000, news)
news()






#--------color------------------------------------------------------
color=['gray','skyblue']
#--------------------------------------------------------------


root.mainloop()

